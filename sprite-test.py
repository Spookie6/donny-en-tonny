import pygame, math, sys

from src.sprites import Pos, Donny

class Brick:
	def __init__(self, pos=None) -> None:
		self.img = pygame.image.load("src/assets/brick.png").convert_alpha()
		self.img = pygame.transform.scale(self.img, (32, 32))
		self.pos = pos
  
	def fill(self, screen):
		rect = screen.get_rect()
		x = math.ceil(rect[2] / 32)
		y = math.ceil(rect[3] / 32)
		# for every y axes
		for i in range(0, y):
			for j in range (0, x):
				screen.blit(self.img, (i * 32, j * 32))
		return screen
      

	def draw(self, screen):
		if not self.pos:
			raise Exception("No position given to draw at")
		screen.blit(self.img, self.pos.getTuple())

class Game:
	# CONSTANT GAME VARIABLES
	SCREEN_WIDTH:int = 1280
	SCREEN_HEIGHT:int = 720
	FPS:int = 60
	def __init__(self) -> None:
		# GAME VARIABLES
		pygame.init()
		self.running:bool = True
		self.font = pygame.font.SysFont("default", 64, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
		self.keys = []
		self.status_msg = ""

		# self.bricks = []
		# self.bricks.append(Brick(Pos(0,0)))
		brick = Brick()
		self.ground = brick.fill(pygame.Surface((1280, 720)))

		self.donny = Donny(Pos(64,64).getTuple(), 8)
	def run(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.keyboard()
			self.screen.fill("black")
			
			self.screen.blit(self.ground, (0,0))
			self.donny.move(self.keys)
			self.donny.draw(self.screen)
			
			# for brick in self.bricks:
			# 	brick.draw(self.screen)

			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			sys.exit()
			self.running = False
		self.keys = keys

if __name__ == "__main__":
	game = Game()
	game.run()