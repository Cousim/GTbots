import random

from Interfaces import Bilateral, Closed, Deterministic
import Bot



class BilateralClosedDeterministic(Bot, Bilateral, Closed, Deterministic):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, commitType, opponentCoopCommitType):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Bilateral.__init__()
        Closed.__init__(assumeCommitProb)
        Deterministic.__init__(commitType, opponentCoopCommitType)

    def setCommitType(self, type):
        self.commitType = type #true for coop, false for defect

    def assumeOpponentCommit(self):
        if (random.randrange(1,101) < self.assumeCommitProb) : self.opponentCoopCommitType = True
        else : self.opponentCoopCommitType = False

    def makeCommitment(self):
        if (random.randrange(1,101) < self.coopCommitProb) : 
            self.setCommitType(True)
            return self.commitType #return cooperation commitment if true
        else : 
            self.setCommitType(False)
            return self.commitType #return defection commitment if false

    def inTurn(self):
        if (self.commitType & self.opponentCoopCommitType) : self.mostCoopStrategy.play(self.history, self.budget) # both coop commit
        elif (self.commitType &  (not self.opponentCoopCommitType)) : self.lessCoopStrategy.play(self.history, self.budget) # self coop commit
        elif ((not self.commitType)  & self.opponentCoopCommitType) : self.lessDefectStrategy.play(self.history, self.budget) # self defect commit
        else : self.mostDefectStrategy.play(self.history, self.budget) # both defect commit
        

        