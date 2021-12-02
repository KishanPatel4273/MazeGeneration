
class Node:
    def __init__(self, x, y):
        #index value no scale
        self.x = x
        self.y = y
                            #Top  Right Bottom Left
        self.sideIsClosed = [True, True, True, True]
        self.isVistedValue = False

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def isVisted(self):
        return self.isVistedValue

    def vist(self):
        self.isVistedValue = True

    def openSide(self, indexSide):
        self.sideIsClosed[indexSide] = False

    def setSideOpened(self, index_side):
        self.sideIsClosed[index_side] = False

    def getTop(self):
        return self.sideIsClosed[0]

    def getRight(self):
        return self.sideIsClosed[1]

    def getBottom(self):
        return self.sideIsClosed[2]

    def getLeft(self):
        return self.sideIsClosed[3]
