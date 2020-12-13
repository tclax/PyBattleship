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
