from bots.Subclasses import *
from bots.Interfaces import *
from game.Subclasses import *
from game.Interfaces import *
from strategies.Subclasses import TitForTat, TitForTwoTats, Pavlov, GrimTrigger, AlwaysDefect

titForTat = TitForTat()
titForTwoTats = TitForTwoTats()
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect()


bilateralClosedDeterministicBot1 = BilateralClosedDeterministic(titForTat, titForTwoTats, pavlov, grimTrigger, 0, 70, 50, False, False)
bilateralClosedDeterministicBot2 = BilateralClosedDeterministic(titForTat, titForTwoTats, pavlov, alwaysDefect, 0, 60, 50, False, False)

bot1PayoffMatrix = {"CC": (3,3),"DC":(5,0),"CD":(0,5),"DD":(1,1)}
bot2PayoffMatrix = {"CC": (3,3),"DC":(5,0),"CD":(0,5),"DD":(1,1)}

bilateralClosedDeterministicGame = BilateralClosedDeterministicGame(bilateralClosedDeterministicBot1, bilateralClosedDeterministicBot2, bot1PayoffMatrix, bot2PayoffMatrix, 7, +1, -1)

bilateralClosedDeterministicGame.gametime()