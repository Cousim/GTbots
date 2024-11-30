import random


class Randomized():

    def __init__(self, prob):
        self.prob = prob

    def play(self, botHistory, botBudget, roundNum):
        if (random.randrange(0,101)<self.prob) : return True
        else : return False

    def name(self):
        return "randomized"