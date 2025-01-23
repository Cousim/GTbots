import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.weightstats import DescrStatsW
from decimal import Decimal

class GameTheoryAnalysis:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='gametheory'
        )
        self.cursor = self.connection.cursor()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def calculate_confidence_interval(self, data, alpha=0.05):
        if len(data) > 1:
            stats = DescrStatsW(data)
            mean = float(stats.mean)
            lower, upper = stats.tconfint_mean(alpha=alpha)
            return float(mean), float(lower), float(upper)
        elif len(data) == 1:
            value = float(data[0])
            return value, value, value
        else:
            return None, None, None

    def process_results(self, results):
        labels, cooperation_rates = zip(*results) if results else ([], [])
        cooperation_rates = [float(rate) if isinstance(rate, Decimal) else rate for rate in cooperation_rates]
        return [str(label) for label in labels], cooperation_rates

    def analyze(self):
        # Fetch data
        results_3h4 = self.fetch_data("""
            SELECT 'Open' AS label, 
                   SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
            FROM PLAYERS p
            JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
            JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
            WHERE t.tournament_id LIKE '3h4:%'
            GROUP BY t.tournament_id;
        """)

        results_3h0 = self.fetch_data("""
            SELECT ROUND(AVG(p.assume_commit_prob), 2) AS label, 
                   SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
            FROM PLAYERS p
            JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
            JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
            WHERE t.tournament_id LIKE '3h0:%'
            GROUP BY t.tournament_id;
        """)

        results_3h10 = self.fetch_data("""
            SELECT 'Open' AS label, 
                   SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
            FROM PLAYERS p
            JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
            JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
            WHERE t.tournament_id LIKE '3h10:%'
            GROUP BY t.tournament_id;
        """)

        results_3h6 = self.fetch_data("""
            SELECT ROUND(AVG(p.assume_commit_prob), 2) AS label, 
                   SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
            FROM PLAYERS p
            JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
            JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
            WHERE t.tournament_id LIKE '3h6:%'
            GROUP BY t.tournament_id;
        """)

        # Process results
        labels_3h4, cooperation_rates_3h4 = self.process_results(results_3h4)
        labels_3h0, cooperation_rates_3h0 = self.process_results(results_3h0)
        labels_3h10, cooperation_rates_3h10 = self.process_results(results_3h10)
        labels_3h6, cooperation_rates_3h6 = self.process_results(results_3h6)

        # Convert to numpy arrays for analysis
        coop_rates_3h4 = np.array(cooperation_rates_3h4)
        coop_rates_3h0 = np.array(cooperation_rates_3h0)
        coop_rates_3h10 = np.array(cooperation_rates_3h10)
        coop_rates_3h6 = np.array(cooperation_rates_3h6)

        # Confidence intervals and p-values
        mean_3h4, ci_lower_3h4, ci_upper_3h4 = self.calculate_confidence_interval(coop_rates_3h4)
        mean_3h0, ci_lower_3h0, ci_upper_3h0 = self.calculate_confidence_interval(coop_rates_3h0)
        t_stat_3h4_3h0, p_value_3h4_3h0 = ttest_ind(coop_rates_3h4, coop_rates_3h0, equal_var=False)

        mean_3h10, ci_lower_3h10, ci_upper_3h10 = self.calculate_confidence_interval(coop_rates_3h10)
        mean_3h6, ci_lower_3h6, ci_upper_3h6 = self.calculate_confidence_interval(coop_rates_3h6)
        t_stat_3h10_3h6, p_value_3h10_3h6 = ttest_ind(coop_rates_3h10, coop_rates_3h6, equal_var=False)

        # Print results
        print("3h4 Cooperation Rates:")
        print(f"Mean: {mean_3h4:.2f}, CI: [{ci_lower_3h4:.2f}, {ci_upper_3h4:.2f}]")
        print("3h0 Cooperation Rates:")
        print(f"Mean: {mean_3h0:.2f}, CI: [{ci_lower_3h0:.2f}, {ci_upper_3h0:.2f}]")
        print(f"T-test p-value (3h4 vs. 3h0): {p_value_3h4_3h0:.5f}")

        print("3h10 Cooperation Rates:")
        print(f"Mean: {mean_3h10:.2f}, CI: [{ci_lower_3h10:.2f}, {ci_upper_3h10:.2f}]")
        print("3h6 Cooperation Rates:")
        print(f"Mean: {mean_3h6:.2f}, CI: [{ci_lower_3h6:.2f}, {ci_upper_3h6:.2f}]")
        print(f"T-test p-value (3h10 vs. 3h6): {p_value_3h10_3h6:.5f}")

        # Plot results
        self.plot_results(labels_3h4, cooperation_rates_3h4, labels_3h0, cooperation_rates_3h0, "3h4 & 3h0")
        self.plot_results(labels_3h10, cooperation_rates_3h10, labels_3h6, cooperation_rates_3h6, "3h10 & 3h6")

    def plot_results(self, labels_a, rates_a, labels_b, rates_b, title_suffix):
        combined_labels = labels_a + labels_b
        combined_rates = rates_a + rates_b

        colors = ['yellow'] * len(labels_a) + ['blue'] * len(labels_b)

        plt.figure(figsize=(10, 6))
        plt.bar(combined_labels, combined_rates, color=colors, alpha=0.7)
        plt.xlabel('Tournament Type or Bot Assume Commit Rate')
        plt.ylabel('Cooperation Rate')
        plt.title(f'Cooperation Rate: {title_suffix}')
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()
        plt.show()

    def close(self):
        self.cursor.close()
        self.connection.close()

# Create instance and run analysis
analysis = GameTheoryAnalysis()
analysis.analyze()
analysis.close()
