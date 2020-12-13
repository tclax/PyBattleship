#Represents a single ship. Ships have a unique code to display on a Board.       
class Ship:
    def __init__(self, length, code):
        self.length = length
        self.code = code
        self.coordinateDict = {}
    
    def ContainsCoordinate(self, x, y):
        return self.coordinateList.contains   
