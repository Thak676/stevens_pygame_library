
import pygame
from . import global_vars

class Image_Rect:

	def __init__(self, file_path: str, x: int, y: int):
		self.img: pygame.Surface = pygame.image.load(file_path)
		self.img.set_colorkey((0, 0, 0))
		self.x = x
		self.y = y

	@property
	def pos(self) -> tuple[int, int]:
		return (self.x, self.y)

	@pos.setter
	def pos(self, value: tuple[int, int]):
		self.x, self.y = value

	def draw(self):
		global_vars.screen.blit(self.img, self.pos)

