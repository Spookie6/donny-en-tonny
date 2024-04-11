import pygame, sys, time

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from sprites import Pos
from components import Button

RESOLUTIONS = ([1280, 720], [1920, 1080], [2560, 1440])

def changeResolution(configs, res):
	for Res in RESOLUTIONS:
		if int(res) in Res:
			configs.setRes(Res)
			

class SettingsMenu:
	FPS:int = 60
	def __init__(self, configs) -> None:
		# Menu VARIABLES
		pygame.init()
		self.configs = configs
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
		self.keys = []
		self.buttonDown = False
		self.menuButtons = []
		# Multiply the button dimensions with the resolution scale
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 - 125), 200, 50, "720p",))
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2), 200, 50, "1080p",))
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 + 125), 200, 50, "1440p",))
		self.menuButtons.append(Button(Pos(self.SCREEN_WIDTH / 2 - 100, self.SCREEN_HEIGHT / 2 + 250), 200, 50, "Save",))

	def run(self) -> None:
		print(f"[SETTINGSMENU] - Resolution: ({self.SCREEN_WIDTH}, {self.SCREEN_HEIGHT})")
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
					if button.title == "Save":
						self.configs.save()
						pygame.time.delay(200)
						self.running = False
					else:
						changeResolution(self.configs, int(button.title[:-1]))

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
	menu = SettingsMenu()
	menu.run()