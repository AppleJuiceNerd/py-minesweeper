from pyray import KeyboardKey


class WindowSettings:
	Size = 400  # Window size will always be 1:1

class GameSettings:
	Controls = {
		"open_cell": "LMB",
		"flag_cell": "RMB",
		"chord": "LMB+RMB",
		"question_mark_toggle": False
	}

class Settings:
	def __init__(self):
		pass