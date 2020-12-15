
import statistics

class SimulationStatistics:
    def __init__(self, simulationResultList):
        self.simulationResultList = simulationResultList
    
    def PrintSimulationStatistics(self):
        minMoves = min(self.simulationResultList, key=lambda x: x.moves)  
        maxMoves = max(self.simulationResultList, key=lambda x: x.moves)

        uniqueAttackStrategies = list(set(SimulationResult.attackStrategy for SimulationResult in self.simulationResultList))
        
        for currentAttackStrategy in uniqueAttackStrategies:
            print(currentAttackStrategy + ':')
            selectList = filter(lambda x: x.attackStrategy == currentAttackStrategy, self.simulationResultList)
            minMoves = min(selectList, key=lambda x: x.moves)
            selectList = filter(lambda x: x.attackStrategy == currentAttackStrategy, self.simulationResultList)
            maxMoves = max(selectList, key=lambda x: x.moves)
            print('Min move: ' + str(minMoves.moves))
            print('Max move: ' + str(maxMoves.moves))
