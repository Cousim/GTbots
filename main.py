from bots import *

game_lenth = 5

AC = AlwaysCooperate(100)
AD = AlwaysDefect(100)
T4T = TitForTat(100)
T42T = TitForTwoTats(100)
PB = Pavlov(100)
GT = GrimTrigger(100)
RB = Randomized(100, 0.5)

players = [PB , RB]
players[0].setP1(True)

results = {"CC": (3,3),"DC":(5,0),"CD":(0,5),"DD":(1,1)}
payoff1 = None
payoff2 = None

for i in range(game_lenth):
    outcome = players[0].nextMove() + players[1].nextMove()
    print(outcome)
    (payoff1 , payoff2) = results.get(outcome)
    
    players[0].addHistory(outcome)
    players[1].addHistory(outcome[::-1])

    players[0].addPayoff(payoff1)
    players[1].addPayoff(payoff2)