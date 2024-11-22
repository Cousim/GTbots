import random

from Interfaces import Unilateral, ObservationCost, Deterministic
import Bot

class UnilateralOCostDeterministic(Bot, Unilateral, ObservationCost, Deterministic):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, payProb, makeCommitment, commitType, opponentCoopCommitType):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Unilateral.__init__(makeCommitment)
        ObservationCost.__init__(assumeCommitProb, payProb)
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
    


    def payObservationCost(self):
        if (random.randrange(1,101) <= self.payProb) : self.setOpponentCoopCommit()
        else : self.assumeOpponentCommit()


    def assumeOpponentCommit(self):
        if (random.randrange(1,101) < self.assumeCommitProb) : self.opponentCoopCommitType = True
        else : self.opponentCoopCommitType = False
    
    def setOpponentCoopCommit(self, opponentCoopCommitType):
        self.opponentCoopCommitType = opponentCoopCommitType

    def inTurn(self):
        if (self.makeCommitment) :
            if (self.commitType) : self.mostCoopStrategy.play(self.history, self.budget) # both coop commit
            else : self.mostDefectStrategy.play(self.history, self.budget) # both defect commit
        else : 
            if (self.opponentCoopCommitType) : self.mostCoopStrategy.play(self.history, self.budget) # both coop commit
            else : self.mostDefectStrategy.play(self.history, self.budget) # both defect commit


