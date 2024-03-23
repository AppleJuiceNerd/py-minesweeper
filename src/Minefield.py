from Tile import *

class Minefield:
	def __init__(self, window_size, field_size):
		self.tiles = []
		self.tile_size = window_size / field_size

		# Make Minefield
		for y in range(int(self.tile_size)):
			for x in range(int(self.tile_size)):
				self.tiles.append(
					Tile((x * self.tile_size, y * self.tile_size), (self.tile_size, self.tile_size))
				)
	
	def Tick(self):
		for tile in self.tiles:
			tile.Tick()

	def Draw(self):
		for tile in self.tiles:
			tile.Draw()