import math
from bots.BilateralClosedDeterministic import BilateralClosedDeterministic
from game.BilateralClosedDeterministicGame import BilateralClosedDeterministicGame
from bots.BilateralClosedMixed import BilateralClosedMixed
from game.BilateralClosedMixedGame import BilateralClosedMixedGame
from bots.BilateralOCostDeterministic import BilateralOCostDeterministic
from game.BilateralOCostDeterministicGame import BilateralOCostDeterministicGame
from bots.BilateralOCostMixed import BilateralOCostMixed
from game.BilateralOCostMixedGame import BilateralOCostMixedGame
from bots.BilateralOpenMixed import BilateralOpenMixed
from game.BilateralOpenMixedGame import BilateralOpenMixedGame
from bots.BilateralOpenDeterministic import BilateralOpenDeterministic
from game.BilateralOpenDeterministicGame import BilateralOpenDeterministicGame
from bots.UnilateralClosedDeterministic import UnilateralClosedDeterministic
from game.UnilateralClosedDeterministicGame import UnilateralClosedDeterministicGame
from bots.UnilateralClosedMixed import UnilateralClosedMixed
from game.UnilateralClosedMixedGame import UnilateralClosedMixedGame
from bots.UnilateralOCostDeterministic import UnilateralOCostDeterministic
from game.UnilateralOCostDeterministicGame import UnilateralOCostDeterministicGame
from bots.UnilateralOCostMixed import UnilateralOCostMixed
from game.UnilateralOCostMixedGame import UnilateralOCostMixedGame
from bots.UnilateralOpenDeterministic import UnilateralOpenDeterministic
from game.UnilateralOpenDeterministicGame import UnilateralOpenDeterministicGame
from bots.UnilateralOpenMixed import UnilateralOpenMixed
from game.UnilateralOpenMixedGame import UnilateralOpenMixedGame

from strategies.TitForTat import TitForTat
from strategies.TitForTwoTats import TitForTwoTats
from strategies.Pavlov import Pavlov
from strategies.GrimTrigger import GrimTrigger
from strategies.AlwaysDefect import AlwaysDefect

# Define strategies
titForTat = TitForTat()
titForTwoTats = TitForTwoTats() 
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect() 

machine_identifier = "ktg"
tournament_count = 0


playerTypes0 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,False, False]]
playerProbs0 = [0.25,0.25,0.25,0.25]

playerTypes1 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 50, 100, 0, 2],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 0, 100, 0, 3],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, 4]]
playerProbs1 = [0.25,0.25,0.25,0.25]

playerTypes2 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,False, False]]
playerProbs2 = [0.25,0.25,0.25,0.25]

playerTypes3 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0]]
playerProbs3 = [0.25,0.25,0.25,0.25]

playerTypes4 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, 1]]
playerProbs4 = [0.25,0.25,0.25,0.25]

playerTypes5 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, False, False]]
playerProbs5 = [0.25,0.25,0.25,0.25]


playerTypes6 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, False, False]]
playerProbs6 = [0.25,0.25,0.25,0.25]


playerTypes7 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 0]]
playerProbs7 = [0.25,0.25,0.25,0.25]

#8
playerTypes8 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, True, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, True, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, True, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, True, False]]
playerProbs8 = [0.25,0.25,0.25,0.25]


playerTypes9 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1]]
playerProbs9 = [0.25,0.25,0.25,0.25]


playerTypes10 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, True, True],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, True, True],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, True, True],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, True, True]]
playerProbs10 = [0.25,0.25,0.25,0.25]


playerTypes11 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0]]
playerProbs11 = [0.25,0.25,0.25,0.25]


#For unilateral games everyone should play each other twice with different commit

def stringToDict(payoffStr):
    payoffDict = {"CC": int(payoffStr[2]), "DC": int(payoffStr[5]), "CD": int(payoffStr[8]), "DD": int(payoffStr[11])}
    return payoffDict

