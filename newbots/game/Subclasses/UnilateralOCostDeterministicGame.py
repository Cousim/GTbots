from Interfaces import UnilateralGame, OCostGame, DeterministicGame
import Game
import random

import bots

class UnilateralOCostDeterministicGame(Game, UnilateralGame, OCostGame, DeterministicGame):
    def __init__(self, bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment, observation_cost):
        Game.__init__(bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment)
        OCostGame.__init__(observation_cost)
    
    def takeUnilateralCommitment(self):
        if (random.randRange(1, 101)<51) :
            self.bot1.makeCommitment = True
        else :
            self.bot2.makeCommitment = True

        bot1Commitment = self.bot1.makeCommitment
        bot2Commitment = self.bot2.makeCommitment

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

    def payForCommitment(self):
        if (self.bot1.makeCommitment) : 
            bot2pays = self.bot2.payCommitment()

            if (bot2pays) :
                self.bot2.budget -= self.observation_cost
                self.bot2.opponentCommitType = self.bot1.commitType
            else : 
                self.bot2.assumeOpponentCommit()

        else : 
            bot1pays = self.bot1.payCommitment()

            if (bot1pays) :
                self.bot1.budget -= self.observation_cost
                self.bot1.opponentCommitType = self.bot1.commitType
            else : 
                self.bot1.assumeOpponentCommit()


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

        self.bot1.makeCommitment = False
        self.bot2.makeCommitment = False


    def checkCommitmentAndPayoff(self, roundNum):
        self.bot1.budget += self.bot1PayoffMatrix.get(self.bot1.history[2*roundNum]+self.bot1.history[1+2*roundNum])
        self.bot2.budget += self.bot2PayoffMatrix.get(self.bot2.history[2*roundNum]+self.bot2.history[1+2*roundNum])

    def gametime(self):
        self.takeUnilateralCommitment()
        self.payForCommitment()
        self.rounds()