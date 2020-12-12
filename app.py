from models import Node, Tile, Board, Ship, BattleshipEngine, SimulationResult

engine = BattleshipEngine()
engine.DEVStartBattleshipSimulation(10)

for result in engine.simulationResuts.values():
    print(result.SimulationResultString() + '\t' + str(len(result.coordinateList)))


#todo: remove duplicate items in the coordinate string, make sure its not being used anywhere more than once