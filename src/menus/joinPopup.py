import pygame, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

# Import components
from components import Button, InputBox
from sprites import Pos

# Import data
from data.configs import Configs
from data.constants import constants

class JoinPopup:
	# # CONSTANT GAME VARIABLES
	FPS:int = constants["FPS"]
	def __init__(self, server, screen) -> None:
		# Menu VARIABLES
		pygame.init()
		self.configs = Configs()
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.surface = pygame.Surface((300, 350))
		self.screen = screen
		self.server = server
  
		self.keys = []
		self.buttonDown = False
  
		self.rect = self.surface.get_rect()
		self.rect[0] = self.screen.get_width() / 2 - self.rect[2] / 2 #x
		self.rect[1] = self.screen.get_height() / 2 - self.rect[3] / 2 #y
  
	def run(self) -> None:
		# Make the components
		button = Button(Pos(self.rect[2] / 2 - 100, self.rect[1] + 75), 200, 50, "Connect", customTextColor="black")
		inputfield = InputBox(Pos(self.rect[2] / 2 - 100, self.rect[1] - 25), 200, 50, "Password", customColor="white", customTextColor="black")
		alertTxt = ""

		while self.running:   
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						if inputfield.active:
							inputfield.active = False
						else:
							self.running = False
					if event.key == pygame.K_TAB:
						inputfield.active = not inputfield.active

				mx, my = pygame.mouse.get_pos()
				mx = mx - self.rect[0]
				my = my - self.rect[1]
				inputfield.handle_event(event, (mx, my))
			self.keyboard()

			# Close popup if clicked outside of it
			mx, my = pygame.mouse.get_pos()
			if self.buttonDown:
				if not self.rect.collidepoint((mx, my)):
					pygame.time.delay(200)
					self.running = False

			# Popup button actions
			mx = mx - self.rect[0]
			my = my - self.rect[1]
			if button.rect.collidepoint((mx, my)):
				button.color = constants["BUTTON_ACTIVE"]
				if self.buttonDown:
					print(inputfield.value)
					if not inputfield.value:
						alertTxt = "Password Required!"
			else: button.color = "White"

			# Rendering
			self.surface.fill("black")
   
			titleImg = self.font.render("Connecting to {name}".format(name=self.server["name"]), False, "White")
			x, y, w, h = titleImg.get_rect(center = (self.rect[0], self.rect[1]))
			alertImg = self.font.render(alertTxt, False, "White")
			x1, y1, w1, h1 = alertImg.get_rect(center = (self.rect[0], self.rect[1]))
   
			button.draw(self.surface)
			inputfield.draw(self.surface)

			self.screen.blit(self.surface, (self.rect[0], self.rect[1]))
			self.screen.blit(titleImg, (self.rect[0] + (self.rect[2] / 2 - w /2), self.rect[1] + self.rect[3] *.2 - h ))
			self.screen.blit(alertImg, (self.rect[0] + (self.rect[2] / 2 - w1 /2), self.rect[1] + self.rect[3] *.4 - h1 ))

			self.buttonDown = False
   
			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		self.keys = keys

if __name__ == "__main__":
	menu = JoinPopup()
	menu.run()