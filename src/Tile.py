from pyray import *

class Tile:
	def __init__(self, position, size):
		self.rect = Rectangle(
			position[0],
			position[1],
			size[0],
			size[1]
		)
		self.Mine = False
		
		
	
	def Tick(self):
		pass

	def Draw(self):
		pass