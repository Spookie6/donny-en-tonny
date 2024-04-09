import pygame, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from sprites import Pos

class Button():
	def __init__(self, pos, width, height, title) -> None:
		self.pos = pos
		self.width = width
		self.height = height
		self.title = title
	def draw(self, screen, font):
		posTuple = self.pos.getTuple()
		pygame.draw.rect(screen, "white", pygame.Rect(posTuple[0], posTuple[1], self.width, self.height) , border_radius=50)

		titleImg = font.render(self.title, True, "Green")
		titleRect = titleImg.get_rect(center=posTuple)
		print(posTuple)
		screen.blit(titleImg, titleRect)
		

class Header():
	def __init__(self) -> None:
		pass