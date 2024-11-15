from bots import *

results = {"CC": (3,3),"DC":(5,0),"CD":(0,5),"DD":(1,1)}

def game(bot1, bot2, results, game_length, commitment, punishment, observation_cost):
    bot1.rules(results, game_length, commitment, punishment, observation_cost, True)
    bot2.rules(results, game_length, commitment, punishment, observation_cost, False)

    if commitment == 1:
        c1 = bot1.getCommitment()
    elif commitment == 2:
        c1 = bot1.getCommitment()
        c2 = bot2.getCommitment()

    for key in results.keys():
        if c1 and (key[0] != c1):
            res = results.get(key)
            results.update({key : (res[0]-punishment, res[1])})
    
        if c2 and (key[1] != c2):
            res = results.get(key)
            results.update({key: (res[0], res[1]-punishment)})

    payoff1 = None
    payoff2 = None

    for i in range(game_length):
        outcome = bot1.nextMove() + bot2.nextMove()
        print(outcome)
        (payoff1 , payoff2) = results.get(outcome)
    
        bot1.addHistory(outcome)
        bot2.addHistory(outcome[::-1])

        bot1.addPayoff(payoff1)
        bot2.addPayoff(payoff2)