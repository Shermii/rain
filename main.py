import pygame
import random

pygame.init()

screen = pygame.display.set_mode((720,480),pygame.RESIZABLE and pygame.NOFRAME)
width = screen.get_width()
height = screen.get_height()
clock = pygame.time.Clock()

raindrops = []

class drop:
	def __init__(self):
		self.color = ()
		self.x = random.randint(0,width)
		self.y = random.randint(-height,0)
		self.z = random.randint(1,8)
		self.coords = [self.x, self.y, self.z]
		self.rect = pygame.Rect(self.x, self.y, 5/self.z, 10/self.z)

	def do(self):
		self.color = (50/self.z, 50/self.z, 255/self.z)
		pygame.draw.rect(screen, self.color, self.rect)
		self.rect.y += 2
		if (self.rect.y+10 >= height):
			self.x = random.randint(0,width)
			self.y = random.randint(-height,0)
			self.z = random.randint(1,8)
			self.coords = [self.x, self.y, self.z]
			self.rect = pygame.Rect(self.x, self.y, 5/self.z, 10/self.z)

for i in range(1000):
	raindrops.append(drop())



if __name__ == "__main__":
	while 1:
		screen.fill((0,0,0))

		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				quit()
			if (event.type == pygame.VIDEORESIZE):
				screen = pygame.display.set_mode((event.w, event.h), pygame.NOFRAME, 16)
				width = screen.get_width()
				height = screen.get_height()
			if (event.type == pygame.KEYDOWN):
				if (event.key == pygame.K_ESCAPE):
					quit()

		for raindrop in raindrops:
			raindrop.do()
		
		pygame.display.update((0,0,720,480))
		clock.tick(180000)



