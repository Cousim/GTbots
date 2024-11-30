import random
from datetime import datetime

class BilateralOpenMixed():
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, opponentCoopCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.opponentCoopCommitProb = opponentCoopCommitProb
        self.seed = seed

    def makeMixedCommitment(self):
        self.seed = datetime.now().timestamp()
        return self.coopCommitProb, self.seed

    def setOpponentCoopCommit(self, opponentCommitProb):
        self.opponentCommitProb = opponentCommitProb

    def inTurn(self, roundNum):
        return self.mostCoopStrat.play(self.history, self.budget, roundNum)
    