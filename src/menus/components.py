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
		screen.blit(titleImg, (self.pos.x + (self.width / 2 - titleRect[2] / 2), self.pos.y + (self.height / 2 - titleRect[3] / 2)))

	def checkActive(self, buttonDown):
		mousePos = pygame.mouse.get_pos()
		if buttonDown:
			if mousePos[0] in range(self.pos.x, self.pos.x + self.width) and mousePos[1] in range(self.pos.y, self.pos.y + self.height):
				self.title = "clicked!"
		

class Header():
	def __init__(self) -> None:
		pass