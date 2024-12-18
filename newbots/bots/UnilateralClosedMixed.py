import random
from datetime import datetime

class UnilateralClosedMixed():
    bot_number = 0
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, assumeOpponentCommitProb, opponentCoopCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.makeCommitment = makeCommitment #no need
        self.assumeCommitProb = assumeOpponentCommitProb
        self.opponentCoopCommitProb = opponentCoopCommitProb
        self.seed = seed
        UnilateralClosedMixed.bot_number += 1
        self.id = UnilateralClosedMixed.bot_number


    def makeUnilateralCommitment(self):

        if (self.makeCommitment):
            self.seed = datetime.now().timestamp()
            return self.coopCommitProb, self.seed
        else :
            pass


    def assumeOpponentCommit(self):
        self.opponentCoopCommitProb = self.assumeCommitProb

    def inTurn(self, roundNum):
        return self.mostCoopStrat.play(self.history, self.budget, roundNum)




    
            