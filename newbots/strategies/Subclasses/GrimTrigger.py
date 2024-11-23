import Strategy

class GrimTrigger(Strategy):
     
     def play(botHistory, botBudget):
          if ('D' in botHistory) :
               return True
          else :
               return False