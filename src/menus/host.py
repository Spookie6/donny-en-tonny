import pygame, sys, time

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

# Import components
from sprites import Pos
from components import Button
from server import Server

# Import data
from data.constants import Constants
constants = Constants()

class HostMenu:
	# CONSTANT GAME VARIABLES
	FPS = constants.FPS
	def __init__(self, configs) -> None:
		# Menu VARIABLES
		pygame.init()
		self.configs = configs
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), )
  
		self.keys = []
		self.buttonDown = False
  
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 - 25), 200, 50, "Activate Server", None))

	def run(self) -> None:
     
		# Load bg image
		bg_img = pygame.image.load("src/assets/background.png").convert_alpha()
  
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
			self.keyboard()

			self.screen.fill("black")
			self.screen.blit(bg_img, (0,0))
   
			for button in self.menuButtons:
				button.draw(self.screen, self.font)
				mx, my = pygame.mouse.get_pos()
				if button.rect.collidepoint((mx, my)):
					button.color = "Green"
					if self.buttonDown:
						pygame.time.delay(200)
						server = Server("Enrico", "Password")
						server.start()
				else: button.color = "White"
   
			pygame.display.update()
			self.clock.tick(self.FPS)
			self.buttonDown = False
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.time.delay(200)
			self.running = False
		self.keys = keys


if __name__ == "__main__":
	menu = HostMenu()
	menu.run()