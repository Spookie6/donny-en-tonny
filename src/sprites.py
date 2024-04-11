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

class Icon(pygame.sprite.Sprite):
    def __init__(self,imagePath, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.smileyImage = pygame.image.load(imagePath)
        self.image = self.smileyImage.convert_alpha()
        ### need to assume a default scale, DISPLAYS[0] will be default for us
        self.rect = self.image.get_rect()
        self.pos = Pos(x, y)
        self.rect.x = x
        self.rect.y = y
        self.defaultx = (float(self.rect[2])/2560)*100
        self.defaulty = (float(self.rect[3])/1440)*100
        ## this is the percent of the screen that the image should take up in the x and y planes



    def updateSize(self,configs):
        self.image = ImageRescaler(self.smileyImage,(self.defaultx,self.defaulty))
        self.rect = self.image.get_rect()
        self.rect.x = self.posX
        self.rect.y = self.posY

def ImageRescaler(image,originalScaleTuple, configs): #be sure to restrict to only proper ratios
    w, h = configs.toml_dict['resolution']
    newImage = pygame.transform.scale(image,(int(w*(originalScaleTuple[0]/100)),
                                         int(h*(originalScaleTuple[1]/100))))
    return newImage

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
