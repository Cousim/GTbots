from Interfaces import Unilateral, Closed, Mixed
import Bot

class UnilateralClosedMixed(Bot, Unilateral, Closed, Mixed):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, assumeOpponentCommitProb, opponentCoopCommitProb, seed):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Unilateral.__init__(makeCommitment)
        Closed.__init__(assumeOpponentCommitProb)
        Mixed.__init__(opponentCoopCommitProb, seed)


    def makeUnilateralCommitment(self):
        if (self.makeCommitment):
                return self.coopCommitProb
        else :
            pass


    def assumeOpponentCommit(self):
        self.opponentCoopCommitProb = self.assumeOpponentCommitProbs

    def inTurn(self):
        self.mostCoopStrategy.play()




    
            