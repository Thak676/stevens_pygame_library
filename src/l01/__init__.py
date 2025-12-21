
from .funcs import *
from .Image_Rect import Image_Rect
from .global_vars import *
IR = Image_Rect

# Store registered functions
_user_update = None
_window_size = (400, 400)

def game(func):
	"""Decorator to register the game's update function and start the game loop."""
	global _user_update
	_user_update = func
	run()
	return func

def update(func):
	"""Decorator to register the update function without auto-starting."""
	global _user_update
	_user_update = func
	return func

def set_window(x: int, y: int):
	"""Set the window size before running."""
	global _window_size
	_window_size = (x, y)

def run():
	"""Start the game loop."""
	init(_window_size[0], _window_size[1])

	while True:
		process_events()
		if _user_update:
			_user_update()
		update_screen()

