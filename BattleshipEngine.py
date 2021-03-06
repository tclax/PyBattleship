from Board import Board
from Ship import Ship
from SimulationResult import SimulationResult
from SimulationStatistics import SimulationStatistics


import functionalComponents
import random, copy

#Represents a game of battleship. Using a board of set ships, the engine will attempt to compute positions of the ships in an attempt to sink all the ships. The engine will determine how many turns have passed after all ships are sunk. The fewer the turns, the better the engine is.
class BattleshipEngine: 
    def __init__(self):
        self.board = Board(8)
        self.simulationResuts = {}

    def PrintBoard(self):
        self.board.PrintBoard()  
    
    def SetNewBoard(self):
        #setup new board
        self.board = Board(8)

        #place 5 ships in random coordinates
        self.board.PlaceShipAtRandomCoordinate(Ship(5, 'A'))
        self.board.PlaceShipAtRandomCoordinate(Ship(4, 'B'))
        self.board.PlaceShipAtRandomCoordinate(Ship(3, 'S'))
        self.board.PlaceShipAtRandomCoordinate(Ship(3, 'S'))
        self.board.PlaceShipAtRandomCoordinate(Ship(2, 'C'))

        self.board.initalTileListState = copy.deepcopy(self.board.tileList)

    #runs the Battleship simulations against a set number of attack strategies.
    def StartBattleshipSimulation(self, iterations):
        for x in range(0, iterations):
            #start a new random board
            self.SetNewBoard()           

            #start the simulation for the horizontal attack
            simulationResult = self.HorizontalLinearAttackStrategy()
            #add the results to the dictionary
            self.simulationResuts[simulationResult.attackStrategy+'#'+str(x)] = simulationResult
            #reset the board
            self.board.PrintBoard()
            self.board.ResetBoard()

            self.board.PrintBoard()

            #start the simulation for the vertical attack
            simulationResult = self.VerticalLinearAttackStrategy()
            #add the results to the dictionary
            self.simulationResuts[simulationResult.attackStrategy+'#'+str(x)] = simulationResult
            #reset the board
            self.board.PrintBoard()
            self.board.ResetBoard()
            self.board.PrintBoard()
    
    def DEVStartBattleshipSimulation(self, iterations):
        self.SetNewBoard()
        for x in range(0, iterations):
            simulationResult = self.DiagonalHitScanAttackStratgy()
            self.simulationResuts[simulationResult.attackStrategy+'#'+str(x)] = simulationResult
            self.board.ResetBoard()

            simulationResult = self.DiagonalLinearAttackStrategy()
            self.simulationResuts[simulationResult.attackStrategy+'#'+str(x)] = simulationResult
            self.board.ResetBoard()

            simulationResult = self.RandomHitScanAttackStrategy()
            self.simulationResuts[simulationResult.attackStrategy+'#'+str(x)] = simulationResult
            self.board.ResetBoard()

            simulationResult = self.VerticalLinearAttackStrategy()
            self.simulationResuts[simulationResult.attackStrategy+'#'+str(x)] = simulationResult
            self.board.ResetBoard()

            simulationResult = self.HorizontalLinearAttackStrategy()
            self.simulationResuts[simulationResult.attackStrategy+'#'+str(x)] = simulationResult
            self.board.ResetBoard()
        
        stats = SimulationStatistics(self.simulationResuts.values())
        stats.PrintSimulationStatistics()
            
    #allows the user to attack by entering coordinates 
    def AttackStrategyUserInput(self):      
        moves = 0
        while(not self.board.CheckIfAllShipsSunk()):
            print('Not sunk')
            moves += 1
            self.board.PrintBoard()
            while True:
                print('Enter a starting coordinate for the ship:')
                x = input('Enter x coordinate: ')
                y = input('Enter y coordinate: ')
                if(functionalComponents.CoordinateString(x,y) in self.board.tileList and (self.board.tileList[functionalComponents.CoordinateString(x,y)].code != self.board.missTileCode or self.board.tileList[functionalComponents.CoordinateString(x,y)].code != self.board.hitTileCode)):
                    break
            y = int(y)

            self.board.AttackBoard(functionalComponents.CoordinateString(x,y))
    
    #Attacks from an inital starting point left to right
    def HorizontalLinearAttackStrategy(self):        
        coordinateList = []  
        moves = 1

        #calc starting point and make first attack
        startingChar = 'A'
        startingX = chr(ord(startingChar) + random.randint(0, self.board.size - 1))
        startingY = random.randint(0, self.board.size - 1)
        coordinateList.append(functionalComponents.CoordinateString(startingX, startingY))
        self.board.AttackBoard(functionalComponents.CoordinateString(startingX, startingY))
        x = str(startingX)
        y = startingY
        originalTile = self.board.tileList[functionalComponents.CoordinateString(x, y)]

        #loop until all the ships are sunk
        #calculate the next position to attack
        while(not self.board.CheckIfAllShipsSunk()):
            #self.board.PrintBoard()
            currentTile = self.board.tileList[functionalComponents.CoordinateString(x, y)]

            if(not currentTile.hasEastTile and not currentTile.hasSouthTile):
                x = startingChar
                y = 0
            elif(not currentTile.hasEastTile):
                x = chr(ord(x) + 1)
                y = 0
            else:
                y += 1

            coordinateList.append(functionalComponents.CoordinateString(x, y))
            self.board.AttackBoard(functionalComponents.CoordinateString(x,y))  
            moves += 1  

        return SimulationResult(self.board.initalTileListState, coordinateList, moves, "Horizontal Linear")  

    #attacks top to bottom, starting at a random point and moving down each row, then to the next column
    def VerticalLinearAttackStrategy(self):        
        coordinateList = []  
        moves = 1

        #calc starting point and make first attack
        startingChar = 'A'
        startingX = chr(ord(startingChar) + random.randint(0, self.board.size - 1))
        startingY = random.randint(0, self.board.size - 1)        
        coordinateList.append(functionalComponents.CoordinateString(startingX, startingY))
        self.board.AttackBoard(functionalComponents.CoordinateString(startingX, startingY))
        x = str(startingX)
        y = startingY
        originalTile = self.board.tileList[functionalComponents.CoordinateString(x, y)]

        #loop until all the ships are sunk
        #calculate the next position to attack
        while(not self.board.CheckIfAllShipsSunk()):
            #self.board.PrintBoard()
            currentTile = self.board.tileList[functionalComponents.CoordinateString(x, y)]

            if(not currentTile.hasEastTile and not currentTile.hasSouthTile):
                x = startingChar
                y = 0
            elif(not currentTile.hasSouthTile):
                x = startingChar
                y += 1
            else:
                x = chr(ord(x) + 1)


            coordinateList.append(functionalComponents.CoordinateString(x, y))
            self.board.AttackBoard(functionalComponents.CoordinateString(x, y))  
            moves += 1  

        return SimulationResult(self.board.initalTileListState, coordinateList, moves, "Vertical Linear")
    
    #randomly attacks coordinates until a hit is registers. then attack each adjacent tile until each direction registers a miss or is off the board
    def RandomHitScanAttackStrategy(self):
        coordinateList = []
        validCoordinateList = []
        moves = 0

        #set all adjacent flags to false until a hit is registered
        checkNorth = False
        checkSouth = False
        checkWest = False
        checkEast = False

        currentCoordinate = ''

        #build a list of all coordinates 
        availableCoordinates = self.board.GetAvailableCoordinateList()

        #loop until all ships are sunk
        while(not self.board.CheckIfAllShipsSunk()):
            #if all check flags are set to false, calc a new random coordinate that is available           
            if(not checkNorth and not checkSouth and not checkWest and not checkEast):
                currentCoordinate = random.choice(availableCoordinates)
                initialCoordinate = currentCoordinate
            elif(checkNorth):
                while(checkNorth):
                    currentCoordinate = functionalComponents.MoveCoordinateNorth(currentCoordinate)

                    #attack with the generated coordinate
                    coordinateList.append(currentCoordinate)
                    availableCoordinates.remove(currentCoordinate)
                    self.board.AttackBoard(currentCoordinate) 
                    checkNorth = self.board.tileList[currentCoordinate].hasNorthTile and functionalComponents.MoveCoordinateNorth(currentCoordinate) in availableCoordinates and self.board.tileList[currentCoordinate].code != self.board.missTileCode
                    moves += 1
            elif(checkSouth):
                 while(checkSouth):
                    currentCoordinate = functionalComponents.MoveCoordinateSouth(currentCoordinate)
                    
                    #attack with the generated coordinate
                    coordinateList.append(currentCoordinate)
                    availableCoordinates.remove(currentCoordinate)
                    self.board.AttackBoard(currentCoordinate)
                    checkSouth = self.board.tileList[currentCoordinate].hasSouthTile and functionalComponents.MoveCoordinateSouth(currentCoordinate) in availableCoordinates and self.board.tileList[currentCoordinate].code != self.board.missTileCode 
                    moves += 1
            elif(checkWest):
                 while(checkWest):
                    currentCoordinate = functionalComponents.MoveCoordinateWest(currentCoordinate)
                    
                    #attack with the generated coordinate
                    coordinateList.append(currentCoordinate)
                    availableCoordinates.remove(currentCoordinate)
                    self.board.AttackBoard(currentCoordinate)  
                    checkWest = self.board.tileList[currentCoordinate].hasWestTile and functionalComponents.MoveCoordinateWest(currentCoordinate) in availableCoordinates and self.board.tileList[currentCoordinate].code != self.board.missTileCode
                    moves += 1
            elif(checkEast):
                while(checkEast):
                    currentCoordinate = functionalComponents.MoveCoordinateEast(currentCoordinate)
                    
                    #attack with the generated coordinate
                    coordinateList.append(currentCoordinate)
                    availableCoordinates.remove(currentCoordinate)
                    self.board.AttackBoard(currentCoordinate)  
                    checkEast = self.board.tileList[currentCoordinate].hasEastTile and functionalComponents.MoveCoordinateEast(currentCoordinate) in availableCoordinates and self.board.tileList[currentCoordinate].code != self.board.missTileCode
                    moves += 1

            #set back to the original coordinate
            currentCoordinate = initialCoordinate

            #adjust check flags to the new coordinate
            checkNorth = self.board.tileList[currentCoordinate].hasNorthTile and functionalComponents.MoveCoordinateNorth(currentCoordinate) in availableCoordinates
            checkSouth = self.board.tileList[currentCoordinate].hasSouthTile and functionalComponents.MoveCoordinateSouth(currentCoordinate) in availableCoordinates
            checkWest = self.board.tileList[currentCoordinate].hasWestTile and functionalComponents.MoveCoordinateWest(currentCoordinate) in availableCoordinates
            checkEast = self.board.tileList[currentCoordinate].hasEastTile and functionalComponents.MoveCoordinateEast(currentCoordinate) in availableCoordinates
            
            #attack with the generated coordinate       
            if(currentCoordinate in availableCoordinates):
                coordinateList.append(currentCoordinate)
                availableCoordinates.remove(currentCoordinate)
                self.board.AttackBoard(currentCoordinate)  
                moves += 1 
        
        return SimulationResult(self.board.initalTileListState, coordinateList, moves, "Random Hitscan")
   
   #starts with a random tile on the board. moves diagonally, down and to the left after each attack.
    def DiagonalLinearAttackStrategy(self):
        coordinateList = []  
        moves = 1

        #calc starting point and make first attack
        startingChar = 'A'
        startingX = chr(ord(startingChar) + random.randint(0, self.board.size - 1))
        startingY = random.randint(0, self.board.size - 1)
        coordinateList.append(functionalComponents.CoordinateString(startingX, startingY))
        self.board.AttackBoard(functionalComponents.CoordinateString(startingX, startingY))
        x = str(startingX)
        y = startingY
        originalTile = self.board.tileList[functionalComponents.CoordinateString(x, y)]

        #loop until all the ships are sunk
        #calculate the next position to attack
        while(not self.board.CheckIfAllShipsSunk()):
            currentTile = self.board.tileList[functionalComponents.CoordinateString(x, y)]

            if(not currentTile.hasWestTile and not currentTile.hasNorthTile):
                x = startingChar
                y += 1
            elif(not currentTile.hasEastTile and not currentTile.hasSouthTile):
                x = startingChar
                y = 0
            elif(not currentTile.hasWestTile and not currentTile.hasSouthTile):
                x = chr(ord(startingChar) + 1)
                y = self.board.size - 1
            elif(not currentTile.hasSouthTile and functionalComponents.MoveCoordinateWest(currentTile.GetCoordiante()) != self.board.emptyTileCode):
                x = chr(ord(startingChar) + y + 1)
                y = self.board.size - 1 
            elif(not currentTile.hasWestTile):
                y = ord(x) - ord(startingChar) + 1
                x = startingChar             
            else:
                x = chr(ord(x) + 1)
                y -= 1


            coordinateList.append(functionalComponents.CoordinateString(x, y))
            self.board.AttackBoard(functionalComponents.CoordinateString(x,y))  
            moves += 1  

        return SimulationResult(self.board.initalTileListState, coordinateList, moves, "Diagonal Linear")  
    
    def DiagonalHitScanAttackStratgy(self):
        coordinateList = []  
        moves = 1

        #calc starting point and make first attack
        startingChar = 'A'
        startingX = chr(ord(startingChar) + random.randint(0, self.board.size - 1))
        startingY = random.randint(0, self.board.size - 1)
        coordinateList.append(functionalComponents.CoordinateString(startingX, startingY))
        self.board.AttackBoard(functionalComponents.CoordinateString(startingX, startingY))
        x = str(startingX)
        y = startingY
        originalTile = self.board.tileList[functionalComponents.CoordinateString(x, y)]
        validCoordinateList = []

        #set all adjacent flags to false until a hit is registered
        checkNorth = False
        checkSouth = False
        checkWest = False
        checkEast = False

        #build a list of all coordinates 
        availableCoordinates = self.board.GetAvailableCoordinateList()

        #loop until all ships are sunk
        while(not self.board.CheckIfAllShipsSunk()):
            #if all check flags are set to false, calc a new random coordinate that is available           
            if(not checkNorth and not checkSouth and not checkWest and not checkEast):
                currentTile = self.board.tileList[functionalComponents.CoordinateString(x,y)]
                if(not currentTile.hasWestTile and not currentTile.hasNorthTile):
                    x = startingChar
                    y += 1
                elif(not currentTile.hasEastTile and not currentTile.hasSouthTile):
                    x = startingChar
                    y = 0
                elif(not currentTile.hasWestTile and not currentTile.hasSouthTile):
                    x = chr(ord(startingChar) + 1)
                    y = self.board.size - 1
                elif(not currentTile.hasSouthTile and functionalComponents.MoveCoordinateWest(currentTile.GetCoordiante()) != self.board.emptyTileCode):
                    x = chr(ord(startingChar) + y + 1)
                    y = self.board.size - 1 
                elif(not currentTile.hasWestTile):
                    y = ord(x) - ord(startingChar) + 1
                    x = startingChar             
                else:
                    x = chr(ord(x) + 1)
                    y -= 1

                currentCoordinate = functionalComponents.CoordinateString(x, y)
                initialCoordinate = currentCoordinate
            elif(checkNorth):
                while(checkNorth):
                    currentCoordinate = functionalComponents.MoveCoordinateNorth(currentCoordinate)

                    #attack with the generated coordinate
                    coordinateList.append(currentCoordinate)
                    availableCoordinates.remove(currentCoordinate)
                    self.board.AttackBoard(currentCoordinate) 
                    checkNorth = self.board.tileList[currentCoordinate].hasNorthTile and functionalComponents.MoveCoordinateNorth(currentCoordinate) in availableCoordinates and self.board.tileList[currentCoordinate].code != self.board.missTileCode
                    moves += 1
            elif(checkSouth):
                 while(checkSouth):
                    currentCoordinate = functionalComponents.MoveCoordinateSouth(currentCoordinate)
                    
                    #attack with the generated coordinate
                    coordinateList.append(currentCoordinate)
                    availableCoordinates.remove(currentCoordinate)
                    self.board.AttackBoard(currentCoordinate)
                    checkSouth = self.board.tileList[currentCoordinate].hasSouthTile and functionalComponents.MoveCoordinateSouth(currentCoordinate) in availableCoordinates and self.board.tileList[currentCoordinate].code != self.board.missTileCode 
                    moves += 1
            elif(checkWest):
                 while(checkWest):
                    currentCoordinate = functionalComponents.MoveCoordinateWest(currentCoordinate)
                    
                    #attack with the generated coordinate
                    coordinateList.append(currentCoordinate)
                    availableCoordinates.remove(currentCoordinate)
                    self.board.AttackBoard(currentCoordinate)  
                    checkWest = self.board.tileList[currentCoordinate].hasWestTile and functionalComponents.MoveCoordinateWest(currentCoordinate) in availableCoordinates and self.board.tileList[currentCoordinate].code != self.board.missTileCode
                    moves += 1
            elif(checkEast):
                while(checkEast):
                    currentCoordinate = functionalComponents.MoveCoordinateEast(currentCoordinate)
                    
                    #attack with the generated coordinate
                    coordinateList.append(currentCoordinate)
                    availableCoordinates.remove(currentCoordinate)
                    self.board.AttackBoard(currentCoordinate)  
                    checkEast = self.board.tileList[currentCoordinate].hasEastTile and functionalComponents.MoveCoordinateEast(currentCoordinate) in availableCoordinates and self.board.tileList[currentCoordinate].code != self.board.missTileCode
                    moves += 1

            #set back to the original coordinate
            currentCoordinate = initialCoordinate

            #adjust check flags to the new coordinate
            checkNorth = self.board.tileList[currentCoordinate].hasNorthTile and functionalComponents.MoveCoordinateNorth(currentCoordinate) in availableCoordinates
            checkSouth = self.board.tileList[currentCoordinate].hasSouthTile and functionalComponents.MoveCoordinateSouth(currentCoordinate) in availableCoordinates
            checkWest = self.board.tileList[currentCoordinate].hasWestTile and functionalComponents.MoveCoordinateWest(currentCoordinate) in availableCoordinates
            checkEast = self.board.tileList[currentCoordinate].hasEastTile and functionalComponents.MoveCoordinateEast(currentCoordinate) in availableCoordinates
            
            #attack with the generated coordinate       
            if(currentCoordinate in availableCoordinates):
                coordinateList.append(currentCoordinate)
                availableCoordinates.remove(currentCoordinate)
                self.board.AttackBoard(currentCoordinate)  
                moves += 1 
                    
        return SimulationResult(self.board.initalTileListState, coordinateList, moves, "Diagonal Hitscan")


