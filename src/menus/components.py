import pygame, sys, time

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)
sys.path.append(path)

from data.constants import constants
from data.configs import Configs

# from joinPopup import JoinPopup

class Button:
	def __init__(self, pos, width, height, title, action=None, screen=None, customTextColor=None) -> None:
		self.pos = pos
		self.width = width
		self.height = height
		self.color = constants["BUTTON_INACTIVE"]
		self.title = title
		self.action = action
		self.screen = screen
		self.rect = pygame.Rect(pos.x, pos.y, self.width, self.height)
		self.txtColor = customTextColor or constants["BUTTON_TEXT_COLOR"]
  
	def draw(self, screen):
		posTuple = self.pos.getTuple()
		pygame.draw.rect(screen, self.color, self.rect)

		titleImg = constants["FONT"].render(self.title, False, self.txtColor)
		x, y, w, h = titleImg.get_rect(center=posTuple)
		screen.blit(titleImg, (self.pos.x + (self.width / 2 - w / 2), self.pos.y + (self.height / 2 - h / 2)))

	def checkActive(self, buttonDown, configs):
		mx, my = pygame.mouse.get_pos()
		if (self.rect.collidepoint((mx, my))):
			self.color = constants["BUTTON_ACTIVE"]
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
			self.color = constants["BUTTON_INACTIVE"]
   
class InputBox:
	def __init__(self, pos, width, height, placeholder, customColor=None, customTextColor=None):
		self.configs = Configs()
		self.password = placeholder.lower() == "password"
  
		self.defColor = customColor or constants["INPUTBOX_INACTIVE"]
		self.txtColor = customTextColor or constants["INPUTBOX_TEXT_COLOR"]
		print(self.txtColor)
  
		self.pos = pos
		self.width = width
		self.height = height
		self.placeholder = placeholder
		self.color = self.defColor
		self.active = False
		self.frameCount = 0
		self.animationStatus = 0
		self.value = self.configs.toml_dict[f"server_{self.placeholder.lower()}"] or placeholder
  
		self.charSet = "abcdefghijklmnopqrstuvwxyz0123456789"
		if self.password:
			self.charSet += "!@#$%^&*<>?/~\\"
  
		self.rect = pygame.Rect(pos.x, pos.y, width, height)
		self.txt_surf = constants["FONT"].render("*"*len(self.value) if self.password else self.value, True, self.txtColor)
		self.txt_surf2 = constants["FONT"].render("", True, self.txtColor)

	def handle_event(self, event, mousePos=None):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(mousePos if mousePos else event.pos):
				self.active = True
			else:
				self.active = False
	 
		if not self.active:
				self.frameCount = 0
				self.animationStatus = False
				self.color = self.defColor
				if self.value == "":
					self.value = self.placeholder
		else:
			self.color = constants["INPUTBOX_ACTIVE"]
			if self.value == self.placeholder:
				self.value = ""

		if event.type == pygame.KEYDOWN:
			if self.active:
				if event.key == pygame.K_RETURN:
					self.value = ""
				elif event.key == pygame.K_BACKSPACE:
					self.value = self.value[:-1]
				else:
					Ascii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
					if self.rect[0] + self.rect[2] - 20 <= self.rect[0] + self.txt_surf.get_rect()[2] + 20:
						return
					if event.unicode.lower() not in self.charSet:
						return
					self.value += event.unicode
				self.configs.setValue(f"server_{self.placeholder.lower()}", self.value if self.value != self.placeholder else "")
				self.configs.save()


	def draw(self, screen):
		if self.active:
			self.frameCount += 1
  
		if self.frameCount == 40:
			self.frameCount = 0
			self.animationStatus = not self.animationStatus

		if self.animationStatus == 0:
				self.txt_surf2 = constants["FONT"].render(" ", True, self.txtColor)
		if self.animationStatus == 1:
				self.txt_surf2 = constants["FONT"].render("|", True, self.txtColor)
		self.txt_surf = constants["FONT"].render("*"*len(self.value) if self.password and self.value != self.placeholder else self.value, True, self.txtColor)
	
		posTuple = self.pos.getTuple()
		pygame.draw.rect(screen, self.color, self.rect)
		x, y, w, h = self.txt_surf.get_rect(center=posTuple)
  		
		if self.value == self.placeholder:
			self.txt_surf.set_alpha(100)

		screen.blit(self.txt_surf, (self.rect[0] + 20, self.pos.y + (self.height / 2 - h / 2)))
		screen.blit(self.txt_surf2, (self.rect[0] + self.txt_surf.get_rect()[2] + 20, self.pos.y + (self.height / 2 - h / 2)))
  
class ServerListItem:
	def __init__(self, server, x, y, w, h):
		self.server = server
		self.ip = server["ip"]
		self.name = server["name"]
		self.playerCount = server["playerCount"]
		self.ping = round(server["ping"])
  
		self.rect = pygame.Rect(x, y, w, h)
		self.color = constants["LISTITEM_INACTIVE"]
  
		self.txt_surf_name = constants["FONT"].render(self.name, True, constants["INPUTBOX_TEXT_COLOR"])
		self.txt_surf_playerCount = constants["FONT"].render(f"{self.playerCount}/4", True, constants["INPUTBOX_TEXT_COLOR"])
		self.txt_surf_ping = constants["FONT"].render(f"{self.ping} ms", True, constants["INPUTBOX_TEXT_COLOR"])

	def handleEvent(self, server, screen, action):
		mx, my = pygame.mouse.get_pos()
		if self.rect.collidepoint(mx, my):
			self.color = constants["LISTITEM_ACTIVE"]
			if (pygame.mouse.get_pressed()[0]):
				action(server, screen).run()
		else:
			self.color = constants["LISTITEM_INACTIVE"]
 
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
		screen.blit(self.txt_surf_name, (self.rect[0] + 10, self.rect[1] + 10))
  
		txt_width = self.txt_surf_playerCount.get_rect()[2]
		screen.blit(self.txt_surf_playerCount, (self.rect[0] + self.rect[2] - txt_width - 10, self.rect[1] + 10))
  
		ping_txt_width = self.txt_surf_ping.get_rect()[2]
		screen.blit(self.txt_surf_ping, (self.rect[0] + self.rect[2] - txt_width - ping_txt_width - 30, self.rect[1] + 10))