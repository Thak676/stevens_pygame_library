
Only tested in wsl.

Allows for simple code like the following:

import pygame
from l01 import *
from pygame.locals import *

init(640, 640)

while True:
        fill_screen(19, 214, 248)
        for event in pygame.event.get():
                if event.type == QUIT:
                        quit()
        update_screen()

