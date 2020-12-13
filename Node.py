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
