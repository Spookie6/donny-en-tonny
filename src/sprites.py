import pygame, math, time

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
	def draw(self, screen):	
		pygame.draw.circle(screen, "white", self.pos.getTuple(), 50)
	def move(self, keys):
		self.pos.move(keys, self.speed)

class Tonny():
	pass