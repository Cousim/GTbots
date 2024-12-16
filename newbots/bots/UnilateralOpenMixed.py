import random
from datetime import datetime

class UnilateralOpenMixed():
    bot_number = 0
    def __init__(self, mostCoopStrat, lessCoopStrat, lessDefectStrat, mostDefectStrat, budget, coopCommitProb, makeCommitment, opponentCoopCommitProb, seed):
        self.mostCoopStrat = mostCoopStrat
        self.lessCoopStrat = lessCoopStrat
        self.lessDefectStrat = lessDefectStrat
        self.mostDefectStrat = mostDefectStrat
        self.coopCommitProb = coopCommitProb
        self.budget = budget
        self.history = []
        self.makeCommitment = makeCommitment
        self.opponentCoopCommitProb = opponentCoopCommitProb
        self.seed = seed
        UnilateralOpenMixed.bot_number += 1
        self.id = UnilateralOpenMixed.bot_number


    def makeMixedCommitment(self):
        if (self.makeCommitment):
            self.seed = datetime.now().timestamp()
            return self.coopCommitProb, self.seed
        else :
            pass


    def setOpponentCoopCommit(self, opponentCoopCommit):
        self.opponentCoopCommit = opponentCoopCommit

    def inTurn(self, roundNum):
        self.mostCoopStrat.play(self.history, self.budget, roundNum)




    
            