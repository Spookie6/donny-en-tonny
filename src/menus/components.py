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
		self.color = "White"
		self.borderRadius = 50
		self.title = title
		self.action = action
		self.rect = pygame.Rect(pos.x, pos.y, self.width, self.height)
  
	def draw(self, screen, font):
		posTuple = self.pos.getTuple()
		pygame.draw.rect(screen, self.color, self.rect)

		titleImg = font.render(self.title, False, "Blue")
		x, y, w, h = titleImg.get_rect(center=posTuple)
		screen.blit(titleImg, (self.pos.x + (self.width / 2 - w / 2), self.pos.y + (self.height / 2 - h / 2)))

	def checkActive(self, buttonDown, configs):
		mx, my = pygame.mouse.get_pos()
		if (self.rect.collidepoint((mx, my))):
			self.color = "Green"
			if buttonDown:
				if self.action:
					pygame.time.delay(200)
					self.action(configs).run()
				else:
					self.title = "Clicked"
		if not (self.rect.collidepoint((mx, my))):
			self.color = "White"
    
	def rescale(self, originalScaleTuple, configs):
		w, h = configs.toml_dict['resolution']

		self.width = int(w/1920) * self.width
		self.height = int(h/1080) * self.height
		self.pos.x = w / 2 - self.width / 2
		self.pos.y = h / 2 - self.height / 2
		self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)

class Header():
	def __init__(self) -> None:
		pass