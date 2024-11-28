import random

from Interfaces import Bilateral, ObservationCost, Mixed
import Bot

class BilateralOpenMixed(Bot, Bilateral, ObservationCost, Mixed):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, payProb, opponentCommitProb, seed):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Bilateral.__init__()
        ObservationCost.__init__(assumeCommitProb, payProb)
        Mixed.__init__(opponentCommitProb, seed)

    def makeMixedCommitment(self):
        return self.coopCommitProb, self.seed

    def setOpponentCoopCommit(self, opponentCommitProb):
        self.opponentCommitProb = opponentCommitProb

    def payObservationCost(self):
        if (random.randrange(1,101) <= self.payProb) : return True
        else : return False

    def assumeOpponentCommit(self):
        pass

    def inTurn(self):
        self.mostCoopStrategy().play
    