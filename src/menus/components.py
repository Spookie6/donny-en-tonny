import pygame, sys, time

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from sprites import Pos

class Button:
	def __init__(self, pos, width, height, title, action=None) -> None:
		self.pos = pos
		self.width = width
		self.height = height
		self.title = title
		self.action = action
		self.rect = pygame.Rect(pos.x, pos.y, self.width, self.height)
  
	def draw(self, screen, font):
		posTuple = self.pos.getTuple()
		pygame.draw.rect(screen, "white", self.rect , border_radius=50)

		titleImg = font.render(self.title, True, "Green")
		x, y, w, h = titleImg.get_rect(center=posTuple)
		screen.blit(titleImg, (self.pos.x + (self.width / 2 - w / 2), self.pos.y + (self.height / 2 - h / 2)))

	def checkActive(self, buttonDown, configs):
		mx, my = pygame.mouse.get_pos()
		if buttonDown and self.rect.collidepoint((mx, my)):
			if self.action:
				pygame.time.delay(200)
				self.action(configs).run()
			else:
				self.title = "Clicked"
		

class Header():
	def __init__(self) -> None:
		pass