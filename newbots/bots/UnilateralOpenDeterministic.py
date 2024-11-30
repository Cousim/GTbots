import random
from datetime import datetime



class UnilateralOpenDeterministic():
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, commitType, opponentCoopCommitType):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.makeCommitment = makeCommitment
        self.commitType = commitType #true for coop, false for defect
        self.opponentCoopCommitType = opponentCoopCommitType

    def setCommitType(self, type):
        self.commitType = type #true for coop, false for defect

    def makeUnilateralCommitment(self):
        random.seed(datetime.now().timestamp())
        if (self.makeCommitment):
            if (random.randrange(1,101) < self.coopCommitProb) : 
                self.setCommitType(True)
                return self.commitType #return cooperation commitment if true
            else : 
                self.setCommitType(False)
                return self.commitType #return defection commitment if false
        else :
            pass


    def setOpponentCoopCommit(self, opponentCoopCommit):
        self.opponentCoopCommit = opponentCoopCommit

    def inTurn(self, roundNum):
        if (self.makeCommitment) :
            if (self.commitType) : self.mostCoopStrat.play(self.history, self.budget, roundNum) # both coop commit
            else : self.mostDefectStrat.play(self.history, self.budget, roundNum) # both defect commit
        else : 
            if (self.opponentCoopCommitType) : self.mostCoopStrat.play(self.history, self.budget, roundNum) # both coop commit
            else : self.mostDefectStrat.play(self.history, self.budget, roundNum) # both defect commit




    
            