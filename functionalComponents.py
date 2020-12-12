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