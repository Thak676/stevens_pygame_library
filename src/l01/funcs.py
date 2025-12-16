
import pygame
import sys
from . import global_vars

def init(x: int, y: int) -> None:
	pygame.init()
	global_vars.screen = pygame.display.set_mode((x, y))
	global_vars.clock = pygame.time.Clock()
	
def quit():
	pygame.quit()
	sys.exit()

def fill_screen(r: int, g: int, b: int):
	global_vars.screen.fill((r, g, b))

def update_screen():
	pygame.display.update()
	global_vars.clock.tick(60)

