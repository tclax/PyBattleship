from Tile import Tile
import functionalComponents
import random, copy

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
    
