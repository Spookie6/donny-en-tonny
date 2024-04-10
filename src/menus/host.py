import pygame, sys, time

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from sprites import Pos
from components import Button
from server import Server

class HostMenu:
	# CONSTANT GAME VARIABLES
	SCREEN_WIDTH:int = 1920
	SCREEN_HEIGHT:int = 1080
	FPS:int = 60
	def __init__(self, configs) -> None:
		# Menu VARIABLES
		pygame.init()
		self.configs = configs
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
		self.keys = []
		self.buttonDown = False
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 10), 200, 50, "Activate Server", None))

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
				mx, my = pygame.mouse.get_pos()
				if self.buttonDown and button.rect.collidepoint((mx, my)):
					pygame.time.delay(200)
					server = Server("Enrico", "Password")
					server.start()
   
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