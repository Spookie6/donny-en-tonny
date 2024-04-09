import pygame, math, time, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from sprites import Pos
from components import Button

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
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(10, 10), 200, 50, "Host"))
		self.menuButtons.append(Button(Pos(10, 100), 200, 50, "Join"))
		self.menuButtons.append(Button(Pos(10, 200), 200, 50, "Settings"))

	def run(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.keyboard()
			self.screen.fill("black")
			for button in self.menuButtons:
				button.draw(self.screen, self.font)
   
			pygame.display.flip()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.quit()
		self.keys = keys

if __name__ == "__main__":
	menu = Menu()
	menu.run()