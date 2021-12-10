class DisjointSet:
    def __init__(self, n, m):
        self.rank = {}
        self.parent = {}
        for i in range(n):
            for j in range(m):
                self.rank[(i, j)] = 0
                self.parent[(i, j)] = (i, j)
    
    def find(self, s):
        if self.parent[s] != s:
            self.parent[s] = self.find(self.parent[s])
        return self.parent[s]
    
    def union(self, s1, s2):
        set_1 = self.find(s1)
        set_2 = self.find(s2)
        if self.rank[set_1] > self.rank[set_2]:
            self.parent[set_2] = set_1
        elif self.rank[set_2] > self.rank[set_1]:
            self.parent[set_1] = set_2
        else:
            r = random.randint(2)
            if r == 0:
                self.parent[set_2] = set_1
                self.rank[set_1] = self.rankk[set_1] + 1
            else:
                self.parent[set_1] = set_2
                self.rank[set_2] = self.rank[set_2] + 1