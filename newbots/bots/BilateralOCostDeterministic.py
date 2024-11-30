import random
from datetime import datetime

class BilateralOCostDeterministic():
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, payProb, commitType, opponentCoopCommitType):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.assumeCommit = assumeCommitProb
        self.payProb = payProb
        self.commitType = commitType #true for coop, false for defect
        self.opponentCoopCommitType = opponentCoopCommitType

    def setCommitType(self, type):
        self.commitType = type #true for coop, false for defect

    def makeCommitment(self):
        random.seed(datetime.now().timestamp())
        if (random.randrange(1,101) < self.coopCommitProb) : 
            self.setCommitType(True)
            return self.commitType #return cooperation commitment if true
        else : 
            self.setCommitType(False)
            return self.commitType #return defection commitment if false

    def payObservationCost(self):
        random.seed(datetime.now().timestamp())
        if (random.randrange(1,101) <= self.payProb) : return True
        else : return False


    def assumeOpponentCommit(self):
        if (random.randrange(1,101) < self.assumeCommitProb) : self.opponentCoopCommitType = True
        else : self.opponentCoopCommitType = False
    
    def setOpponentCoopCommit(self, opponentCoopCommitType):
        self.opponentCoopCommitType = opponentCoopCommitType

    def inTurn(self, roundNum):
        if (self.commitType & self.opponentCoopCommitType) : return self.mostCoopStrategy.play(self.history, self.budget, roundNum) # both coop commit
        elif (self.commitType &  (not self.opponentCoopCommitType)) : return self.lessCoopStrategy.play(self.history, self.budget, roundNum) # self coop commit
        elif ((not self.coopCommit) == 0 & self.opponentCoopCommit == 100) : return self.lessDefectStrategy.play(self.history, self.budget, roundNum) # self defect commit
        else : return self.mostDefectStrategy.play(self.history, self.budget, roundNum) # both defect commit

