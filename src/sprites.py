import pygame

class Pos():
	def __init__(self, x, y):
		self.x = x
		self.y = y
  
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
			if self.y + 32 >= 720:
				self.y = 720 - 32
			if self.x + 32 >= 1280:
				self.x = 1280 - 32

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
		self.rect = pygame.Rect(self.pos.x, self.pos.y, 32,32)
  
	def draw(self, screen):
		self.rect = pygame.Rect(self.pos.x, self.pos.y, 32,32)
		pygame.draw.rect(screen, "blue", self.rect)

	def move(self, keys):
		self.pos.move(keys, self.speed)

class Tonny():
	pass
