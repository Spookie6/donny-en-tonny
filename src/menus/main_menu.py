import pygame, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from components import Button
from host import Host
from sprites import Pos
from main import Game

class Menu():
	# CONSTANT GAME VARIABLES
	SCREEN_WIDTH:int = 1920
	SCREEN_HEIGHT:int = 1080
	FPS:int = 60
	def __init__(self) -> None:
		# Menu VARIABLES
		pygame.init()
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
		self.keys = []
		self.buttonDown = False
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 10), 200, 50, "Host", Host))
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 + 110), 200, 50, "Join", Game))
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 + 210), 200, 50, "Settings"))

	def run(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True

			self.screen.fill("black")
			self.keyboard()
   
			for button in self.menuButtons:
				button.draw(self.screen, self.font)
				button.checkActive(self.buttonDown)
   
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
	menu = Menu()
	menu.run()