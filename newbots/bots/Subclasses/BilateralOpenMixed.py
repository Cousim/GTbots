import random

from Interfaces import Bilateral, Open, Mixed
import Bot

class BilateralOpenMixed(Bot, Bilateral, Open, Mixed):
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, coopCommitProb, budget, opponentCommitProb):
        Bot.__init__(mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb)
        Bilateral.__init__()
        Open.__init__()
        Mixed.__init__(opponentCommitProb)

    def makeMixedCommitment(self):
        return self.coopCommitProb

    def setOpponentCoopCommit(self, opponentCommitProb):
        self.opponentCommitProb = opponentCommitProb

    #mixed bots wont have strategies i guess???
    '''
    def inTurn(self):
        if (self.commitType & self.opponentCoopCommitType) : self.mostCoopStrategy.play() # both coop commit
        elif (self.commitType &  (not self.opponentCoopCommitType)) : self.lessCoopStrategy.play() # self coop commit
        elif ((not self.coopCommit) == 0 & self.opponentCoopCommit == 100) : self.lessDefectStrategy.play() # self defect commit
        else : self.mostDefectStrategy.play() # both defect commit
    '''