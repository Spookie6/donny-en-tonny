import pygame, sys, time

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from sprites import Pos

class Button:
	def __init__(self, pos, width, height, title, action=None, screen=None) -> None:
		self.pos = pos
		self.width = width
		self.height = height
		self.color = "White"
		self.borderRadius = 50
		self.title = title
		self.action = action
		self.screen = screen
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
					if self.screen:
						self.action(configs, self.screen).run()
					else:
						self.action(configs).run()
				else:
					self.title = "Clicked"
     
		if not (self.rect.collidepoint((mx, my))):
			self.color = "White"
   
class InputBox:
	def __init__(self, pos, width, height, placeholder, constants):
		self.pos = pos
		self.width = width
		self.height = height
		self.placeholder = placeholder
		self.color = "White"
		
		self.active = False
		self.value = ""
  
		self.rect = pygame.Rect(pos.x, pos.y, width, height)
		self.txt_surf = constants.FONT.render(self.value, True, self.color)

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				self.active = True
			else: self.active = False

		if event.type == pygame.KEYDOWN:
			if self.active:
				if event.key == pygame.K_RETURN:
					print(self.value)
					self.value = ""
				elif event.key == pygame.K_BACKSPACE:
					self.value = self.value[:-1]
				else:
					self.value += event.unicode


	def draw(self, screen):
		pass