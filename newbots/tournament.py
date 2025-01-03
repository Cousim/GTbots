import mysql.connector
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import csv

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

from database import queries

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234", 
  auth_plugin='mysql_native_password'
)

# creating database_cursor to perform SQL operation to run queries
db_cursor = db_connection.cursor(buffered=True)

db_cursor.execute("USE gametheory")

# Define strategies
titForTat = TitForTat()
titForTwoTats = TitForTwoTats() 
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect() 

machine_identifier = "ktg"
                #BilateralClosedDeterministic strategies, budget, coopCommitProb, assumeCommitProb, commitType, opponentCommitType
playerTypes0 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,False, False]]
playerWeights0 = [0.25,0.25,0.25,0.25]
                #BilateralClosedMixed strategies, budget, coopCommitProb, assumeCommitProb, opponentCommitProb, seed
playerTypes1 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 50, 100, 0, 2],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 0, 100, 0, 3],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, 4]]
playerWeights1 = [0.25,0.25,0.25,0.25]
                #BilateralOCostDeterministic strategies, budget, coopCommitProb, assumeCommitProb, payProb, commitType, opponentCoopCommitType
playerTypes2 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,False, False]]
playerWeights2 = [0.25,0.25,0.25,0.25]
                #BilateralOCostMixed strategies, budget, coopCommitProb, assumeCommitProb, payProb, opponentCoopCommitProb, seed
playerTypes3 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100,100,0,0, 0]]
playerWeights3 = [0.25,0.25,0.25,0.25]

                #BilateralOpenDeterministic, strategies, budget, coopCommitProb, commitType, opponentCoopCommitType
playerTypes4 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, False, False]]
playerWeights4 = [0.25,0.25,0.25,0.25]
                #BilateralOpenMixed, budget, coopCommitProb, opponentCoopCommitProb, seed
playerTypes5 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0]]
playerWeights5 = [0.25,0.25,0.25,0.25]


                #UnilateralClosedDeterministic, strategies, budget, coopCommitProb, assumeCommitProb, commitType, opponentCoopCommitType
playerTypes6 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, False, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, False, False]]
playerWeights6 = [0.25,0.25,0.25,0.25]

                #UnilateralClosedMixed, strategies, budget, coopCommitProb, assumeOpponentCommitProb, opponentCoopCommitProb, seed
playerTypes7 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 0],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 0]]
playerWeights7 = [0.25,0.25,0.25,0.25]

                #UnilateralOCostDeterministic, strategies, budget, coopCommitProb, assumeCommitProb, payProb, commitType, opponentCoopCommitType
playerTypes8 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, True, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, True, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, True, False],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0, True, False]]
playerWeights8 = [0.25,0.25,0.25,0.25]

                #UnilateralOCostMixed, budget, coopCommitProb, assumeOppCommitProb, payProb, opponentCoopCommitProb, seed
playerTypes9 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1],
               [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 100, 100, 1]]
playerWeights9 = [0.25,0.25,0.25,0.25]

                #UnilateralOpenDeterministic, budget, coopCommitProb, commitType, opponentCoopCommitType
playerTypes10 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, True, True],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, True, True],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, True, True],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, True, True]]
playerWeights10 = [0.25,0.25,0.25,0.25]

                #UnilateralOpenMixed, budget, coopCommitProb, opponentCoopCommitProb, seed
playerTypes11 = [[titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0],
                [titForTwoTats, titForTat, pavlov, grimTrigger, 0, 100, 100, 0]]
playerWeights11 = [0.25,0.25,0.25,0.25]

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#For unilateral games everyone should play each other twice with different commit
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def stringToDict(payoffStr):
    payoffDict = {"CC": int(payoffStr[2]), "DC": int(payoffStr[5]), "CD": int(payoffStr[8]), "DD": int(payoffStr[11])}
    return payoffDict

