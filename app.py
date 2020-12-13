from BattleshipEngine import BattleshipEngine
from SimulationResult import SimulationResult

engine = BattleshipEngine()
engine.DEVStartBattleshipSimulation(10)

for result in engine.simulationResuts.values():
    print(result.SimulationResultString() + '\t' + str(len(result.coordinateList)))
