import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import permutations

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="gametheory"
)
cursor = connection.cursor()

# Retrieve relevant player data from the PLAYERS table
cursor.execute(
    """
    SELECT tournament_id, player_id, budget
    FROM PLAYERS
    WHERE tournament_id LIKE '4h%'
    """
)
players_data = cursor.fetchall()

# Create a dictionary to store rankings for each permutation and player type
rankings = {str(i): {"".join(p): [] for p in permutations("1234")} for i in range(8)}

# Process each player's data
for player in players_data:
    tournament_id = player[0]
    player_id = player[1]
    budget = player[2]

    # Extract player_type, game_type, and permutation from tournament_id
    try:
        tournament_parts = tournament_id.split(", ")
        game_type = int(tournament_parts[0].split(": ")[0][2])  # Extract game type (0, 2, 4)
        player_type = int(tournament_parts[0].split(": ")[1])  # Extract player type (e.g., "0")
        permutation = tournament_parts[1].strip()  # Extract permutation (e.g., "1234")

        # Store budget in the corresponding permutation
        if permutation in rankings[str(player_type)]:
            rankings[str(player_type)][permutation].append((game_type, budget))
    except (IndexError, ValueError) as e:
        print(f"Error parsing tournament_id '{tournament_id}': {e}")
        continue

# Calculate average ranking for each permutation and player type
average_rankings = {str(i): {} for i in range(8)}

for player_type, perms in rankings.items():
    for perm, data in perms.items():
        if data:  # Ensure there is data to process
            total_rankings = []

            # Separate data by game type and calculate rankings for each game type
            for game_type in [0, 2, 4]:
                game_data = [budget for g_type, budget in data if g_type == game_type]

                if game_data:
                    # Sort budgets in descending order to calculate rankings
                    sorted_budgets = sorted(game_data, reverse=True)
                    rankings_list = [sorted_budgets.index(budget) + 1 for budget in game_data]

                    # Collect rankings for this game type
                    total_rankings.extend(rankings_list)

            # Calculate the average ranking across all game types
            if total_rankings:
                average_rankings[player_type][perm] = np.mean(total_rankings)
            else:
                average_rankings[player_type][perm] = 0
        else:
            average_rankings[player_type][perm] = 0  # Default to 0 if no data

# Plot the results for each player type
for player_type, perms in average_rankings.items():
    perms_sorted = sorted(perms.keys())  # Ensure permutations are sorted
    avg_ranks = [perms[perm] for perm in perms_sorted]

    plt.figure(figsize=(12, 6))
    bars = plt.bar(perms_sorted, avg_ranks, color='skyblue')
    plt.xlabel('Permutations')
    plt.ylabel('Average Ranking (Lower is Better)')
    plt.title(f'Average Ranking for Player Type {player_type}')
    plt.xticks(rotation=90)

    # Add exact average ranking on top of each bar
    for bar, avg_rank in zip(bars, avg_ranks):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f'{avg_rank:.2f}', 
                 ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()

# Close the database connection
cursor.close()
connection.close()