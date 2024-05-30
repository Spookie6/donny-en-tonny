import pygame, time
from sprites import Pos, Donny

class Game:
	# CONSTANT GAME VARIABLES
	FPS:int = 60
	def __init__(self, configs) -> None:
		# GAME VARIABLES
		pygame.init()
		self.configs = configs
		self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.configs.toml_dict["resolution"]

		self.running:bool = True
		self.font = pygame.font.SysFont("default", 64, bold=False, italic=False)
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
		self.keys = []
		self.status_msg = ""

		self.donny = Donny(Pos(0,0).getTuple(), 10)

	def run(self) -> None:
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.keyboard()
			self.screen.fill("black")
			
			self.donny.move(self.keys)
			self.donny.draw(self.screen)

			pygame.display.update()
			self.clock.tick(self.FPS)
   
	def keyboard(self) -> list:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE]:
			pygame.time.delay(200)
			self.running = False
		self.keys = keys

if __name__ == "__main__":
	game = Game()
	game.run()