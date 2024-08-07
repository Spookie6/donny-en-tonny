import pygame

from data.constants import constants

class Pos:
	def __init__(self, x = None, y = None, width = None, height = None):
		self.x = x
		self.y = y
  
	def centered(w=0, h=0):
		res = constants["RESOLUTION"]
		return Pos(res[0] / 2 - w / 2, res[1] / 2 - h / 2)
  
	def getTuple(self):
		return (self.x, self.y)

	def move(self, keys, speed):
			if keys[pygame.K_w]:
				self.y -= speed
			if keys[pygame.K_s]:
				self.y += speed
			if keys[pygame.K_a]:
				self.x -= speed
			if keys[pygame.K_d]:
				self.x += speed
			if self.y < 0:
				self.y = 0
			if self.x < 0:
				self.x = 0
			if self.y + 16 >= 720:
				self.y = 720 - 16
			if self.x + 16 >= 1280:
				self.x = 1280 - 16

class Icon:
    pass

# Building Blocks
class Ground():
	pass

class Lava():
	pass

class Pathway():
	pass

class Door():
	pass

# Characters
class Donny():
	def __init__(self, starting_pos, speed):
		self.pos = Pos(starting_pos[0], starting_pos[1])
		self.speed = speed
		self.rect = pygame.Rect(self.pos.x, self.pos.y, 16,16)
  
	def draw(self, screen):
		self.rect = pygame.Rect(self.pos.x, self.pos.y, 16,16)
		pygame.draw.rect(screen, "blue", self.rect)

	def move(self, keys):
		self.pos.move(keys, self.speed)

class Tonny():
	pass
