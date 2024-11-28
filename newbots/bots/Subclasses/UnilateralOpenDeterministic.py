import random

from Interfaces import Unilateral, Open, Deterministic
import Bot

class UnilateralOpenDeterministic(Bot, Unilateral, Open, Deterministic):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, commitType, opponentCoopCommitType):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Unilateral.__init__(makeCommitment)
        Open.__init__()
        Deterministic.__init__(commitType, opponentCoopCommitType)

    def setCommitType(self, type):
        self.commitType = type #true for coop, false for defect

    def makeUnilateralCommitment(self):
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

    def inTurn(self):
        if (self.makeCommitment) :
            if (self.commitType) : self.mostCoopStrategy.play(self.history, self.budget) # both coop commit
            else : self.mostDefectStrategy.play(self.history, self.budget) # both defect commit
        else : 
            if (self.opponentCoopCommitType) : self.mostCoopStrategy.play(self.history, self.budget) # both coop commit
            else : self.mostDefectStrategy.play(self.history, self.budget) # both defect commit




    
            