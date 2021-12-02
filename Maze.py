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

    def getUnvistedNeighbors(self, x, y):
        neighbors = []
        if 0 <= y - 1 < self.N and not self.getNode(x,y-1).isVisted():
            neighbors.append((x, y -1))
        if 0 <= x + 1 < self.N and not self.getNode(x+1,y).isVisted():
            neighbors.append((x + 1, y))
        if 0 <= y + 1 < self.N and not self.getNode(x,y+1).isVisted():
            neighbors.append((x, y + 1))
        if 0 <= x - 1 < self.N and not self.getNode(x-1,y).isVisted():
            neighbors.append((x - 1, y))

        return neighbors
    
    def connectNodes(self, A, B, indexSideFromA):
        self.getNode(A[0], A[1]).openSide(indexSide = indexSideFromA)
        self.getNode(B[0], B[1]).openSide(indexSide = (indexSideFromA + 2) % 4 )

    def generateMaze(self):
        self.getNode(0,0).openSide(3)
        self.getNode(self.N - 1, self.N - 1).openSide(1)

        self.getNode(0,0).vist()
        stack = [(0,0)]
        while len(stack):
            currNodeLoc = stack.pop()
            neighbors = self.getUnvistedNeighbors(currNodeLoc[0], currNodeLoc[1])
            if len(neighbors):
                stack.append(currNodeLoc)
                nextNodeLoc = neighbors[random.randint(0, len(neighbors) - 1)]
                indexFromCurrLoc = (nextNodeLoc[0] - currNodeLoc[0], nextNodeLoc[1] - currNodeLoc[1])
                indexFromCurr = -1
                if indexFromCurrLoc[0] == 0 and indexFromCurrLoc[1] == -1:
                    indexFromCurr = 0
                if indexFromCurrLoc[0] == 1 and indexFromCurrLoc[1] == 0:
                    indexFromCurr = 1
                if indexFromCurrLoc[0] == 0 and indexFromCurrLoc[1] == 1:
                    indexFromCurr = 2
                if indexFromCurrLoc[0] == -1 and indexFromCurrLoc[1] == 0:
                    indexFromCurr = 3
                
                self.connectNodes(currNodeLoc, nextNodeLoc, indexFromCurr)
                self.getNode(nextNodeLoc[0], nextNodeLoc[1]).vist()
                stack.append((nextNodeLoc[0], nextNodeLoc[1]))