def tournament(gameType, gameLength, playerCount, playerTypes, playerProbs, payoffs, punishment, reward):
    bots = []
    #ADD TO DB: tourn_id gametype gamelength playercount payoff punishment reward
    bot1PayoffMatrix = stringToDict(payoffs)
    bot2PayoffMatrix = stringToDict(payoffs)
    if gameType == 0:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot = BilateralClosedDeterministic( 
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                assumeCommitProb=playerTypes[i][6], 
                commitType=playerTypes[i][7], 
                opponentCoopCommitType=playerTypes[i][8])
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    BilateralClosedDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=+1, 
                    punishment=punishment).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1
        
    elif gameType == 1:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot = BilateralClosedMixed(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5],  
                assumeCommitProb=playerTypes[i][6], 
                opponentCommitProb=playerTypes[i][7], 
                seed=playerTypes[i][8]  # Default seed value
                )
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    BilateralClosedMixedGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment
                    ).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 2:

        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot = BilateralOCostDeterministic(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3],  
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                assumeCommitProb=playerTypes[i][6],  
                payProb=playerTypes[i][7], 
                commitType=playerTypes[i][8],  # Default value for commitType
                opponentCoopCommitType=playerTypes[i][9]  # Default value for opponentCoopCommitType
            )
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    BilateralOCostDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment, 
                    observation_cost=3  # Add observation cost parameter
                    ).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1
                 
    elif gameType == 3:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot =BilateralOCostMixed(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3], playerTypes[i][4], 
                playerTypes[i][5], 
                playerTypes[i][6],  
                playerTypes[i][7], 
                playerTypes[i][8], 
                playerTypes[i][9])
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    BilateralOCostMixedGame(bots[i], bots[n], bot1PayoffMatrix, bot2PayoffMatrix, gameLength, reward, punishment, 3).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 4:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot =BilateralOpenMixed(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                opponentCoopCommitProb=playerTypes[i][6], 
                seed=playerTypes[i][7]  # Default seed value
                )
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    BilateralOpenMixedGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1
    
    elif gameType == 5:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot =BilateralOpenDeterministic(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3],
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5],  
                commitType=playerTypes[i][6], 
                opponentCoopCommitType=playerTypes[i][7])  
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    BilateralOpenDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment
                    ).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 6:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot =UnilateralClosedDeterministic(
                mostCoopStrat=playerTypes[i][0], 
                lessCoopStrat=playerTypes[i][1], 
                lessDefectStrat=playerTypes[i][2], 
                mostDefectStrat=playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                assumeCommitProb=playerTypes[i][6], 
                commitType=playerTypes[i][7],  # Default value for commitType
                opponentCoopCommitType=playerTypes[i][8]  # Default value for opponentCoopCommitType
                ) 
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    UnilateralClosedDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment
                    ).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1
    
    elif gameType == 7:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot =UnilateralClosedMixed(
                mostCoopStrat=playerTypes[i][0], 
                lessCoopStrat=playerTypes[i][1],  
                lessDefectStrat=playerTypes[i][2], 
                mostDefectStrat=playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                assumeOpponentCommitProb=playerTypes[i][6], 
                opponentCoopCommitProb=playerTypes[i][7], 
                seed=playerTypes[i][8] 
                )   
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    UnilateralClosedMixedGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment
                    ).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 8:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot =UnilateralOCostDeterministic(
                mostCoopStrat=playerTypes[i][0], 
                lessCoopStrat=playerTypes[i][1], 
                lessDefectStrat=playerTypes[i][2], 
                mostDefectStrat=playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                assumeCommitProb=playerTypes[i][6], 
                payProb=playerTypes[i][7], 
                commitType=playerTypes[i][8],  # Example value for commitType
                opponentCoopCommitType=playerTypes[i][9]  # Example value for opponentCoopCommitType
                )
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    UnilateralOCostDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment, 
                    observation_cost=3  # Example value for observation_cost
                    ).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 9:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot = UnilateralOCostMixed(
                mostCoopStrat=playerTypes[i][0], 
                lessCoopStrat=playerTypes[i][1], 
                lessDefectStrat=playerTypes[i][2], 
                mostDefectStrat=playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5],
                payProb=playerTypes[i][6], 
                opponentCoopCommitProb=playerTypes[i][7],
                assumeOppCommitProb = playerTypes[i][8],
                seed=playerTypes[i][9]  # Default seed value
                )
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    UnilateralOCostMixedGame(
                    bot1=bots[i], 
                    bot2=bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment, 
                    observation_cost=3).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 10:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot = UnilateralOpenDeterministic(
                mostCoopStrat=playerTypes[i][0], 
                lessCoopStrat=playerTypes[i][1], 
                lessDefectStrat=playerTypes[i][2], 
                mostDefectStrat=playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                commitType=playerTypes[i][6],  # True as a default value, can change
                opponentCoopCommitType=playerTypes[i][7]  # True as a default value, can change
                )
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    UnilateralOpenDeterministicGame(
                    bot1=bots[i], 
                    bot2=bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment).gametime()  # Example values for commitment and punishment

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 11:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerProbs[i]))):      
                bot = UnilateralOpenMixed(
                mostCoopStrat=playerTypes[i][0], 
                lessCoopStrat=playerTypes[i][1], 
                lessDefectStrat=playerTypes[i][2], 
                mostDefectStrat=playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                opponentCoopCommitProb=playerTypes[i][6],
                seed=playerTypes[i][7]  # Default seed value
                )
                bots.append(bot)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    UnilateralOpenMixedGame(
                    bot1=bots[i], 
                    bot2=bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment,
                    ).gametime()
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1


# not used right now, will be used in nested for loops
#insert_tournaments = (
#    "INSERT INTO TOURNAMENTS "
#    "(tournament_id, game_type, game_length, payoffs, punishment, reward) "
#    "VALUES (%s, %s, %s, %s, %s, %s)"
#)

#tournament(0,7,4,playerTypes0, playerProbs0, "CC3DC5CD0DD1", -1, 1)
#tournament(1,7,4,playerTypes1, playerProbs1, "CC3DC5CD0DD1", -1, 1)
#tournament(2,7,4,playerTypes2, playerProbs2, "CC3DC5CD0DD1", -1, 1)
#tournament(3,7,4,playerTypes3, playerProbs3, "CC3DC5CD0DD1", -1, 1)
#tournament(4,7,4,playerTypes4, playerProbs4, "CC3DC5CD0DD1", -1, 1)
#tournament(5,7,4,playerTypes5, playerProbs5, "CC3DC5CD0DD1", -1, 1)
tournament(6,7,4,playerTypes6, playerProbs6, "CC3DC5CD0DD1", -1, 1)
tournament(7,7,4,playerTypes7, playerProbs7, "CC3DC5CD0DD1", -1, 1)
tournament(8,7,4,playerTypes8, playerProbs8, "CC3DC5CD0DD1", -1, 1)
tournament(9,7,4,playerTypes9, playerProbs9, "CC3DC5CD0DD1", -1, 1)
tournament(10,7,4,playerTypes10, playerProbs10, "CC3DC5CD0DD1", -1, 1)
tournament(11,7,4,playerTypes11, playerProbs11, "CC3DC5CD0DD1", -1, 1)