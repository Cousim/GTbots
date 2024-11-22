import random

from Interfaces import Unilateral, Closed, Deterministic
import Bot

class UnilateralClosedDeterministic(Bot, Unilateral, Closed, Deterministic):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, assumeCommitProb, commitType, opponentCoopCommitType):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Unilateral.__init__(makeCommitment)
        Closed.__init__(assumeCommitProb)
        Deterministic.__init__(commitType, opponentCoopCommitType)

    def setCommitType(self, type):
        self.commitType = type #true for coop, false for defect

    def makeUnilateralCommitment(self):
        if (self.makeCommitment):
            if (random.randrange(1,101) < self.coopCommitProb) : 
                self.setCommitType(True)
                return None #return cooperation commitment if true
            else : 
                self.setCommitType(False)
                return None #return defection commitment if false
        else :
            pass


    def assumeOpponentCommit(self):
        if (random.randrange(1,101) < self.assumeCommitProb) : self.opponentCoopCommitType = True
        else : self.opponentCoopCommitType = False

    def inTurn(self):
        if (self.makeCommitment) :
            if (self.commitType) : self.mostCoopStrategy.play(self.history, self.budget) # both coop commit
            else : self.mostDefectStrategy.play(self.history, self.budget) # both defect commit
        else : 
            if (self.opponentCoopCommitType) : self.mostCoopStrategy.play(self.history, self.budget) # both coop commit
            else : self.mostDefectStrategy.play(self.history, self.budget) # both defect commit


