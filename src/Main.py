from pyray import *

from Minefield import *


class Game:
	def __init__(self):
		init_window(500, 500, "Minesweeper")

		self.field = Minefield(500, 15)

	def Tick(self):
		self.field.Tick()

	def Draw(self):
		self.field.Draw()

	def Run(self):
		while not window_should_close():
			self.Tick()

			begin_drawing()
			clear_background(GRAY)

			self.Draw()

			end_drawing()


if __name__ == "__main__":
	Minesweeper = Game()
	Minesweeper.Run()