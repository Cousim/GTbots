import random

from Interfaces import Unilateral, ObservationCost, Mixed
import Bot

class UnilateralOCostMixed(Bot, Unilateral, ObservationCost, Mixed):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment,  payProb, opponentCoopCommitProb, seed,):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Unilateral.__init__(makeCommitment)
        ObservationCost.__init__(payProb)
        Mixed.__init__(opponentCoopCommitProb, seed)


    def makeUnilateralCommitment(self):
        if (self.makeCommitment):
                return self.coopCommitProb
        else :
            pass

    def setOpponentCoopCommit(self, opponentCoopCommit):
        self.opponentCoopCommit = opponentCoopCommit

    def payObservationCost(self):
        if (random.randrange(1,101) <= self.payProb) : return True
        else : return False

    def assumeOpponentCommit(self):
        pass

    def inTurn(self):
        self.mostCoopStrategy.play()




    
            