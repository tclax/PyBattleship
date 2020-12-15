#Functions
def CoordinateString(x,y):
    return str(x)+","+str(y)

def MoveCoordinateNorth(coordinateString):
    splitCoordinate = coordinateString.split(',')
    x = coordinateString.split(',')[0]
    y = coordinateString.split(',')[1]

    northCoordinate = CoordinateString(chr(ord(x) - 1), y)
    return northCoordinate

def MoveCoordinateSouth(coordinateString):
    splitCoordinate = coordinateString.split(',')
    x = coordinateString.split(',')[0]
    y = coordinateString.split(',')[1]

    southCoordindate = CoordinateString(chr(ord(x) + 1), y)
    return southCoordindate

def MoveCoordinateWest(coordinateString):
    splitCoordinate = coordinateString.split(',')
    x = coordinateString.split(',')[0]
    y = coordinateString.split(',')[1]

    westCoordinate = CoordinateString(x, int(y) - 1)
    return westCoordinate

def MoveCoordinateEast(coordinateString):
    splitCoordinate = coordinateString.split(',')
    x = coordinateString.split(',')[0]
    y = coordinateString.split(',')[1]

    eastCoordinate = CoordinateString(x, int(y) + 1)
    return eastCoordinate

def MoveCoordinateDiagonal(coordinateString, board):
    startingChar = 'A'
    currentTile = board.tileList[coordinateString]
    x = currentTile.x
    y = currentTile.y

    if(not currentTile.hasWestTile and not currentTile.hasNorthTile):
        x = startingChar
        y += 1
    elif(not currentTile.hasEastTile and not currentTile.hasSouthTile):
        x = startingChar
        y = 0
    elif(not currentTile.hasWestTile and not currentTile.hasSouthTile):
        x = chr(ord(startingChar) + 1)
        y = board.size - 1
    elif(not currentTile.hasSouthTile and MoveCoordinateWest(currentTile.GetCoordiante()) != board.emptyTileCode):
        x = chr(ord(startingChar) + y + 1)
        y = board.size - 1 
    elif(not currentTile.hasWestTile):
        y = ord(x) - ord(startingChar) + 1
        x = startingChar             
    else:
        x = chr(ord(x) + 1)
        y -= 1
    
    return CoordinateString(x,y)