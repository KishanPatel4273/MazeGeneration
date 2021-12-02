from Node import *
import random

class Maze:
    def __init__(self, n, scale):
        self.scale = scale
        self.N = n
        self.graph = [[Node(x, y) for x in range(n)] for y in range(n)]
        self.generateMaze()

    def getNode(self, x, y):
        return self.graph[y][x]

    ## returns [(x1, y2) ... ]
    def getUnvistedNeighbors(self, x, y):
        neighbors = []
        if(0 <= y - 1 <= self.N -1 and (False == self.getNode(x,y-1).isVisted() )): #top
            neighbors.append((x, y -1))
        if(0 <= x + 1 <= self.N -1 and (False == self.getNode(x+1,y).isVisted())): #right
            neighbors.append((x + 1, y))
        if(0 <= y + 1 <= self.N -1 and (False == self.getNode(x,y+1).isVisted())): #bottom
            neighbors.append((x, y + 1))
        if(0 <= x - 1 <= self.N -1 and (False == self.getNode(x-1,y).isVisted())): #left
            neighbors.append((x - 1, y))

        return neighbors
    
    ## A <- index > B
    def connectNodes(self, A, B, indexSideFromA):
        self.getNode(A[0], A[1]).openSide(indexSide = indexSideFromA)
        # 0 --> 2 # 1 --> 3 # 2 --> 0 # 3 --> 1
        # i + 2 mod 4
        self.getNode(B[0], B[1]).openSide(indexSide = (indexSideFromA + 2) % 4 )

    def generateMaze(self):
        self.getNode(0,0).openSide(3) # start
        self.getNode(self.N - 1, self.N - 1).openSide(1) # end

        self.getNode(0,0).vist()
        stack = [(0,0)] # stack of nodes' using (x,y)
        while(len(stack) != 0):
            currNodeLoc = stack.pop() #(x, y)
            neighbors = self.getUnvistedNeighbors(currNodeLoc[0], currNodeLoc[1])# ((x, y) ...)
            if len(neighbors) != 0:
                stack.append(currNodeLoc)
                nextNodeLoc = neighbors[random.randint(0, len(neighbors) - 1)]
                indexFromCurrLoc = (nextNodeLoc[0] - currNodeLoc[0], nextNodeLoc[1] - currNodeLoc[1])
                indexFromCurr = -1
                if(indexFromCurrLoc[0] == 0 and indexFromCurrLoc[1] == -1):
                    indexFromCurr = 0 # above
                if(indexFromCurrLoc[0] == 1 and indexFromCurrLoc[1] == 0):
                    indexFromCurr = 1 # to the right
                if(indexFromCurrLoc[0] == 0 and indexFromCurrLoc[1] == 1):
                    indexFromCurr = 2 # below
                if(indexFromCurrLoc[0] == -1 and indexFromCurrLoc[1] == 0): 
                    indexFromCurr = 3 # to the left
                
                self.connectNodes(currNodeLoc, nextNodeLoc, indexFromCurr)
                self.getNode(nextNodeLoc[0], nextNodeLoc[1]).vist()
                stack.append((nextNodeLoc[0], nextNodeLoc[1]))