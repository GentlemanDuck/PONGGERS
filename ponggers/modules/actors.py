from pygame import *; from random import randint;

class player(sprite.Sprite):
	def __init__(self, textura, largura, altura, fonte):
		#pucha a classe super()
		super().__init__()

#textura e corpo
		self.image = image.load(textura)
		self.rect = self.image.get_rect()
		self.score = 0
		self.pontos = fonte.render(str(self.score), True, (0, 0, 0), (255, 255, 255))
		self.pontosRect = self.pontos.get_rect()

#movimento
	def moveUp(self, pixels):
		#pixels == velocidade
		self.rect.y -= pixels
		#limite da tela
		if self.rect.y < 0:
			self.rect.y = 0


	def moveDown(self, pixels):
		#pixels == velocidade denovo
		self.rect.y += pixels
		#limite da tela dnv
		if self.rect.y > 492:
			self.rect.y = 492	


class ball(sprite.Sprite):
	def __init__(self, textura, largura, altura, bolasfx):
#mesmo de cima
		super().__init__()
		self.image = image.load(textura)
		self.vel = [randint(-3, 3), randint(-3, 3)]
		while 0 in self.vel:
			self.vel = [randint(-3, 3), randint(-3, 3)]
		self.rect = self.image.get_rect()
		self.sfx = bolasfx
		
#faz a bola mecher
	def update(self, p1, p2):
		self.rect.x += self.vel[0]
		self.rect.y += self.vel[1]


#faz a bola quicar
	def bounce(self):
		#aumentar velocidade a cada 2 quicadas
		bounceCount = 0
		bounceCount += 1
		if self.vel[0] < 0:
			self.vel[0] = -self.vel[0] + 1
		elif self.vel[0] > 0:
			self.vel[0] = -self.vel[0] - 1
		self.vel[1] = randint(-3, 3)
		while self.vel[1] == 0:
			self.vel[1] = randint(-3, 3)