def tournament(gameType, gameLength, playerCount, playerTypes, playerWeights, payoffs, punishment, reward):
    db_cursor.execute("""SELECT COUNT(*) FROM TOURNAMENTS""")
    tourCount = db_cursor.fetchone()[0]
    db_cursor.fetchall()

    if tourCount == None:
        tourCount = 0

    tournamentID = machine_identifier + str(tourCount)
    db_cursor.execute(queries.insertTournament, (tournamentID, gameType, gameLength, payoffs, punishment, reward))

    bots = []

    bot1PayoffMatrix = stringToDict(payoffs)
    bot2PayoffMatrix = stringToDict(payoffs)
    if gameType == 0:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
                bot = BilateralClosedDeterministic( 
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                assumeCommitProb=playerTypes[i][6], 
                commitType=playerTypes[i][7], 
                opponentCoopCommitType=playerTypes[i][8])
                bots.append(bot)

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), playerTypes[i][1].stratInt(), playerTypes[i][2].stratInt(), playerTypes[i][3].stratInt(), 
                        playerTypes[i][5], playerTypes[i][6], None, 0, 0, 0, bot.getBudget()) #pay_prob None cunku closed game
                db_cursor.execute(queries.insertPlayer, val2)
          
        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = BilateralClosedDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=+1, 
                    punishment=punishment).gametime()

                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], matchupInfo[1][0], matchupInfo[1][1], matchupInfo[0][1][0], matchupInfo[0][1][1], None, None, None, None)
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall

                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])

                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
 
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1
        
    elif gameType == 1:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
                bot = BilateralClosedMixed(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5],  
                assumeCommitProb=playerTypes[i][6], 
                opponentCommitProb=playerTypes[i][7], 
                seed=playerTypes[i][8]  # Default seed value
                )
                bots.append(bot)

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), None, None, None, 
                        playerTypes[i][5], playerTypes[i][6], None, 0, 0, 0, bot.getBudget()) # pay_prob None cunku closed game, 3 strateji None cunku mixed botlar tek strateji uyguluyor (su anki haliyle)
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = BilateralClosedMixedGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment
                    ).gametime()

                                                  # divide w/ 100 to show prob in range [0,1]
                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], (matchupInfo[1][0] / 100), (matchupInfo[1][1] / 100), 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, None, matchupInfo[2][0], matchupInfo[2][1])
                
                    db_cursor.execute(queries.insertMatchup, val3)
                    
                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall

                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])

                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))

                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 2:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
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

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), playerTypes[i][1].stratInt(), playerTypes[i][2].stratInt(), playerTypes[i][3].stratInt(), 
                        playerTypes[i][5], playerTypes[i][6], playerTypes[i][7], 0, 0, 0, bot.getBudget())
                db_cursor.execute(queries.insertPlayer, val2)                

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = BilateralOCostDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment, 
                    observation_cost=3  # Add observation cost parameter
                    ).gametime()

                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], matchupInfo[1][0], matchupInfo[1][1], 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], matchupInfo[2][0], matchupInfo[2][1], None , None)               
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall

                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])

                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))
                    
                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1
                 
    elif gameType == 3:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
                bot =BilateralOCostMixed(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3], playerTypes[i][4], 
                playerTypes[i][5], 
                playerTypes[i][6],  
                playerTypes[i][7], 
                playerTypes[i][8], 
                playerTypes[i][9])
                bots.append(bot)

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), None, None, None, 
                        playerTypes[i][5], playerTypes[i][6], playerTypes[i][7], 0, 0, 0, bot.getBudget()) # 3 strateji None cunku mixed botlar tek strateji uyguluyor (su anki haliyle)
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = BilateralOCostMixedGame(bots[i], bots[n], bot1PayoffMatrix, bot2PayoffMatrix, gameLength, reward, punishment, 3).gametime()

                    # divide w/ 100 to show prob in range [0,1]
                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], (matchupInfo[1][0] / 100), (matchupInfo[1][1] / 100), 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], matchupInfo[2][0], matchupInfo[2][1], matchupInfo[3][0], matchupInfo[3][1])
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall

                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])

                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 4:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
                bot =BilateralOpenDeterministic(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3],
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5],  
                commitType=playerTypes[i][6], 
                opponentCoopCommitType=playerTypes[i][7])  
                bots.append(bot)

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), playerTypes[i][1].stratInt(), playerTypes[i][2].stratInt(), playerTypes[i][3].stratInt(), 
                        playerTypes[i][5], None, None, 0, 0, 0, bot.getBudget()) # assume_commit_prob, pay_prob None cunku open game
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = BilateralOpenDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment
                    ).gametime()

                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], matchupInfo[1][0], matchupInfo[1][1], 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, None, None, None)
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall

                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])

                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    #SEED part is here !!!!!!!!

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1
    
    elif gameType == 5:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
                bot =BilateralOpenMixed(
                playerTypes[i][0], playerTypes[i][1], playerTypes[i][2], playerTypes[i][3], 
                budget=playerTypes[i][4], 
                coopCommitProb=playerTypes[i][5], 
                opponentCoopCommitProb=playerTypes[i][6], 
                seed=playerTypes[i][7]  # Default seed value
                )
                bots.append(bot)

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), None, None, None, 
                        playerTypes[i][5], None, None, 0, 0, 0, bot.getBudget()) # assume_commit_prob, pay_prob None cunku open game, 3 strateji None cunku mixed botlar tek strateji uyguluyor (su anki haliyle)
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i < n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = BilateralOpenMixedGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix, 
                    bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment).gametime()

                    # divide w/ 100 to show prob in range [0,1]
                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], (matchupInfo[1][0] / 100), (matchupInfo[1][1] / 100), 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, None, matchupInfo[2][0], matchupInfo[2][1])
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall

                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])

                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    elif gameType == 6:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
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

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), playerTypes[i][1].stratInt(), playerTypes[i][2].stratInt(), playerTypes[i][3].stratInt(), 
                        playerTypes[i][5], playerTypes[i][6], None, 0, 0, 0, bot.getBudget()) # pay_prob None cunku closed game
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i != n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = UnilateralClosedDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment
                    ).gametime()

                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], matchupInfo[1], None, 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, None, None, None)
                    db_cursor.execute(queries.insertMatchup, val3)    

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall

                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])

                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))                
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1

    
    elif gameType == 7:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
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

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), None, None, None, 
                        playerTypes[i][5], playerTypes[i][6], None, 0, 0, 0, bot.getBudget()) # pay_prob None cunku closed game, 3 strateji None cunku mixed botlar tek strateji uyguluyor (su anki haliyle)
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i != n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = UnilateralClosedMixedGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment
                    ).gametime()

                    # divide w/ 100 to show prob in range [0,1]
                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], (matchupInfo[1] / 100), None, 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, None, matchupInfo[2], None)
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]
#
                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]
