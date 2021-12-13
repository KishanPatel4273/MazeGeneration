from Render import *
import numpy as np
from Node import *
from Maze import *

class Screen:
	def __init__(self, x, y, width, height, n, m):
		self.width = width
		self.height = height
		self.render = Render(x, y, width, height, orientationAsCanvis = True)	
		self.N = n
		self.M = m
		self.scale = 50
		self.maze = Maze(self.N, self.M, self.scale)
		print(self.maze)
		self.time = 0

	def tick_screen(self):
		self.time = self.time + 1
		#if(self.time % 5 == 0):
			#self.maze = Maze(self.N, self.scale)

	def render_screen(self, pixels):
		for y in range(self.N):
			for x in range(self.M):
				self.render.draw_node(pixels=pixels, node=self.maze.getNode(y,x))
