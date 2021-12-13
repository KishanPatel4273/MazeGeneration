from Node import *
import random
from DisjointSet import DisjointSet

class Maze:
    def __init__(self, n, m, scale):
        self.scale = scale
        self.n = n
        self.m = m
        self.graph = [[Node(x, y) for x in range(self.m)] for y in range(self.n)]
        self.generateMaze()
    
    def __str__(self):
        s = str(self.m) + " " + str(self.n) + "\n"
        for i in range(self.n):
            for j in range(self.m):
                s += chr(sum([0 if self.graph[i][j].sideIsClosed[k] else 1 * k**2 for k in range(4)]) + ord('a')) + "\n"
        return s

    def getNode(self, x, y):
        return self.graph[x][y]
    
    def connectNodes(self, A, B, indexSideFromA):
        self.getNode(A[0], A[1]).openSide(indexSide = indexSideFromA)
        self.getNode(B[0], B[1]).openSide(indexSide = (indexSideFromA + 2) % 4 )

    def get_edge_weight_dict(self):
        edges = set()
        for i in range(self.n):
            for j in range(self.m):
                if i > 0:
                    edges.add(((i, j), (i - 1, j)))
                if i < self.n - 1:
                    edges.add(((i, j), (i + 1, j)))
                if j > 0:
                    edges.add(((i, j), (i , j - 1)))
                if j < self.m - 1:
                    edges.add(((i, j), (i, j + 1)))
        edge_weights = {}
        for edge in edges:
            edge_weights[edge] = random.randint(0, 10)
        return dict(sorted(edge_weights.items(), key=lambda x:x[1]))
    
    def mark_walls_deleted(self, x1, y1, x2, y2):
        c1 = self.graph[x1][y1]
        c2 = self.graph[x2][y2]
        if x1 == x2:
            if y1 > y2:
                c1.sideIsClosed[3] = False
                c2.sideIsClosed[1] = False
            elif y2 > y1:
                c1.sideIsClosed[1] = False
                c2.sideIsClosed[3] = False
        if y1 == y2:
            if x1 > x2:
                c1.sideIsClosed[0] = False
                c2.sideIsClosed[2] = False
            elif x2 > x1:
                c1.sideIsClosed[2] = False
                c2.sideIsClosed[0] = False

    def generateMaze(self):
        self.getNode(0,0).openSide(3)
        self.getNode(self.n - 1, self.m - 1).openSide(1)

        minimum_spanning_tree = set()
        disjoint_set = DisjointSet(self.n, self.m)
        sorted_edge_weight_dic = self.get_edge_weight_dict()
        for ((x,y), weight) in sorted_edge_weight_dic.items():
            if x != y:
                if disjoint_set.find(x) != disjoint_set.find(y):
                    minimum_spanning_tree.add((x, y))
                    self.mark_walls_deleted(x[0], x[1], y[0], y[1])
                    disjoint_set.union(x, y)