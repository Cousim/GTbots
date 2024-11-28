import random

from Interfaces import Unilateral, Open, Mixed
import Bot

class UnilateralOpenMixed(Bot, Unilateral, Open, Mixed):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, opponentCoopCommitProb, seed):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Unilateral.__init__(makeCommitment)
        Open.__init__()
        Mixed.__init__(opponentCoopCommitProb, seed)


    def makeUnilateralCommitment(self):
        if (self.makeCommitment):
                return self.coopCommitProb
        else :
            pass


    def setOpponentCoopCommit(self, opponentCoopCommit):
        self.opponentCoopCommit = opponentCoopCommit

    def inTurn(self):
        self.mostCoopStrategy.play()




    
            