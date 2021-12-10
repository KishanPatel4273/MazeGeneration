from disjoint_set import DisjointSet
from Node import Node

class Kruskal:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.cell_dict = dict()
        self.nodes, self.edges = self.initialize_grid()
        self.maze_object = self.kruskal()

    def initialize_grid(self):
        nodes = set()
        edges = set()
        for i in range(self.m):
            for j in range(self.n):
                nodes.add((i, j))
                if i == 0 and j == 0:
                    self.cell_dict[(i, j)] = Node(1,1,1,0)
                elif i == self.m - 1 and j == self.n - 1:
                    self.cell_dict[(i, j)] = Node(1,0,1,1)
                else:
                    self.cell_dict[(i, j)] = Node(1,1,1,1)

                if i > 0:
                    edge_1 = (i - 1, j)
                    edges.add(((i, j), edge_1))
                if i < self.m - 1:
                    edge_2 = (i + 1, j)
                    edges.add(((i, j), edge_2))
                if j > 0:
                    edge_3 = (i , j - 1)
                    edges.add(((i, j), edge_3))
                if j < self.n - 1:
                    edge_4 = (i, j + 1)
                    edges.add(((i, j), edge_4))
        return nodes, edges

    def assign_random_edge_weights(self):
        edge_weight_dic = {}
        for edge in self.edges:
            random_weight = int(random.random()*11)
            edge_weight_dic[edge] = random_weight
        return edge_weight_dic
    
    def mark_walls_deleted(self, v1, v2):
        Cell1 = self.cell_dict[v1]
        Cell2 = self.cell_dict[v2]
        x1, y1 = v1 
        x2, y2 = v2
        if x1 == x2:
            if y1 > y2:
                Cell1.left = 0
                Cell2.right = 0
            elif y2 > y1: 
                Cell1.right = 0
                Cell2.left = 0
        if y1 == y2:
            if x1 > x2:
                Cell1.top = 0
                Cell2.bottom = 0
            elif x2 > x1: 
                Cell1.bottom = 0
                Cell2.top = 0

    def kruskal(self):
        edge_weight_dic = self.assign_random_edge_weights()
        min_spanning_tree = set()
        disjoint_set = DisjointSet(self.m, self.n)
        sorted_edge_weight_dic = dict(sorted(edge_weight_dic.items(), key=lambda item:item[1]))
        for ((x,y), weight) in sorted_edge_weight_dic.items():
            if x != y:
                if disjoint_set.find_set(x) != disjoint_set.find_set(y):
                    min_spanning_tree.add((x, y))
                    self.mark_walls_deleted(x,y)
                    disjoint_set.union(x, y)
        return min_spanning_tree
        