#
                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall
#
                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])
#
                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1


    elif gameType == 8:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
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

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), playerTypes[i][1].stratInt(), playerTypes[i][2].stratInt(), playerTypes[i][3].stratInt(), 
                        playerTypes[i][5], playerTypes[i][6], playerTypes[i][7], 0, 0, 0, bot.getBudget())
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i != n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = UnilateralOCostDeterministicGame(
                    bots[i], 
                    bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment, 
                    observation_cost=3  # Example value for observation_cost
                    ).gametime()

                                        # since deterministic, no division
                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], matchupInfo[1], None, 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, matchupInfo[2], None, None)
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]
#
                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]
#
                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall
#
                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])
#
                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1


    elif gameType == 9:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
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
                
                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), None, None, None, 
                        playerTypes[i][5], playerTypes[i][6], playerTypes[i][7], 0, 0, 0, bot.getBudget()) #3 strateji None cunku mixed botlar tek strateji uyguluyor (su anki haliyle)
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i != n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = UnilateralOCostMixedGame(
                    bot1=bots[i], 
                    bot2=bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment, 
                    observation_cost=3).gametime()

                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], (matchupInfo[1] / 100), None, 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, matchupInfo[2], matchupInfo[3], None)
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]

                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall

                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])
#
                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1


    elif gameType == 10:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
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

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), playerTypes[i][1].stratInt(), playerTypes[i][2].stratInt(), playerTypes[i][3].stratInt(), 
                        playerTypes[i][5], None, None, 0, 0, 0, bot.getBudget()) # assume_commit_prob, pay_prob None cunku open game
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i != n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = UnilateralOpenDeterministicGame(
                    bot1=bots[i], 
                    bot2=bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment).gametime()  # Example values for commitment and punishment
                    
                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], matchupInfo[1], None, 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, None, None, None)
                    db_cursor.execute(queries.insertMatchup, val3)
                    
                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]
#
                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]
#
                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall
#
                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])
