import pygame, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

# Import components
from components import Button
from sprites import Pos

# Import menu screens
from host import HostMenu
from quitpopup import QuitPopup
from main import Game

# Import data
from data.configs import Configs
from data.constants import Constants
constants = Constants()

class MainMenu:
	# # CONSTANT GAME VARIABLES
	FPS:int = constants.FPS
	def __init__(self) -> None:
		# Menu VARIABLES
		pygame.init()	
		self.configs = Configs()
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]

		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),  )
  
		self.keys = []
		self.buttonDown = False
		self.pressed = False
  
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(1280 / 2 - 100, 720 / 2 + 25), 200, 50, "Host", HostMenu))
		self.menuButtons.append(Button(Pos(1280 / 2 - 100, 720 / 2 + 100), 200, 50, "Join", Game))
		self.menuButtons.append(Button(Pos(1280 / 2 - 100, 720 / 2 + 175), 200, 50, "Quit", QuitPopup, self.screen))

		self.quit = False
 
	def run(self) -> None:

		# Load bg image
		bg_img = pygame.image.load("src/assets/background.png").convert_alpha()
  		
		while self.running:
			print("Main")
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
			self.configs = Configs()
			self.keyboard()
   
			self.screen.fill("black")
			self.screen.blit(bg_img, (0,0))
			
			for button in self.menuButtons:
				button.draw(self.screen, self.font)
				button.checkActive(self.buttonDown, self.configs)

			self.buttonDown = False
   
			if self.quit:
				print("h")
				self.quit = False
				self.buttonDown = False
				pygame.time.delay(200)
				QuitPopup(self.configs, self.screen).run()

			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()

		if not keys[pygame.K_ESCAPE]:
			self.pressed = False
   
		if keys[pygame.K_ESCAPE]:
			if not self.pressed:
				if self.quit:
					self.quit = False
				else:
					self.quit = True
				self.pressed = True
    
		self.keys = keys


if __name__ == "__main__":
	menu = MainMenu()
	menu.run()