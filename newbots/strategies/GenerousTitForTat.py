class GenerousTitForTat():
    def play(self, botHistory, botBudget, roundNum):
        print("Generous tit for tat")
        revenge = False
        if botHistory == [] or len(botHistory) < 4:
            return True
        else:
            if revenge:
                revenge = False
                return False
            elif (botHistory[2*roundNum-1] == "D" and botHistory[2*roundNum-3] == "D"):
                revenge = True
                return False
            else:
                return True
            
    def name(self):
        return "generoustitfortat"