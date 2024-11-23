import Strategy

class Pavlov(Strategy):

    def play(botHistory, botBudget):
        if not botHistory:
            return True
        if (botHistory[-1][0] == "C") and (botHistory[-1][1]=="D"):
            return False
        return True