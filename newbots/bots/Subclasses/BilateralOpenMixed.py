import random

from Interfaces import Bilateral, Open, Mixed
import Bot

class BilateralOpenMixed(Bot, Bilateral, Open, Mixed):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, opponentCommitProb, seed):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Bilateral.__init__()
        Open.__init__()
        Mixed.__init__(opponentCommitProb, seed)

    def makeMixedCommitment(self):
        return self.coopCommitProb, self.seed

    def setOpponentCoopCommit(self, opponentCommitProb):
        self.opponentCommitProb = opponentCommitProb

    def inTurn(self):
        self.mostCoopStrategy().play
    