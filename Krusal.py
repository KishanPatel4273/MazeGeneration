class Kruskal:

    def __init__(self, n, m, graph):
        self.n = n
        self.m = m
        self.graph = graph
        self.nodes, self.edges = self.initial_grid()
        self.maze_object = self.kruskal_maze()
