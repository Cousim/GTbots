

class BilateralClosedDeterministicGame():
    
    def __init__(self, bot1, bot2, bot1PayoffMatrix, bot2PayoffMatrix, game_length, commitment, punishment):
        self.bot1 = bot1
        self.bot2 = bot2
        self.bot1PayoffMatrix = bot1PayoffMatrix
        self.bot2PayoffMatrix = bot2PayoffMatrix
        self.game_length = game_length
        self.commitment = commitment
        self.punishment = punishment
        self.gameHistory = []
    

    def takeBilateralCommitment(self):
        bot1Commitment = self.bot1.makeCommitment()
        bot2Commitment = self.bot2.makeCommitment()

        if (bot1Commitment) :
            self.bot1PayoffMatrix.update({"CC": self.bot1PayoffMatrix.get("CC") + self.commitment})
            self.bot1PayoffMatrix.update({"CD": self.bot1PayoffMatrix.get("CD") + self.commitment})
            self.bot1PayoffMatrix.update({"DC": self.bot1PayoffMatrix.get("DC") + self.punishment})
            self.bot1PayoffMatrix.update({"DD": self.bot1PayoffMatrix.get("DD") + self.punishment})
        else : 
            self.bot1PayoffMatrix.update({"CC": self.bot1PayoffMatrix.get("CC") + self.punishment})
            self.bot1PayoffMatrix.update({"CD": self.bot1PayoffMatrix.get("CD") + self.punishment})
            self.bot1PayoffMatrix.update({"DC": self.bot1PayoffMatrix.get("DC") + self.commitment})
            self.bot1PayoffMatrix.update({"DD": self.bot1PayoffMatrix.get("DD") + self.commitment})

        if (bot2Commitment) :
            self.bot2PayoffMatrix.update({"CC": self.bot2PayoffMatrix.get("CC") + self.commitment})
            self.bot2PayoffMatrix.update({"CD": self.bot2PayoffMatrix.get("CD") + self.commitment})
            self.bot2PayoffMatrix.update({"DC": self.bot2PayoffMatrix.get("DC") + self.punishment})
            self.bot2PayoffMatrix.update({"DD": self.bot2PayoffMatrix.get("DD") + self.punishment})
        else : 
            self.bot2PayoffMatrix.update({"CC": self.bot2PayoffMatrix.get("CC") + self.punishment})
            self.bot2PayoffMatrix.update({"CD": self.bot2PayoffMatrix.get("CD") + self.punishment})
            self.bot2PayoffMatrix.update({"DC": self.bot2PayoffMatrix.get("DC") + self.commitment})
            self.bot2PayoffMatrix.update({"DD": self.bot2PayoffMatrix.get("DD") + self.commitment})
   

    def assumeCommitment(self):
        self.bot1.opponentCommitType = self.bot1.assumeOpponentCommit()
        self.bot2.opponentCommitType = self.bot2.assumeOpponentCommit()


    def rounds(self):
        print("Bot 1 Strategy: " + str(self.bot1.stratName()))
        print("Bot 2 Strategy: "+ str(self.bot2.stratName()))

        self.bot1.stratName()
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
        
        self.gameHistory = self.bot1.history
        self.bot1.history = []
        self.bot2.history = []


    def checkCommitmentAndPayoff(self, roundNum):
        self.bot1.budget += self.bot1PayoffMatrix.get(self.bot1.history[2*roundNum]+self.bot1.history[1+2*roundNum])
        self.bot2.budget += self.bot2PayoffMatrix.get(self.bot2.history[2*roundNum]+self.bot2.history[1+2*roundNum])


    def gametime(self):
        self.takeBilateralCommitment()
        self.assumeCommitment()
        self.rounds()

    def sendMatchupInfo(self):
        return [self.bot1.id, self.bot2.id, self.bot1.commitType, self.bot2.commitType, self.gameHistory]


