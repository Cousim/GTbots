def calculate_cooperativeness(bot):
    """
    Calculates the cooperativeness of a bot based on its history.
    Cooperativeness is the ratio of cooperative moves ('C') to total moves.
    """
    history = bot.getHistory()
    cooperative_moves = sum(1 for move in history if move[0] == 'C')
    total_moves = len(history)
    return cooperative_moves / total_moves if total_moves > 0 else 0

def simulate_games(bots, game_length, results):
    """
    Simulates games between all pairs of bots and ranks them by cooperativeness.
    """
    cooperativeness_scores = {}

    for bot1 in bots:
        cooperativeness_scores[bot1.__class__.__name__] = 0
        for bot2 in bots:
            if bot1 == bot2:
                continue

            # Reset histories and budgets for each pair of bots
            bot1.history = []
            bot2.history = []
            bot1.budget = 100
            bot2.budget = 100

            # Simulate the game
            for _ in range(game_length):
                outcome = bot1.nextMove() + bot2.nextMove()
                (payoff1, payoff2) = results.get(outcome)

                bot1.addHistory(outcome)
                bot2.addHistory(outcome[::-1])

                bot1.addPayoff(payoff1)
                bot2.addPayoff(payoff2)

        # Calculate cooperativeness after playing with all other bots
        cooperativeness_scores[bot1.__class__.__name__] = calculate_cooperativeness(bot1)

    # Sort strategies by cooperativeness
    ranked_bots = sorted(cooperativeness_scores.items(), key=lambda x: x[1], reverse=True)
    return ranked_bots

if __name__ == "__main__":
    # Define results matrix for payoffs
    results = {"CC": (3, 3), "DC": (5, 0), "CD": (0, 5), "DD": (1, 1)}

    # Define bots
    bots = [
        AlwaysCooperate(100),
        AlwaysDefect(100),
        TitForTat(100),
        TitForTwoTats(100),
        Pavlov(100),
        GrimTrigger(100),
        Randomized(100, 0.5)
    ]

    # Set game parameters
    game_length = 5

    # Simulate games and rank bots by cooperativeness
    ranked_bots = simulate_games(bots, game_length, results)

    # Print results
    print("Ranking of Bot Strategies by Cooperativeness:")
    for rank, (bot_name, score) in enumerate(ranked_bots, 1):
        print(f"{rank}. {bot_name}: Cooperativeness = {score:.2f}")