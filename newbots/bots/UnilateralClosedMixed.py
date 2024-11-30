import random
from datetime import datetime

class UnilateralClosedMixed():
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, assumeOpponentCommitProb, opponentCoopCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.makeCommitment = makeCommitment
        self.assumeCommitProb = assumeOpponentCommitProb
        self.opponentCoopCommitProb = opponentCoopCommitProb
        self.seed = seed


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




    
            