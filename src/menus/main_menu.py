import pygame, sys
import tkinter as tk

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

RESOLUTIONS = ([1280, 720], [1920, 1080], [2560, 1440])

from components import Button
from sprites import Pos

from host import HostMenu
from settings import SettingsMenu 
from main import Game

from data.configs import Configs

class MainMenu:
	# # CONSTANT GAME VARIABLES
	FPS:int = 60
	def __init__(self) -> None:
		# Menu VARIABLES
		pygame.init()	
		self.configs = Configs()
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]
  
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.surface = pygame.Surface((2560, 1440))
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
		self.keys = []
		self.buttonDown = False
		self.menuButtons = []
		self.menuButtons.append(Button(Pos(self.surface.get_rect()[2] / 2 - 200, self.surface.get_rect()[3] / 2 - 130), 400, 100, "Host", HostMenu))
		self.menuButtons.append(Button(Pos(self.surface.get_rect()[2] / 2 - 200, self.surface.get_rect()[3] / 2), 400, 100, "Join", Game))
		self.menuButtons.append(Button(Pos(self.surface.get_rect()[2] / 2 - 200, self.surface.get_rect()[3] / 2 + 130), 400, 100, "Settings", SettingsMenu))
	
	def run(self) -> None:
		print(f"[MAIN MENU] - Resolution: ({self.screen.get_rect()})")
		print(f"[MAIN MENU] - Button Info: {self.menuButtons[0].pos.x}, {self.menuButtons[0].pos.y}")

		# Load bg image
		bg_img = pygame.image.load("src/assets/menu-backgroun.jpg").convert_alpha()
		print(bg_img.get_rect())
  
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.buttonDown = True
			self.configs = Configs()
			self.keyboard()
   
			self.surface.fill("black")
			self.surface.blit(bg_img, (0,0))
   
			# Resize
			sw, sh = self.configs.toml_dict["resolution"]
			if  sw != self.SCREEN_WIDTH:
				print("Wrong resolution!")
				self.resizeDisplay((sw, sh))
				for button in self.menuButtons:
					button.rescale((), self.configs)
				print(f"[MAIN MENU] - Rezised to ({sw}, {sh})")
				print(f"[MAIN MENU] - Button Info: {self.menuButtons[0].pos.x}, {self.menuButtons[0].pos.y}")

			for button in self.menuButtons:
				button.draw(self.surface, self.font)
				button.checkActive(self.buttonDown, self.configs)
   
			self.buttonDown = False
   
			pygame.transform.scale(self.surface, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT), dest_surface=self.surface)
			print(self.surface.get_rect())
			self.screen.blit(self.surface, (0, 0))
			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
		self.keys = keys
  
	def resizeDisplay(self, size) -> None:
		print("Rezising!")
		self.screen = pygame.display.set_mode(size)
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = size
		# self.font = pygame.font.SysFont("default", 32, bold=False, italic=False)


if __name__ == "__main__":
	menu = MainMenu()
	menu.run()