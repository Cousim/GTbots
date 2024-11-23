import Strategy

class TitForTat(Strategy):

    def play(botHistory, botBudget) :
        if not botHistory:
            return True #True for cooperation
        else:
            if (botHistory[-1][1] == "C") : 
                return True
            else :
                return False #False for defection