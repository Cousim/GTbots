from Interfaces import BilateralGame, OpenGame, DeterministicGame
import Game

import bots

class BilateralOpenDeterministicGame(Game, BilateralGame, OpenGame, DeterministicGame):
    def __init__(self, bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment):
        Game.__init__(bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment)
    
    def takeBilateralCommitment(self):
        bot1Commitment = self.bot1.makeCommitment()
        bot2Commitment = self.bot2.makeCommitment()

        if (bot1Commitment) :
            self.bot1PayoffMatrix.update({"CC": self.bot1PayoffMatrix.get("CC") + self.commitment})
            self.bot1PayoffMatrix.update({"CD": self.bot1PayoffMatrix.get("CD") + self.commitment})
            self.bot1PayoffMatrix.update({"DC": self.bot1PayoffMatrix.get("DC") + self.punishment})
            self.bot1PayoffMatrix.update({"DD": self.bot1PayoffMatrix.get("DD") + self.punishment})
        else : 
            self.bot1PayoffMatrix.update({"CC": self.bot1PayoffMatrix.get("CC") + self.punishment})
            self.bot1PayoffMatrix.update({"CD": self.bot1PayoffMatrix.get("CD") + self.punishment})
            self.bot1PayoffMatrix.update({"DC": self.bot1PayoffMatrix.get("DC") + self.commitment})
            self.bot1PayoffMatrix.update({"DD": self.bot1PayoffMatrix.get("DD") + self.commitment})

        if (bot2Commitment) :
            self.bot1PayoffMatrix.update({"CC": self.bot1PayoffMatrix.get("CC") + self.commitment})
            self.bot1PayoffMatrix.update({"CD": self.bot1PayoffMatrix.get("CD") + self.commitment})
            self.bot1PayoffMatrix.update({"DC": self.bot1PayoffMatrix.get("DC") + self.punishment})
            self.bot1PayoffMatrix.update({"DD": self.bot1PayoffMatrix.get("DD") + self.punishment})
        else : 
            self.bot1PayoffMatrix.update({"CC": self.bot1PayoffMatrix.get("CC") + self.punishment})
            self.bot1PayoffMatrix.update({"CD": self.bot1PayoffMatrix.get("CD") + self.punishment})
            self.bot1PayoffMatrix.update({"DC": self.bot1PayoffMatrix.get("DC") + self.commitment})
            self.bot1PayoffMatrix.update({"DD": self.bot1PayoffMatrix.get("DD") + self.commitment})

    
    def setOpponentCommitment(self):
        self.bot1.opponentCommitType = self.bot2.opponentCommitType
        self.bot2.opponentCommitType = self.bot1.opponentCommitType


    def rounds(self):
        for i in range(self.game_length):
            bot1Move = self.bot1.inTurn()
            bot2Move = self.bot2.inTurn()

            self.bot1.history.append(bot1Move) #adds self move in the even indexes starting w/ 0
            self.bot1.history.append(bot2Move)

            self.bot2.history.append(bot2Move)
            self.bot2.history.append(bot1Move)


            self.checkCommitmentAndPayoff(self, i)

        self.bot1.history = []
        self.bot2.history = []


    def checkCommitmentAndPayoff(self, roundNum):
        self.bot1.budget += self.bot1PayoffMatrix.get(self.bot1.history[2*roundNum]+self.bot1.history[1+2*roundNum])
        self.bot2.budget += self.bot2PayoffMatrix.get(self.bot2.history[2*roundNum]+self.bot2.history[1+2*roundNum])

    def gametime(self):
        self.takeBilateralCommitment()
        self.setOpponentCommitment()
        self.rounds()