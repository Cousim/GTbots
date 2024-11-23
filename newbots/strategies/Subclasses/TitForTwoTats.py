import Strategy

class TitForTwoTats(Strategy):
    def play(botHistory, botBudget):
        if not botHistory:
            return True
        else:
            if (botHistory[-1][1] == "C") : return True
            else :  return False
            