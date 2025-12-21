
from .funcs import *
from .Image_Rect import Image_Rect
from .global_vars import *
IR = Image_Rect

import inspect

def run(width, height):
    init(width, height)
    
    # Get the caller's global namespace
    frame = inspect.currentframe().f_back
    user_globals = frame.f_globals
    
    # Look for their update() function
    user_update = user_globals.get('update')
    
    while True:
        process_events()
        if user_update:
            user_update()
        update_screen()

