from bots.UnilateralClosedDeterministic import UnilateralClosedDeterministic
from game.UnilateralClosedDeterministicGame import UnilateralClosedDeterministicGame

from strategies.TitForTat import TitForTat
from strategies.TitForTwoTats import TitForTwoTats
from strategies.Pavlov import Pavlov
from strategies.GrimTrigger import GrimTrigger
from strategies.AlwaysDefect import AlwaysDefect

# Define strategies
titForTat = TitForTat()
titForTwoTats = TitForTwoTats()
pavlov = Pavlov()
grimTrigger = GrimTrigger()
alwaysDefect = AlwaysDefect()

# Create bot instances
unilateralClosedDeterministicBot1 = UnilateralClosedDeterministic(
    mostCoopStrat=titForTat, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=grimTrigger, 
    budget=0, 
    coopCommitProb=70, 
    makeCommitment=True,  # Example value for makeCommitment
    assumeCommitProb=50, 
    commitType=False,  # Default value for commitType
    opponentCoopCommitType=False  # Default value for opponentCoopCommitType
)

unilateralClosedDeterministicBot2 = UnilateralClosedDeterministic(
    mostCoopStrat=titForTat, 
    lessCoopStrat=titForTwoTats, 
    lessDefectStrat=pavlov, 
    mostDefectStrat=alwaysDefect, 
    budget=0, 
    coopCommitProb=80, 
    makeCommitment=False,  # Example value for makeCommitment
    assumeCommitProb=50, 
    commitType=False,  # Default value for commitType
    opponentCoopCommitType=False  # Default value for opponentCoopCommitType
)

# Define payoff matrices
bot1PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}
bot2PayoffMatrix = {"CC": 3, "DC": 5, "CD": 0, "DD": 1}

# Create game instance
unilateralClosedDeterministicGame = UnilateralClosedDeterministicGame(
    bot1=unilateralClosedDeterministicBot1, 
    bot2=unilateralClosedDeterministicBot2, 
    bot1PayoffMatrix=bot1PayoffMatrix, 
    bot2PayoffMatrix=bot2PayoffMatrix, 
    game_length=7, 
    commitment=+1, 
    punishment=-1
)

# Run the game
unilateralClosedDeterministicGame.gametime()
