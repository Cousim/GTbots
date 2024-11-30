import random
from datetime import datetime

class UnilateralOCostMixed():
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment,  payProb, opponentCoopCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.makeCommitment = makeCommitment
        self.payProb = payProb
        self.opponentCoopCommitProb = opponentCoopCommitProb
        self.seed = seed


    def makeUnilateralCommitment(self):
        if (self.makeCommitment):
            self.seed = datetime.now().timestamp()
            return self.coopCommitProb, self.seed
        else :
            pass

    def setOpponentCoopCommit(self, opponentCoopCommit):
        self.opponentCoopCommit = opponentCoopCommit

    def payObservationCost(self):
        random.seed(datetime.now().timestamp())
        if (random.randrange(1,101) <= self.payProb) : return True
        else : return False

    def assumeOpponentCommit(self):
        pass

    def inTurn(self, roundNum):
        self.mostCoopStrat.play(self.history, self.budget, roundNum)




    
            