from typing import Any
import random

class Bot:
    def __init__(self, budget):
        self.budget = budget
        self.history = []
        self.results = None
        self.game_length = None
        self.commitment = None
        self.punishment = None
        self.observation_cost = None
        self.P1 = False

    def rules(self, results, game_length, commitment, punishment, observation_cost, P1):
        self.results = results
        self.game_length = game_length
        self.commitment = commitment
        self.punishment = punishment
        self.observation_cost = observation_cost
        self.P1 = P1

    def setP1(self, flag):
        self.P1 = flag
 
    def getP1(self):
        return self.P1
    
    def addHistory(self, moves):
        self.history.append(moves)

    def getHistory(self):
        return self.history
    
    def addPayoff(self, p):
        self.budget += p

    def getBudget(self):
        return self.budget

class AlwaysDefect(Bot):
    def getCommitment(self):
        return "D"
    
    def nextMove(self):
        return "D"

class AlwaysCooperate(Bot):
    def getCommitment(self):
        return "C"
    
    def nextMove(self):
        return "C"

class TitForTat(Bot):
    def nextMove(self):
        if not self.getHistory():
            return "C"
        else:
            return self.getHistory()[-1][1]

class TitForTwoTats(Bot):
    def nextMove(self):
        if (len(self.getHistory()) >= 2) and (self.getHistory()[-1][1] + self.getHistory()[-2][1] == "DD"):
            return "D"
        return "C"
    
class Pavlov(Bot):
    def nextMove(self):
        if not self.getHistory():
            return "C"
        if (self.getHistory()[-1][0] == "C") and (self.getHistory()[-1][1]=="D"):
            return "D"
        return "C"


class GrimTrigger(Bot):
    def __init__(self, budget):
        super().__init__(budget)
        self.flag = False

    def nextMove(self):
        if (self.getHistory()) and (self.getHistory()[-1][1] == "D"):
            self.flag = True

        if self.flag:
            return "D"
        else:
            return "C"

class Randomized(Bot):
    def __init__(self, budget, prob):
        super().__init__(budget)
        self.prob = prob

    def nextMove(self):
        if random.random()<self.prob:
            return "D"
        return "C"