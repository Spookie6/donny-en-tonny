import pygame, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from components import Button
from sprites import Pos

from host import HostMenu
from settings import SettingsMenu 
from main import Game

from data.configs import Configs

class MainMenu:
	# # CONSTANT GAME VARIABLES
	# SCREEN_WIDTH:int = width
	# SCREEN_HEIGHT:int = height
	FPS:int = 60
	def __init__(self) -> None:
		# Menu VARIABLES
		pygame.init()	
		self.configs = Configs()
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
		self.keys = []
		self.buttonDown = False
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 + 10), 200, 50, "Host", HostMenu))
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 + 110), 200, 50, "Join", Game))
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 + 210), 200, 50, "Settings", SettingsMenu))

	def run(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
			if self.configs.toml_dict["resolution"][0] != self.SCREEN_WIDTH:
				print("hello!")

			self.screen.fill("black")
			self.keyboard()
   
			for button in self.menuButtons:
				button.draw(self.screen, self.font)
				button.checkActive(self.buttonDown, self.configs)
   
			pygame.display.update()
			self.clock.tick(self.FPS)
			self.buttonDown = False
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
		self.keys = keys


if __name__ == "__main__":
	menu = MainMenu()
	menu.run()