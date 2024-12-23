import sys

class AlwaysCooperate(): 
    def play(self, botHistory, botBudget, roundNum):
        print("Always Cooperate")
        return True

class GenerousTitForTat():
    def play(self, botHistory, botBudget, roundNum):
        print("Generous tit for tat")
        revenge = False
        if botHistory == [] or len(botHistory) < 4:
            return True
        else:
            if (botHistory[2*roundNum-1] == "D" and botHistory[2*roundNum-3] == "D"):
                revenge = True
                return False
            elif revenge:
                revenge = False
                return False
            else:
                return True

class Pavlov():
    def play(self, botHistory, botBudget, roundNum):
        print("Pavlov")
        if botHistory == []:
            return True
        if (botHistory[2*roundNum-2] == "C") and (botHistory[2*roundNum-1] == "D"):
            return False
        return True

def play_game(strategy_class):
    print("\nWelcome to the Prisoner's Dilemma Game!")
    print("Type 'C' for Cooperate or 'D' for Defect during your turn.")
    
    bot = strategy_class()
    bot_history = []
    bot_budget = 0  # Placeholder, as botBudget is not used here
    round_num = 0

    while True:
        print(f"\nRound {round_num}:")
        user_move = input("Your move (C/D): ").strip().upper()
        
        if user_move not in ['C', 'D']:
            print("Invalid move! Please type 'C' or 'D'.")
            continue
        
        # Bot decides its move
        bot_move = 'C' if bot.play(bot_history, bot_budget, round_num) else 'D'

        # Update history
        bot_history.extend([bot_move, user_move])

        print(f"Bot's move: {bot_move}")
        print(f"History so far: {bot_history}")

        round_num += 1
    	
        '''
        # Option to quit the game
        quit_game = input("Do you want to play another round? (Y/N): ").strip().upper()
        if quit_game == 'N':
            print("Thanks for playing!")
            break
        '''

if __name__ == "__main__":
    strategies = {
        "1": ("Always Cooperate", AlwaysCooperate),
        "2": ("Generous Tit for Tat", GenerousTitForTat),
        "3": ("Pavlov", Pavlov)
    }

    print("Choose a strategy to play against:")
    for key, (name, _) in strategies.items():
        print(f"{key}: {name}")

    choice = input("Enter the number of your choice: ").strip()

    if choice in strategies:
        _, strategy_class = strategies[choice]
        play_game(strategy_class)
    else:
        print("Invalid choice. Exiting.")
