import pygame, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

# Import components
from components import Button, InputBox
from sprites import Pos

# Import data
from data.configs import Configs
from data.constants import constants

class JoinPopup:
	# # CONSTANT GAME VARIABLES
	FPS:int = constants["FPS"]
	def __init__(self, server, screen) -> None:
		# Menu VARIABLES
		pygame.init()
		self.configs = Configs()
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.surface = pygame.Surface((300, 400))
		self.screen = screen
		self.server = server
  
		self.keys = []
		self.buttonDown = False
  
		self.rect = self.surface.get_rect()
		self.rect[0] = self.screen.get_width() / 2 - self.rect[2] / 2 #x
		self.rect[1] = self.screen.get_height() / 2 - self.rect[3] / 2 #y
  
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
   
			# Make the components
			button = Button(Pos(self.rect[2] / 2 - (self.rect[2] * .6) /2, self.rect[1] + 150), self.rect[2] * .6, 50, "Connect", customTextColor="black")
			inputfield = InputBox(Pos(self.rect[2] / 2 - (self.rect[2] * .6) /2, self.rect[1]), 200, 50, "Password")

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
			if button.rect.collidepoint((mx, my)):
				button.color = constants["BUTTON_ACTIVE"]
				if self.buttonDown:
					pygame.quit()
					sys.exit()
			else: button.color = "White"

			# Rendering
			self.surface.fill("black")
   
			titleImg = self.font.render(f"Connecting to {self.server["name"]}", False, "White")
			x, y, w, h = titleImg.get_rect(center = (self.rect[0], self.rect[1]))
   
			button.draw(self.surface)
			inputfield.draw(self.screen)

			self.screen.blit(self.surface, (self.rect[0], self.rect[1]))
			self.screen.blit(titleImg, (self.rect[0] + (self.rect[2] / 2 - w /2), self.rect[1] + self.rect[3] *.2 - h ))

			self.buttonDown = False
   
			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		self.keys = keys

if __name__ == "__main__":
	menu = JoinPopup()
	menu.run()