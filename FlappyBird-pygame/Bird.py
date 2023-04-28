import pygame
from pygame.locals import*
import random
from pygame import mixer

N_PIXELS_TO_MOVE = 15
mixer.init()

#bird class
class Bird():
	def __init__(self, window , X , Y):
		self.window = window
		self.windowWidth = X
		self.windowHeight = Y
		self.flap = pygame.mixer.Sound('sounds/flap.wav')
		self.birdImage = pygame.image.load("images/bird.png")
		self.birdImage = pygame.transform.scale(self.birdImage, (166,144))
		self.yBird = 0
		self.yBirdSpeed = N_PIXELS_TO_MOVE
		self.birdRect = self.birdImage.get_rect()

	def update(self):
		self.yBird = self.yBird + self.yBirdSpeed
		self.birdRect = pygame.Rect(50, self.yBird , 83,72)
		keyPressedTuple = pygame.key.get_pressed()
		if keyPressedTuple[pygame.K_UP]:
			self.yBird = self.yBird - 2*N_PIXELS_TO_MOVE
			self.flap.play()
		

	def draw(self):
		self.window.blit(self.birdImage, (50,self.yBird))
