import matplotlib.pyplot as plt
import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='gametheory'
)
cursor = connection.cursor()

# Fetch data for 3h4: tournaments
cursor.execute("""
    SELECT t.tournament_id, 
           SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
    FROM PLAYERS p
    JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
    JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
    WHERE t.tournament_id LIKE '3h4:%'
    GROUP BY t.tournament_id;
""")
results_3h4 = cursor.fetchall()

# Fetch data for 3h0: tournaments
cursor.execute("""
    SELECT t.tournament_id, 
           SUM(p.coop_count) / (COUNT(m.tournament_id) * t.game_length * 2) AS cooperation_rate
    FROM PLAYERS p
    JOIN TOURNAMENTS t ON p.tournament_id = t.tournament_id
    JOIN MATCHUPS m ON p.tournament_id = m.tournament_id
    WHERE t.tournament_id LIKE '3h0:%'
    GROUP BY t.tournament_id;
""")
results_3h0 = cursor.fetchall()

cursor.close()
connection.close()

# Process results
tournament_ids_3h4, cooperation_rates_3h4 = zip(*results_3h4) if results_3h4 else ([], [])
tournament_ids_3h0, cooperation_rates_3h0 = zip(*results_3h0) if results_3h0 else ([], [])

# Plot
plt.figure(figsize=(10, 6))

# Plot 3h4: tournaments
plt.bar(tournament_ids_3h4, cooperation_rates_3h4, color='blue', label='3h4: Tournaments')

# Plot 3h0: tournaments
plt.bar(tournament_ids_3h0, cooperation_rates_3h0, color='green', label='3h0: Tournaments', alpha=0.7)

# Labels and legend
plt.xlabel('Tournament IDs')
plt.ylabel('Cooperation Rate')
plt.title('Cooperation Rate for Tournaments Starting with "3h4:" and "3h0:"')
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()

