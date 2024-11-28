from Interfaces import UnilateralGame, OCostGame, MixedGame
import Game
import random

import bots

class UnilateralOCostMixedGame(Game, UnilateralGame, OCostGame, MixedGame):
    def __init__(self, bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment, observation_cost):
        Game.__init__(bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment)
        UnilateralGame.__init__()
        OCostGame.__init__(observation_cost)
        MixedGame.__init__(self)
    
    def takeUnilateralCommitment(self):
        if (random.randRange(1, 101)<51) :
            self.bot1.makeCommitment = True
        else :
            self.bot2.makeCommitment = True

        bot1Commitment = self.bot1.makeCommitment
        bot2Commitment = self.bot2.makeCommitment

        if (bot1Commitment) :
            bot1CommitProb, bot1Seed = self.bot1.makeMixedCommitment()
            random.seed(bot1Seed)
            for i in range(self.game_length):
                if (random.randrange(1,101) <= bot1CommitProb) : 
                        self.bot1CommitMoves.append("C")
                else : 
                    self.bot1CommitMoves.append("D")
        if (bot2Commitment) :
            bot2CommitProb, bot2Seed = self.bot2.makeMixedCommitment()
            random.seed(bot1Seed)
            for i in range(self.game_length):
                if (random.randrange(1,101) <= bot2CommitProb) : 
                    self.bot2CommitMoves.append("C")
                else : 
                    self.bot2CommitMoves.append("D")

        
    def payForCommitment(self):
        bot1pays = False
        bot2pays = False

        if (self.bot1.makeCommitment) : bot2pays = self.bot2.payCommitment()
        else: bot1pays = self.bot1.payCommitment()
        
        if (bot1pays) :
            self.bot1.budget -= self.observation_cost
            self.bot1.opponentCommitType = self.bot2.commitType
        else : 
            self.bot1.assumeOpponentCommit()

        if (bot2pays) :
            self.bot2.budget -= self.observation_cost
            self.bot2.opponentCommitType = self.bot1.commitType
        else : 
            self.bot2.assumeOpponentCommit()

    def setOpponentCommitment(self):
        if (self.bot1.makeCommitment) : self.bot2.opponentCommitProb = self.bot1.coopCommitProb
        else : self.bot1.opponentCommitType = self.bot2.commitType

    def assumeOpponentCommitment(self):
        if (self.bot1.makeCommitment) : self.bot2.assumeOpponentCommit()
        else : self.bot1.assumeOpponentCommit()


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
        if (self.bot1.makeCommitment):
            if (self.bot1CommitList.get(roundNum) == self.bot1.history[2*roundNum]) :
                self.bot1.budget += self.commitment
            else : 
                self.bot1.budget += self.punishment
        
        if (self.bot2.makeCommitment):
            if (self.bot2CommitList.get(roundNum) == self.bot2.history[2*roundNum]) :
                self.bot2.budget += self.commitment
            else : 
                self.bot2.budget += self.punishment



    def gametime(self):
        self.takeUnilateralCommitment()
        self.setOpponentCommitment()
        self.rounds()