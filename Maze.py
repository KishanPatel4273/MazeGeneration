from krusal import Kruskal
import random

class Maze:
    def __init__(self, n, scale):
        self.scale = scale
        self.N = n
        self.graph = Kruskal(n, n)