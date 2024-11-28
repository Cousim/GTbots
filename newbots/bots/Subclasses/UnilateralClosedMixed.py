import random

from Interfaces import Unilateral, Closed, Mixed
import Bot

class UnilateralClosedMixed(Bot, Unilateral, Closed, Mixed):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, opponentCoopCommitProb, seed):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Unilateral.__init__(makeCommitment)
        Closed.__init__()
        Mixed.__init__(opponentCoopCommitProb, seed)


    def makeUnilateralCommitment(self):
        if (self.makeCommitment):
                return self.coopCommitProb
        else :
            pass


    def assumeOpponentCommit(self):
        pass

    def inTurn(self):
        self.mostCoopStrategy.play()




    
            