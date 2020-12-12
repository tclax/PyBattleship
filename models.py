import random, copy, functionalComponents

#Represents a node that contains a value and another node connection for the cardinal directions North, South, East, West
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.northNode = None
        self.southNode = None
        self.westNode = None
        self.eastNode = None
    
    def HasNorthNode(self):
        return self.northNode != None
    
    def HasSouthNode(self):
        return self.southNode != None
    
    def HasWestNode(self):
        return self.westNode != None
    
    def HasEastNode(self):
        return self.eastNode != None
    
    def PrintNodeValue(self):
        print(self.dataval)
    
    def PrintNeighborNodeValues(self):
        print('North: ' + self.northNode.dataval)
        print('South: ' + self.southNode.dataval)
        print('West: ' + self.westNode.dataval)
        print('East: ' + self.eastNode.dataval)

#Represents a tile. A tile has am x,y  coordinate, and a code value
class Tile:
    def __init__(self, x, y, code):
        self.x = x
        self.y = y
        self.code = code
        self.hasNorthTile = False
        self.hasSouthTile = False
        self.hasWestTile = False
        self.hasEastTile = False
    
    
    def PrintCoordinate(self):
        print('(' + str(self.x) + ',' + str(self.y) + ')')

    def GetCoordiante(self):
        return str(self.x) + ',' + str(self.y)

    def GetCoordianteString(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
#Represents a collection of Nodes that will act as the Battleship board
class Board:
    def __init__(self, size):
        self.tileList = {}
        self.initalTileListState = {}
        self.emptyTileCode = '*'
        self.hitTileCode = 'X'
        self.missTileCode = 'o'
        self.size = size
        self.hitCounter = 0
        self.shipTileCount = 0
        self.shipCodesAppendedString = ''

        #initialize the tiles to their x y and code values.
        startingChar = 'A'
        for x in range(0, self.size):
            for y in range (0, self.size):
                #initialize the tile
                coordinateString = functionalComponents.CoordinateString(chr(ord(startingChar) + x), y)
                self.tileList[coordinateString]  = (Tile(chr(ord(startingChar) + x), y,self.emptyTileCode))

                #link the tiles to their cardinal nodes
                #if x is 0, tile cannot be linked to north tiles
                self.tileList[coordinateString].hasNorthTile = (x != 0)
                #if y is 0, tile cannot be linked to west tiles
                self.tileList[coordinateString].hasWestTile = (y != 0)
                #if y is the size of the board, tile cannot be linked to east tiles
                self.tileList[coordinateString].hasEastTile = (y < self.size - 1)
                #if x is the size of the board, the tile cannot be linked to south tiles
                self.tileList[coordinateString].hasSouthTile = (x < self.size - 1)
        
    
    def PrintBoard(self):
        #Print the x index
        startingChar = 'A'
        print(' ', end=' ')
        for x in range(0, self.size):
            print(str(x), end='  ')
        print()
        for x in range(0, self.size):
            print(chr(ord(startingChar) + x), end=' ')
            for y in range(0, self.size):
                print(self.tileList[functionalComponents.CoordinateString(chr(ord(startingChar) + x), y)].code, end='  ')
            print()

    def PrintBoardCoordinates(self):
        #Print the x index
        startingChar = 'A'
        print('  ', end=' ')
        for x in range(0, self.size):
            print(str(x), end='    ')
        print()
        for x in range(0, self.size):
            print(chr(ord(startingChar) + x), end=' ')
            for y in range(0, self.size):
                print(functionalComponents.CoordinateString(chr(ord(startingChar) + x), y), end='  ')
            print()
    

    #Directs the user to place a ship by first selecting a starting cooridnate, and then finding all valid directions is can be placed. 
    def PlaceShipAtRandomCoordinate(self, ship):
        self.shipCodesAppendedString += ship.code
        ascii_letters_row = 'A'
        startingChar = 'A'
        for x in range(1, self.size):
            ascii_letters_row = ascii_letters_row + chr(ord(startingChar) + x)

        #Main loop of the method. Allows a user to enter valid coordinates and select a valid direction to place the boat
        while True:
            #Get position
            x = 'a'
            y = -1
            while True:
                x = random.choice(ascii_letters_row)
                y = random.randint(0, ship.length)
                if(functionalComponents.CoordinateString(x,y) in self.tileList and self.tileList[functionalComponents.CoordinateString(x,y)].code == self.emptyTileCode):
                    break

            #Using the starting point, find if there is a valid placement of the ship size in the following directions: North, South, West, East
            validCoordinatesDict = {}

            #Check North
            northCoordinateList = []
            for i in range(0, ship.length):
                changeCoordinate = chr(ord(x) - i)
                if(functionalComponents.CoordinateString(changeCoordinate,y) in self.tileList and self.tileList[functionalComponents.CoordinateString(changeCoordinate,y)].code == self.emptyTileCode):
                    northCoordinateList.append(self.tileList[functionalComponents.CoordinateString(changeCoordinate,y)])
                else:
                    northCoordinateList = []
                    break           
            #Add to the dictionary of valid moves
            if len(northCoordinateList) == ship.length:
                validCoordinatesDict['North'] = northCoordinateList

            #Check South
            southCoordinateList = []
            for i in range(0, ship.length):
                changeCoordinate = chr(ord(x) + i)
                if(functionalComponents.CoordinateString(changeCoordinate,y) in self.tileList and self.tileList[functionalComponents.CoordinateString(changeCoordinate,y)].code == self.emptyTileCode):
                    southCoordinateList.append(self.tileList[functionalComponents.CoordinateString(changeCoordinate,y)])
                else:
                    southCoordinateList = []
                    break           
            #Add to the dictionary of valid moves
            if len(southCoordinateList) == ship.length:
                validCoordinatesDict['South'] = southCoordinateList
            
            #Check West
            westCoordinateList = []
            for i in range(0, ship.length):
                changeCoordinate = y - i
                if(functionalComponents.CoordinateString(x,changeCoordinate) in self.tileList and self.tileList[functionalComponents.CoordinateString(x,changeCoordinate)].code == self.emptyTileCode):
                    westCoordinateList.append(self.tileList[functionalComponents.CoordinateString(x,changeCoordinate)])
                else:
                    westCoordinateList = []
                    break            
            #Add to the dictionary of valid moves
            if len(westCoordinateList) == ship.length:
                validCoordinatesDict['West'] = westCoordinateList
            
            #Check East
            eastCoordinateList = []
            for i in range(0, ship.length):
                changeCoordinate = y + i
                if(functionalComponents.CoordinateString(x,changeCoordinate) in self.tileList and self.tileList[functionalComponents.CoordinateString(x,changeCoordinate)].code == self.emptyTileCode):
                    eastCoordinateList.append(self.tileList[functionalComponents.CoordinateString(x,changeCoordinate)])
                else:
                    eastCoordinateList = []
                    break           
            #Add to the dictionary of valid moves
            if len(eastCoordinateList) == ship.length:
                validCoordinatesDict['East'] = eastCoordinateList
           
            #Allow the computer to randomly generate a direction they want to place the ship
            if len(validCoordinatesDict) > 0:
                selectionIndex = 0
                selectionDict = []           
                for key, value in validCoordinatesDict.items():
                    selectionDict.append(key)
                    selectionIndex = selectionIndex + 1
                userSelection = random.randint(0, selectionIndex-1)

                #Apply the ship code to the cooridnates selected
                direction = selectionDict[userSelection]
                directionCoordinates = validCoordinatesDict[direction]
                for i in range(0, len(directionCoordinates)):
                    self.tileList[directionCoordinates[i].GetCoordiante()].code = ship.code
                    self.shipTileCount += 1                   

                #Kills main loop
                break

    def PlaceShip(self, ship):
        raise NameError('Use random placement instead')
        #Main loop of the method. Allows a user to enter valid coordinates and select a valid direction to place the boat
        while True:
            #Get position
            x = 'a'
            y = -1
            while True:
                print('Enter a starting coordinate for the ship:')
                x = input('Enter x coordinate: ')
                y = input('Enter y coordinate: ')
                if(functionalComponents.CoordinateString(x,y) in self.tileList and self.tileList[functionalComponents.CoordinateString(x,y)].code == self.emptyTileCode):
                    break
            y = int(y)

            #Using the starting point, find if there is a valid placement of the ship size in the following directions: North, South, West, East
            validCoordinatesDict = {}

            #Check North
            northCoordinateList = []
            for i in range(0, ship.length):
                changeCoordinate = chr(ord(x) - i)
                if(functionalComponents.CoordinateString(changeCoordinate,y) in self.tileList and self.tileList[functionalComponents.CoordinateString(changeCoordinate,y)].code == self.emptyTileCode):
                    northCoordinateList.append(self.tileList[functionalComponents.CoordinateString(changeCoordinate,y)])
                else:
                    northCoordinateList = []
                    break           
            #Add to the dictionary of valid moves
            if len(northCoordinateList) == ship.length:
                validCoordinatesDict['North'] = northCoordinateList

            #Check South
            southCoordinateList = []
            for i in range(0, ship.length):
                changeCoordinate = chr(ord(x) + i)
                if(functionalComponents.CoordinateString(changeCoordinate,y) in self.tileList and self.tileList[functionalComponents.CoordinateString(changeCoordinate,y)].code == self.emptyTileCode):
                    southCoordinateList.append(self.tileList[functionalComponents.CoordinateString(changeCoordinate,y)])
                else:
                    southCoordinateList = []
                    break           
            #Add to the dictionary of valid moves
            if len(southCoordinateList) == ship.length:
                validCoordinatesDict['South'] = southCoordinateList
            
            #Check West
            westCoordinateList = []
            for i in range(0, ship.length):
                changeCoordinate = y - i
                if(functionalComponents.CoordinateString(x,changeCoordinate) in self.tileList and self.tileList[functionalComponents.CoordinateString(x,changeCoordinate)].code == self.emptyTileCode):
                    westCoordinateList.append(self.tileList[functionalComponents.CoordinateString(x,changeCoordinate)])
                else:
                    westCoordinateList = []
                    break            
            #Add to the dictionary of valid moves
            if len(westCoordinateList) == ship.length:
                validCoordinatesDict['West'] = westCoordinateList
            
            #Check East
            eastCoordinateList = []
            for i in range(0, ship.length):
                changeCoordinate = y + i
                if(functionalComponents.CoordinateString(x,changeCoordinate) in self.tileList and self.tileList[functionalComponents.CoordinateString(x,changeCoordinate)].code == self.emptyTileCode):
                    eastCoordinateList.append(self.tileList[functionalComponents.CoordinateString(x,changeCoordinate)])
                else:
                    eastCoordinateList = []
                    break           
            #Add to the dictionary of valid moves
            if len(eastCoordinateList) == ship.length:
                validCoordinatesDict['East'] = eastCoordinateList
           
            #Allow the user to select a direction they want to place the ship in or allow them to enter a new starting point
            if len(validCoordinatesDict) > 0:
                self.PrintBoard()
                selectionIndex = 0
                selectionDict = []           
                for key, value in validCoordinatesDict.items():
                    selectionDict.append(key)
                    print(str(selectionIndex) + '. ' + key, end=' ')
                    for i in range(0, len(value)):
                        print(value[i].GetCoordianteString(), end=' ')
                    print()
                    selectionIndex = selectionIndex + 1
                print(str(selectionIndex) + '. Enter a new starting coordinate')
                userSelection = input('Select a direction to place the ship: ')
                userSelection = int(userSelection)
                #Only allow answers above
                while True:
                    if userSelection == selectionIndex:
                        break
                    elif userSelection <= selectionIndex and userSelection >= 0:
                        #Apply the ship code to the cooridnates selected
                        direction = selectionDict[userSelection]
                        print(direction)
                        directionCoordinates = validCoordinatesDict[direction]
                        for i in range(0, len(directionCoordinates)):
                            print(directionCoordinates[i].GetCoordianteString())
                            self.tileList[directionCoordinates[i].GetCoordiante()].code = ship.code
                        break
                    userSelection = input('Select a direction to place the ship: ')
                    userSelection = int(userSelection)

                #Kills main loop
                break
            
    def ImportBoard(self, coordinateList):
        raise NameError('Not implemented')
    
    def CheckIfAllShipsSunk(self):
        return self.shipTileCount == self.hitCounter

    #Represents an attack on the board. If there is is a ship code at the position a hit is recorded and changes that tile to a hit. A miss will change tile to a miss.
    def AttackBoard(self, coordinateString):
        if(self.tileList[coordinateString].code in self.shipCodesAppendedString):
            self.hitCounter += 1
            self.tileList[coordinateString].code = self.hitTileCode
        else:
            self.tileList[coordinateString].code = self.missTileCode
    
    #Returns a list of all coordinates that are empty.
    def GetAvailableCoordinateList(self):
        availableCoordinateList = []
        startingChar = 'A'
        for x in range(0, self.size):
            for y in range(0, self.size):
                availableCoordinateList.append(functionalComponents.CoordinateString(chr(ord(startingChar) + x), y))

        return availableCoordinateList

    #Sets the board tile back to their original state
    def ResetBoard(self):
        self.tileList = copy.deepcopy(self.initalTileListState)
        self.hitCounter = 0
    

    

#Represents a single ship. Ships have a unique code to display on a Board.       
class Ship:
    def __init__(self, length, code):
        self.length = length
        self.code = code
        self.coordinateDict = {}
    
    def ContainsCoordinate(self, x, y):
        return self.coordinateList.contains   
    

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
            simulationResult = self.HitScanAttackStrategy()
            self.simulationResuts[simulationResult.attackStrategy+'#'+str(x)] = simulationResult
            self.board.ResetBoard()
            
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
    def HitScanAttackStrategy(self):
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
        
        return SimulationResult(self.board.initalTileListState, coordinateList, moves, "Hitscan")
     
class SimulationResult:
    def __init__(self, initialTileList, coordinateList, moves, attackStrategy):
        self.initialTileList = initialTileList
        self.coordinateList = coordinateList
        self.moves = moves
        self.attackStrategy = attackStrategy
    
    def SimulationResultString(self):
        return self.attackStrategy + ' completed in ' + str(self.moves) + ' moves'
           
    

    