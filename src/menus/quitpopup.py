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
 
	def run(self) -> None:

		while self.running:
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
   
			# Make the buttons
			button_yes = Button(Pos(surf_rect[2] / 2 - 120, surf_rect[3] / 2 + 30), 70, 50, "Yes")
			button_no = Button(Pos(surf_rect[2] / 2 + 40, surf_rect[3] / 2 + 30), 70, 50, "No")

			# Close popup if clicked outside of it
			mx, my = pygame.mouse.get_pos()
			if self.buttonDown:
				if surf_rect.collidepoint((mx, my)):
					pass
				else:
					pygame.time.delay(200)
					self.running = False
	
			# Popup button actions
			mx = mx - surf_rect[0]
			my = my - surf_rect[1]
			if button_yes.rect.collidepoint((mx, my)):
				button_yes.color = "Green"
				if self.buttonDown:
					pygame.quit()
					sys.exit()
			else: button_yes.color = "White"
			if button_no.rect.collidepoint((mx, my)):
				button_no.color = "Green"
				if self.buttonDown:
					self.running = False
			else: button_no.color = "White"
   
			# Rendering
			self.surface.fill("black")
   
			titleImg = self.font.render("Are you sure you want to quit?", False, "Blue")
			x, y, w, h = titleImg.get_rect(center = (surf_rect[0], surf_rect[1]))
   
			button_yes.draw(self.surface, self.font)
			button_no.draw(self.surface, self.font)
   
			self.screen.blit(self.surface, (surf_rect[0], surf_rect[1]))
			self.screen.blit(titleImg, (surf_rect[0] + (surf_rect[2] / 2 - w /2), surf_rect[1] + (surf_rect[3] / 2 - h / 2) - 30))
     
			self.buttonDown = False
   
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