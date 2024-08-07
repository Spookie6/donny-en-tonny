import pygame, sys, threading

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

# Import components
from sprites import Pos
from components import Button, InputBox
from server import Server
from client import Client

# Import data
from data.constants import constants
from data.configs import Configs
configs = Configs()

class HostMenu:
	# CONSTANT GAME VARIABLES
	FPS = constants["FPS"]
	def __init__(self, configs) -> None:
		# Menu VARIABLES
		pygame.init()
		self.configs = configs
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), )
  
		self.server = None
		self.server_thread = None
  
		self.keys = []
		self.buttonDown = False
  
		self.inputFields = []
		centered_pos = Pos.centered(200, 50)
		self.inputFields.append(InputBox(Pos(centered_pos.x, centered_pos.y + 25), 200, 50, "Name"))
		self.inputFields.append(InputBox(Pos(centered_pos.x, centered_pos.y + 100), 200, 50, "Password"))
	
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(centered_pos.x, centered_pos.y + 175), 200, 50, "Activate Server", None))

	def run(self) -> None:
		# Load bg image
		bg_img = pygame.image.load("src/assets/background.png").convert_alpha()
  
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					if self.server:
						self.server.stop()
						# self.server_thread.
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						activebox = list(filter(lambda x : x.active, self.inputFields))
						if len(activebox):
							index = self.inputFields.index(activebox[0])
							self.inputFields[index].active = False
						else:
							self.running = False
							if self.server:
								self.server.stop()

       
					if event.key == pygame.K_TAB:
						if len(self.inputFields) == 1:
							continue
						activebox = list(filter(lambda x : x.active, self.inputFields))
						if len(activebox):
							index = self.inputFields.index(activebox[0])
							self.inputFields[index].active = False
							nextIndex = 0 if len(self.inputFields) == index + 1 else index + 1
							self.inputFields[index].active = False
							self.inputFields[nextIndex].active = True

				for inputbox in self.inputFields:
					inputbox.handle_event(event)
    
			self.keyboard()

			self.screen.fill("black")
			self.screen.blit(bg_img, (0,0))
   
			for button in self.menuButtons:
				button.draw(self.screen)
				mx, my = pygame.mouse.get_pos()
				if button.rect.collidepoint((mx, my)):
					button.color = constants["BUTTON_ACTIVE"]
					if self.buttonDown:
         
						configs = Configs()
						server = Server(configs.toml_dict["server_name"], configs.toml_dict["server_password"])
						thread = threading.Thread(target=server.start)
						thread.start()

						self.server = server
						self.server_thread = thread
      
						client = Client(configs.toml_dict["server_name"], configs.toml_dict["server_password"])
						client.connect()
      
				else: button.color = constants["BUTTON_INACTIVE"]

			for inputbox in self.inputFields:
				inputbox.draw(self.screen)
   
			pygame.display.update()
			self.clock.tick(self.FPS)
			self.buttonDown = False
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		self.keys = keys


if __name__ == "__main__":
	menu = HostMenu()
	menu.run()