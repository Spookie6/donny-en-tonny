import pygame, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

# Import components
from components import Button
from sprites import Pos

# Import data
from data.constants import Constants
constants = Constants()

class QuitPopup:
	# # CONSTANT GAME VARIABLES
	FPS:int = constants.FPS
	def __init__(self, configs, screen) -> None:
		# Menu VARIABLES
		pygame.init()
		self.configs = configs
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]

		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.surface = pygame.Surface((400, 200))
		self.screen = screen
  
		self.keys = []
		self.buttonDown = False
  
		self.menuButtons = []
 
	def run(self) -> None:

		while self.running:
			print(self.buttonDown)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
			self.keyboard()
   
			surf_rect = self.surface.get_rect()
			surf_rect[0] = self.screen.get_width() / 2 - surf_rect[2] / 2
			surf_rect[1] = self.screen.get_height() / 2 - surf_rect[3] / 2
   
			mx, my = pygame.mouse.get_pos()
			if self.buttonDown:
				if surf_rect.collidepoint((mx, my)):
					pass
				else:
					pygame.time.delay(200)
					self.running = False
     
			self.buttonDown = False
			
			for button in self.menuButtons:
				button.draw(self.screen, self.font)
				button.checkActive(self.buttonDown, self.configs)


			self.surface.fill("black")
   
			button_yes = Button(Pos(surf_rect[2] / 2 - 120, surf_rect[3] / 2 + 30), 80, 50, "Yes", QuitPopup)
			button_no = Button(Pos(surf_rect[2] / 2 + 40, surf_rect[3] / 2 + 30), 80, 50, "No", QuitPopup)
			button_yes.draw(self.surface, self.font)
			button_no.draw(self.surface, self.font)
   
			self.screen.blit(self.surface, (self.screen.get_width() / 2 - surf_rect[2] / 2, self.screen.get_height() / 2 - surf_rect[3] / 2))

			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.time.delay(200)
			self.running = False
		self.keys = keys


if __name__ == "__main__":
	menu = QuitPopup()
	menu.run()