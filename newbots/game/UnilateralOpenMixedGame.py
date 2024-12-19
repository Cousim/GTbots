import random
from datetime import datetime

class UnilateralOpenMixedGame():
    def __init__(self, bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment):
        self.bot1 = bot1
        self.bot2 = bot2
        self.bot1PayoffMatrix = bot1PayoffMatrix
        self.bot2PayoffMatrix = bot2PayoffMatrix
        self.game_length = game_length
        self.commitment = commitment
        self.punishment = punishment
        self.bot1CommitMoves = []
        self.gameHistory = []
    
    
    def takeUnilateralCommitment(self):
        self.bot1.makeCommitment = True
        self.bot2.makeCommitment = False
        bot1CommitProb, bot1Seed = self.bot1.makeMixedCommitment()
        random.seed(bot1Seed)
        for i in range(self.game_length):
            if (random.randrange(1,101) <= bot1CommitProb) : 
                    self.bot1CommitMoves.append("C")
            else : 
                self.bot1CommitMoves.append("D")



    
    def setOpponentCommitment(self):
        self.bot2.opponentCommitProb = self.bot1.coopCommitProb
        self.bot1.opponentCommitProb = self.bot2.coopCommitProb


    def rounds(self):
        for i in range(self.game_length):
            bot1Move = self.bot1.inTurn(i)
            bot2Move = self.bot2.inTurn(i)

            self.bot1.history.append(("C" if bot1Move else "D")) #adds self move in the even indexes starting w/ 0
            self.bot1.history.append(("C" if bot2Move else "D"))

            self.bot2.history.append(("C" if bot2Move else "D"))
            self.bot2.history.append(("C" if bot1Move else "D"))


            self.checkCommitmentAndPayoff(i)
            roundStr = str(i)
            print("This round moves: "+self.bot1.history[i]+self.bot1.history[i+1])
            print("Round "+roundStr+" Bot 1 Budget: "+
                  str(self.bot1.budget))
            print("Round "+roundStr+" Bot 2 Budget: "+
                  str(self.bot2.budget))
            
        print(self.bot1.history)
        self.bot1.history = []
        self.bot2.history = []

        self.bot1.makeCommitment = False
        self.bot2.makeCommitment = False


    def checkCommitmentAndPayoff(self, roundNum):
        self.bot1.budget += self.bot1PayoffMatrix.get(self.bot1.history[2*roundNum]+self.bot1.history[1+2*roundNum])
        self.bot2.budget += self.bot2PayoffMatrix.get(self.bot2.history[2*roundNum]+self.bot2.history[1+2*roundNum])
        if (self.bot1.makeCommitment):
            if (self.bot1CommitMoves[roundNum] == self.bot1.history[2*roundNum]) :
                self.bot1.budget += self.commitment
            else : 
                self.bot1.budget += self.punishment
        



    def gametime(self):
        self.takeUnilateralCommitment()
        self.setOpponentCommitment()
        self.rounds()

    def sendMixedMatchupInfo(self):
        return [self.bot1.id, self.bot2.id, self.bot1CommitMoves, self.bot2CommitMoves, self.gameHistory]