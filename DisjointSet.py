import random

class DisjointSet:
    def __init__(self, n, m):
        self.rank = {}
        self.parent = {}
        for i in range(n):
            for j in range(m):
                self.rank[(i, j)] = 0
                self.parent[(i, j)] = (i,j)

    def find(self, s):
        if self.parent[s] != s:
            self.parent[s] = self.find(self.parent[s])
        return self.parent[s]

    def union(self, x, y):
        set_x = self.find(x)
        set_y = self.find(y)

        if self.rank[set_x] > self.rank[set_y]:
            self.parent[set_y] = set_x
        elif self.rank[set_y] > self.rank[set_x]:
            self.parent[set_x] = set_y
        else:
            rand_int = random.randint(0, 2)
            if rand_int == 0:
                self.parent[set_y] = set_x
                self.rank[set_x] = self.rank[set_x] + 1
            else:
                self.parent[set_x] = set_y
                self.rank[set_y] = self.rank[set_y] + 1

