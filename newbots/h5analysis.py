import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to MySQL database
db_config = {
    'host': 'localhost',          
    'user': 'root',              
    'password': '1234',           
    'database': 'gametheory'      
}

conn = mysql.connector.connect(**db_config)

# Step 2: Query the MATCHUPS table
query = """
SELECT
    tournament_id,
    player1_id,
    player2_id,
    player1_commitment,
    player2_commitment,
    history
FROM MATCHUPS;
"""

matchups_df = pd.read_sql(query, conn)

# Step 3: Close the database connection
conn.close()

# Step 4: Function to calculate cooperation rate
def calculate_cooperation_rate(history):
    moves = history.replace(" ", "")  # Remove spaces
    cooperation_count = moves.count("C")
    total_moves = len(moves)
    return cooperation_count / total_moves if total_moves > 0 else 0

# Step 5: Calculate actual cooperation rates
matchups_df["player1_actual_coop"] = matchups_df["history"].apply(lambda h: calculate_cooperation_rate(h))
matchups_df["player2_actual_coop"] = matchups_df["history"].apply(lambda h: calculate_cooperation_rate(h))

# Step 6: Calculate deviation from commitments
matchups_df["player1_deviation"] = abs(matchups_df["player1_actual_coop"] - matchups_df["player1_commitment"])
matchups_df["player2_deviation"] = abs(matchups_df["player2_actual_coop"] - matchups_df["player2_commitment"])

# Display the processed DataFrame
def display_results():
    print(matchups_df)

# Save the results for review
matchups_df.to_csv("commitment_analysis_results.csv", index=False)

# Step 7: Visualize results
# Plot Player 1 vs Player 2 commitment adherence
plt.figure(figsize=(10, 6))

# Scatter plot for Player 1
plt.scatter(matchups_df["player1_commitment"], matchups_df["player1_actual_coop"], label="Player 1", alpha=0.7)

# Scatter plot for Player 2
plt.scatter(matchups_df["player2_commitment"], matchups_df["player2_actual_coop"], label="Player 2", alpha=0.7)

# Add a line for perfect adherence
plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Perfect Adherence")

plt.title("Commitment vs Actual Cooperation")
plt.xlabel("Commitment")
plt.ylabel("Actual Cooperation")
plt.legend()
plt.grid(True)
plt.show()

# Step 8: Display deviations
plt.figure(figsize=(10, 6))

# Plot deviations for Player 1
plt.hist(matchups_df["player1_deviation"], bins=10, alpha=0.7, label="Player 1 Deviations")

# Plot deviations for Player 2
plt.hist(matchups_df["player2_deviation"], bins=10, alpha=0.7, label="Player 2 Deviations")

plt.title("Deviation from Commitments")
plt.xlabel("Deviation")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()

print("Analysis completed. Results saved to 'commitment_analysis_results.csv'.")
