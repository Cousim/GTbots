import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


db_config = {
    'host': 'localhost',          
    'user': 'root',              
    'password': '1234',           
    'database': 'gametheory'      
}


def calculate_average_budgets(players_df, start_id, end_id, interval_index):
    start_ids = range(start_id + (interval_index * 10), end_id, 80)
    average_budgets = []

    for start_id in start_ids:
        group_player_ids = range(start_id, start_id + 10)
        group_players = players_df[players_df['player_id'].isin(group_player_ids)]
        group_budgets = group_players['budget']
        
        avg_budget = group_budgets.mean()
        
        average_budgets.append((start_id, start_id + 9, avg_budget))

    return average_budgets


intervals = [
    (1, 881),
    (881, 1761),
    (1761, 2641),
    (2641, 3521),
    (3521, 4401),
    (4401, 5281),
    (5281, 6161),
    (6161, 7041)
]


colors_5h1 = ['darkblue', 'teal', 'darkorange', 'crimson', 'forestgreen', 'indigo', 'goldenrod','green']
colors_5h7 = ['mediumvioletred', 'dodgerblue', 'limegreen', 'darkviolet', 'tomato', 'slateblue', 'darkcyan','blue']


for idx, (start, end) in enumerate(intervals):
    
    conn = mysql.connector.connect(**db_config)

    query_h1 = f"""
    SELECT * 
    FROM PLAYERS 
    WHERE tournament_id LIKE '5h1%' AND player_id BETWEEN {start} AND {end}
    """
    players_h1_df = pd.read_sql(query_h1, conn)

    query_h7 = f"""
    SELECT * 
    FROM PLAYERS 
    WHERE tournament_id LIKE '5h7%' AND player_id BETWEEN {start} AND {end}
    """
    players_h7_df = pd.read_sql(query_h7, conn)

    conn.close()

    average_budgets_h1 = calculate_average_budgets(players_h1_df, start_id=start, end_id=end, interval_index=idx)
    average_budgets_h7 = calculate_average_budgets(players_h7_df, start_id=start, end_id=end, interval_index=idx)

    groups = [f"{start + (i + idx) * 80}-{start + (i + idx + 1) * 10}" for i in range(len(average_budgets_h1))]
    avg_budgets_h1 = [avg for _, _, avg in average_budgets_h1]
    avg_budgets_h7 = [avg for _, _, avg in average_budgets_h7]

    new_x_labels = [i * 10 for i in range(len(groups))]

    x = range(len(groups))

    plt.figure(figsize=(12, 6))
    bar_width = 0.35
    bars_h1 = plt.bar(x, avg_budgets_h1, width=bar_width, label="5h1 Tournaments", color=colors_5h1[idx], align='center')
    bars_h7 = plt.bar([i + bar_width for i in x], avg_budgets_h7, width=bar_width, label="5h7 Tournaments", color=colors_5h7[idx], align='center')

    plt.title(f'Average Budgets for Players in Tournaments ({start}-{end-1})')
    plt.xlabel('Player Groups')
    plt.ylabel('Average Budget')

    plt.xticks(x, new_x_labels, rotation=45)
    plt.legend()

    for bar in bars_h1:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{round(yval, 2)}', va='bottom', ha='center')

    for bar in bars_h7:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{round(yval, 2)}', va='bottom', ha='center')

    plt.tight_layout()
    plt.show()
