
Allows for simple code like the following (you need to supply your own image):

import pygame
from l01 import *
from pygame.locals import *

initialize(640, 640)

cloud = Image_Rect("images/clouds/cloud_1.png", 100, 100)

while True:
        fill_screen((19, 214, 248))
        cloud.draw()
        for event in pygame.event.get():
                if event.type == QUIT:
                        quit()
        update_screen()

