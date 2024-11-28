from Interfaces import Bilateral, Closed, Mixed
import Bot

class BilateralClosedMixed(Bot, Bilateral, Closed, Mixed):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, assumeCommitProb, opponentCommitProb, seed):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Bilateral.__init__()
        Closed.__init__(assumeCommitProb)
        Mixed.__init__(opponentCommitProb, seed)

    def makeMixedCommitment(self):
        return self.coopCommitProb, self.seed


    def assumeOpponentCommit(self):
        self.opponentCommitProb = self.assumeOpponentCommit

    def inTurn(self):
        self.mostCoopStrategy.play()
    