#
                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))

                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1


    elif gameType == 11:
        count = 0
        for i in range(len(playerTypes)):
            for n in range((math.floor(playerCount*playerWeights[i]))):      
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

                val2 = (bot.getID(), tournamentID, playerTypes[i][0].stratInt(), None, None, None, 
                        playerTypes[i][5], None, None, 0, 0, 0, bot.getBudget()) # assume_commit_prob, pay_prob None cunku open game, 3 strateji None cunku mixed botlar tek strateji uyguluyor (su anki haliyle)
                db_cursor.execute(queries.insertPlayer, val2)

        for i in range(playerCount):
            for n in range(playerCount):
                if i != n:
                    print("Game",count,"****************************************************************************************")
                    matchupInfo = UnilateralOpenMixedGame(
                    bot1=bots[i], 
                    bot2=bots[n], 
                    bot1PayoffMatrix=bot1PayoffMatrix, 
                    bot2PayoffMatrix=bot2PayoffMatrix, 
                    game_length=gameLength, 
                    commitment=reward, 
                    punishment=punishment,
                    ).gametime()
                    
                                                                                            #divide w/ 100 to show prob in [0, 1]
                    val3 = (tournamentID, bots[i].getID(), bots[n].getID(), matchupInfo[0][0], (matchupInfo[1] / 100), None, 
                            matchupInfo[0][1][0], matchupInfo[0][1][1], None, None, matchupInfo[2], None)
                    db_cursor.execute(queries.insertMatchup, val3)

                    for bot_idx in (i, n):
                        db_cursor.execute(queries.getWins, (bots[bot_idx].getID(), tournamentID))
                        oldWins = db_cursor.fetchone()[0]
#
                        db_cursor.execute(queries.getDraws, (bots[bot_idx].getID(), tournamentID))
                        oldDraws = db_cursor.fetchone()[0]
#
                        db_cursor.execute(queries.getLosses, (bots[bot_idx].getID(), tournamentID))
                        oldLosses = db_cursor.fetchone()[0]
                        db_cursor.fetchall
#
                        if bot_idx == i:
                            newWins = oldWins + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                        else:
                            newWins = oldWins + (matchupInfo[0][1][0] < matchupInfo[0][1][1])
                            newLosses = oldLosses + (matchupInfo[0][1][0] > matchupInfo[0][1][1])
                        newDraws = oldDraws + (matchupInfo[0][1][0] == matchupInfo[0][1][1])
#
                        db_cursor.execute(queries.updateWins, (newWins, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateLosses, (newLosses, bots[bot_idx].getID(), tournamentID))
                        db_cursor.execute(queries.updateDraws, (newDraws, bots[bot_idx].getID(), tournamentID))
                    
                    db_cursor.execute(queries.updateBudget, (bots[i].getBudget(), bots[i].getID(), tournamentID))
                    db_cursor.execute(queries.updateBudget, (bots[n].getBudget(), bots[n].getID(), tournamentID))

                    bot1PayoffMatrix = stringToDict(payoffs)
                    bot2PayoffMatrix = stringToDict(payoffs)
                    count += 1


    db_connection.commit()



# not used right now, will be used in nested for loops
#insert_tournaments = (
#    "INSERT INTO TOURNAMENTS "
#    "(tournament_id, game_type, game_length, payoffs, punishment, reward) "
#    "VALUES (%s, %s, %s, %s, %s, %s)"
#)

#tournament(0,7,4,playerTypes0, playerWeights0, "CC3DC6CD0DD1", -1, 0)
#tournament(1,7,4,playerTypes1, playerWeights1, "CC3DC5CD0DD1", -1, 0)
#tournament(2,7,4,playerTypes2, playerWeights2, "CC3DC5CD0DD1", -1, 0)
#tournament(3,7,4,playerTypes3, playerWeights3, "CC3DC5CD0DD1", -1, 0)
#tournament(4,7,4,playerTypes4, playerWeights4, "CC3DC5CD0DD1", -1, 0)
#tournament(5,7,4,playerTypes5, playerWeights5, "CC3DC5CD0DD1", -1, 0)
#tournament(6,7,4,playerTypes6, playerWeights6, "CC3DC5CD0DD1", -1, 0)
#tournament(7,7,4,playerTypes7, playerWeights7, "CC3DC5CD0DD1", -1, 0)
#tournament(8,7,4,playerTypes8, playerWeights8, "CC3DC5CD0DD1", -1, 0)
#tournament(9,7,4,playerTypes9, playerWeights9, "CC3DC5CD0DD1", -1, 0)
#tournament(10,7,4,playerTypes10, playerWeights10, "CC3DC5CD0DD1", -1, 0)
#tournament(11,7,4,playerTypes11, playerWeights11, "CC3DC5CD0DD1", -1, 0)