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
from data.constants import constants

class MainMenu:
	# # CONSTANT GAME VARIABLES
	FPS:int = constants["FPS"]
	def __init__(self) -> None:
		# Menu VARIABLES
		pygame.init()	
		self.configs = Configs()
		constants["FONT"] = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]

		self.running:bool = True
		self.font = constants["FONT"]
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),  )
  
		self.keys = []
		self.buttonDown = False
  
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(1280 / 2 - 100, 720 / 2 + 25), 200, 50, "Host", HostMenu))
		self.menuButtons.append(Button(Pos(1280 / 2 - 100, 720 / 2 + 100), 200, 50, "Join", Game))
		self.menuButtons.append(Button(Pos(1280 / 2 - 100, 720 / 2 + 175), 200, 50, "Quit", QuitPopup, self.screen))

		self.quit = False
 
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
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
							QuitPopup(self.configs, self.screen).run()
       
			self.configs = Configs()
			self.keyboard()
   
			self.screen.fill("black")
			self.screen.blit(bg_img, (0,0))
			
			for button in self.menuButtons:
				button.draw(self.screen)
				button.checkActive(self.buttonDown, self.configs)

			self.buttonDown = False

			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()    
		self.keys = keys


if __name__ == "__main__":
	menu = MainMenu()
	menu.run()