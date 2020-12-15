
class SimulationResult:
    def __init__(self, initialTileList, coordinateList, moves, attackStrategy):
        self.initialTileList = initialTileList
        self.coordinateList = coordinateList
        self.moves = moves
        self.attackStrategy = attackStrategy
    
    def SimulationResultString(self):
        return self.attackStrategy + ' completed in ' + str(self.moves) + ' moves'
    