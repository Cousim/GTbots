import random

import Strategy 

class Randomized(Strategy):

    def __init__(self, prob):
        Strategy.__init__()
        self.prob = prob

    def play(self, botHistory, botBudget):
        if (random.randrange(0,101)<self.prob) : return True
        else : return False