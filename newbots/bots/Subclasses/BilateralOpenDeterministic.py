import random

from Interfaces import Bilateral, Open, Deterministic
import Bot

class BilateralOpenDeterministic(Bot, Bilateral, Open):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, commitType, opponentCoopCommitType):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Bilateral.__init__()
        Open.__init__()
        Deterministic.__init__(commitType, opponentCoopCommitType)

    def setCommitType(self, type):
        self.commitType = type #true for coop, false for defect

    def makeCommitment(self):
        if (random.randrange(1,101) < self.coopCommitProb) : 
            self.setCommitType(True)
            return None #return cooperation commitment if true
        else : 
            self.setCommitType(False)
            return None #return defection commitment if false

    def setOpponentCoopCommit(self, opponentCoopCommit):
        self.opponentCoopCommit = opponentCoopCommit

    def inTurn(self):
        if (self.commitType & self.opponentCoopCommitType) : self.mostCoopStrategy.play(self.history, self.budget) # both coop commit
        elif (self.commitType &  (not self.opponentCoopCommitType)) : self.lessCoopStrategy.play(self.history, self.budget) # self coop commit
        elif ((not self.coopCommit) == 0 & self.opponentCoopCommit == 100) : self.lessDefectStrategy.play(self.history, self.budget) # self defect commit
        else : self.mostDefectStrategy.play(self.history, self.budget) # both defect commit



    
            