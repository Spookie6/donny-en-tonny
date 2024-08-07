import pygame, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

# Import components
from components import Button
from sprites import Pos

# Import data
from data.constants import constants

class QuitPopup:
	# # CONSTANT GAME VARIABLES
	FPS:int = constants["FPS"]
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
  
		self.rect = self.surface.get_rect()
		self.rect[0] = self.screen.get_width() / 2 - self.rect[2] / 2
		self.rect[1] = 0 - self.rect[3]
  
	def run(self) -> None:

		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.running = False
			self.keyboard()
   
			# Make the buttons
			button_yes = Button(Pos(self.rect[2] / 2 - 120, self.rect[3] / 2 + 30), 70, 50, "Yes")
			button_no = Button(Pos(self.rect[2] / 2 + 40, self.rect[3] / 2 + 30), 70, 50, "No")

			# Close popup if clicked outside of it
			mx, my = pygame.mouse.get_pos()
			if self.buttonDown:
				if self.rect.collidepoint((mx, my)):
					pass
				else:
					pygame.time.delay(200)
					self.running = False
	
			# Popup button actions
			mx = mx - self.rect[0]
			my = my - self.rect[1]
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
			x, y, w, h = titleImg.get_rect(center = (self.rect[0], self.rect[1]))
   
			button_yes.draw(self.surface)
			button_no.draw(self.surface)
   

			self.screen.blit(self.surface, (self.rect[0], self.rect[1]))
			self.screen.blit(titleImg, (self.rect[0] + (self.rect[2] / 2 - w /2), self.rect[1] + (self.rect[3] / 2 - h / 2) - 30))
     
			self.buttonDown = False
   
			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		self.keys = keys

if __name__ == "__main__":
	menu = QuitPopup()
	menu.run()