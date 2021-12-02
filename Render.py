import math

class Render:
	def __init__(self, x, y, width, height, orientationAsCanvis = False):
		self.width = width
		self.height = height
		self.x = x
		self.y = y
		self.orientationAsCanvis = orientationAsCanvis
		self.minX = int(self.x - width/2)
		self.maxX = int(self.x + width/2)
		self.minY = int(self.y - height/2)
		self.maxY = int(self.y + height/2)

	def plot_pixel(self, pixels, x, y, color, thickness = 1):
		if thickness != 1:
			self.fill_circle(pixels, x, y, thickness, color)
		if self.orientationAsCanvis:
			y = int(y + self.y)
		else:
			y = int(self.height - (y + self.y))

		x = int(x + self.x)
		if thickness == 1 and 0 <= x and x < self.width and 0 <= y and y < self.height:
			pixels[x,y] = color

	def plot_vector_pixel(self, pixels, v, color):
		self.plot_pixel(pixels, v.getX(), v.getY(), color)

	def draw_line(self, pixels, x1, y1, x2, y2, color, thickness = 1):
		dx = x2 - x1
		dy = y2 - y1
		min_y =  min(int(y1),int(y2))
		max_y = max(int(y1),int(y2)) + 1
		if dx == 0:
			for y in range(min_y, max_y):
				self.plot_pixel(pixels, x1, y, color, thickness)
			return
		min_x =  min(int(x1),int(x2))
		max_x = max(int(x1),int(x2))+1
		if dy == 0:
			for x in range(min_x, max_x):
				self.plot_pixel(pixels, x, y1, color, thickness)
			return
		slope = dy / dx
		if x1 < self.minX: x1 == self.minX
		if x2 < self.minX: x2 == self.minX
		if y1 < self.minY: y1 == self.minY
		if y2 < self.minY: y2 == self.minY
		if x1 >= self.maxX: x1 == self.maxX - 1
		if x2 >= self.maxX: x2 == self.maxX - 1
		if y1 >= self.maxY: y1 == self.maxY - 1
		if y2 >= self.maxY: y2 == self.maxY - 1
		if abs(slope) > 1:
			for y in range(min_y, max_y):
				x = int((y - y1) / slope + x1)  
				self.plot_pixel(pixels, x, y, color, thickness)
		else:
			for x in range(min_x, max_x):
				y = int(slope * (x - x1) + y1)
				self.plot_pixel(pixels, x, y, color, thickness)

	def draw_node(self, pixels, node, scale = 50):
		color = 255
		if node.getTop():
			self.draw_line(pixels, node.getX() * scale, node.getY() * scale, node.getX() * scale + scale, node.getY() * scale, color)
		if node.getRight():
			self.draw_line(pixels, (node.getX() * scale) + scale, node.getY() * scale, (node.getX() * scale) + scale, (node.getY() * scale) + scale, color)
		if node.getBottom():
			self.draw_line(pixels, node.getX() * scale, node.getY() * scale + scale, node.getX() * scale + scale, node.getY() * scale + scale, color)
		if node.getLeft():
			self.draw_line(pixels, node.getX() * scale, node.getY() * scale, node.getX() * scale, (node.getY() * scale) + scale, color)

