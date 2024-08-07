import pygame, sys, threading

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

# Import components
from components import ServerListItem, Button
from sprites import Pos

# Import data
from data.configs import Configs
from data.constants import constants

# Import networking features
from network.serverFetcher import fetchServers

from joinPopup import JoinPopup

class JoinMenu:
	# # CONSTANT GAME VARIABLES
	FPS:int = constants["FPS"]
	def __init__(self, configs) -> None:
		# Menu VARIABLES
		pygame.init()	
		self.configs = Configs()
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]

		self.running:bool = True
		self.font = constants["FONT"]
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),  )
		pygame.display.set_caption("Donny & Tonny")

		self.keys = []
		self.buttonDown = False
	
		self.quit = False

		self.serverList = []
		self.listItems = []
		self.serversLoaded = False
  
		self.thread = threading.Thread(target=fetchServers, args=(self.serverList,))
		self.thread.start()

	def run(self) -> None:

		# Load bg image
		bg_img = pygame.image.load("src/assets/background.png").convert_alpha()
  		
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
							if self.thread.is_alive():
								pass
							else:
								self.serverList = []
								self.listItems = []
								self.running = False
       
			self.configs = Configs()
			self.keyboard()
   
			self.screen.fill("black")
			self.screen.blit(bg_img, (0,0))
   
			if self.thread.is_alive():
				rect = pygame.Rect(Pos.centered().x - 150, Pos.centered().y - 50, 300, 100)
				pygame.draw.rect(self.screen, "Black", rect)
    
				loading_txt_surf = constants["FONT"].render("Loading...", False, "White")
				loading_txt_rect = loading_txt_surf.get_rect()
    
				self.screen.blit(loading_txt_surf, (Pos.centered().x - loading_txt_rect[2] /2, Pos.centered().y - loading_txt_rect[3]/2))
				pygame.display.update()
				continue

			if not self.thread.is_alive():
				if not self.serversLoaded:
					for index, server in enumerate(self.serverList):
						self.listItems.append(ServerListItem(server, Pos.centered().x - 150, Pos.centered().y - 50 + 75 * index, 300, 40))
     
			self.screen.fill("black")
			self.screen.blit(bg_img, (0,0))
   
			if len(self.listItems):
				for item in self.listItems:
					item.handleEvent(item.server, self.screen, JoinPopup)
					item.draw(self.screen)
			else:
				rect = pygame.Rect(Pos.centered().x - 150, Pos.centered().y - 50, 300, 100)
				pygame.draw.rect(self.screen, "Black", rect)
				txt_surf = constants["FONT"].render("No Game Servers Found", False, "Red")
				txt_rect = txt_surf.get_rect()
				self.screen.blit(txt_surf, (Pos.centered().x - txt_rect[2] / 2, Pos.centered().y - txt_rect[3]/2 ))

			self.buttonDown = False

			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()    
		self.keys = keys


if __name__ == "__main__":
	menu = JoinMenu()
	menu.run()