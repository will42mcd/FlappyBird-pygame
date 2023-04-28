import pygame
from pygame import mixer
import sys
from pygame.locals import*
import random
from Bird import*

#2 - define constant
white = (255, 255, 255)
black = (0,0,0)
X = 1280
Y = 960
FRAMES_PER_SECOND = 60
N_PIXELS_TO_MOVE = 15

#3 initialize the world
pygame.init()

window = pygame.display.set_mode((X , Y))
clock = pygame.time.Clock()

#4 - loading assets: sounds , images , ect
pipeImage = pygame.image.load('images/pipe.png')
pipeImage = pygame.transform.scale(pipeImage,(240,920))
topPipeImage = pygame.transform.rotate(pipeImage, 180)
font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render('Welcome to Flappybird', True, white, black)
text1 = font.render('Make it through the 5 pipes to Win!', True, white, black)
text2 = font.render('Press the mouse anywhere to start!', True, white, black)
text3 = font.render('YOU WIN!!', True, white, black)
text4 = font.render('GAME OVER!!', True, white, black)
textRect = text.get_rect()
text1Rect = text1.get_rect()
text2Rect = text2.get_rect()
text3Rect = text3.get_rect()
text4Rect = text4.get_rect()


#5 - initialize the varibles
xPipe = 900
x2Pipe = 1500
x3Pipe = 2100
x4Pipe = 2700
x5Pipe = 3300
pipeSpeed = N_PIXELS_TO_MOVE
oBird = Bird(window , X , Y)
textRect.center = (640, 480)
text1Rect.center = (650 , 550)
text2Rect.center = (560 , 550)
text3Rect.center = (650 , 550)
text4Rect.center = (650 , 550)
yBird = 0
start = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    window.fill(black)

    if start == 0:
        window.fill(black)
        window.blit(text, textRect)
        window.blit(text1, text1Rect)
        window.blit(text2, (310,600))
        if event.type == pygame.MOUSEBUTTONUP:
            start = start + 2

    elif start == 1:
        window.fill(black)
        window.blit(text4,text4Rect)    
        pygame.time.delay(2500)
        start = start - 1
            

    elif start == 2: 
		#8 - Do any "per frame" actions
        window.fill(black)
        oBird.update()
        xPipe = xPipe - pipeSpeed
        x2Pipe = x2Pipe - pipeSpeed
        x3Pipe = x3Pipe - pipeSpeed
        x4Pipe = x4Pipe - pipeSpeed
        x5Pipe = x5Pipe - pipeSpeed
        yBird = yBird + N_PIXELS_TO_MOVE

        pipeRect = pygame.Rect(xPipe, 500 ,240,920)
        topPipeRect = pygame.Rect(xPipe, -800 ,240,920)
        pipe2Rect = pygame.Rect(x2Pipe, 700 ,240,920)
        topPipe2Rect = pygame.Rect(x2Pipe, -600 ,240,920)
        pipe3Rect = pygame.Rect(x3Pipe, 700 ,240,920)
        topPipe3Rect = pygame.Rect(x3Pipe, -600 ,240,920)
        pipe4Rect = pygame.Rect(x4Pipe, 400 ,240,920)
        topPipe4Rect = pygame.Rect(x4Pipe, -900 ,240,920)
        pipe5Rect = pygame.Rect(x5Pipe, 850 ,240,920)
        topPipe5Rect = pygame.Rect(x5Pipe, -450 ,240,920)

        if oBird.birdRect.colliderect(pipeRect):
            start = start - 1
	
        if oBird.birdRect.colliderect(topPipeRect):
            start = start - 1

        if oBird.birdRect.colliderect(pipe2Rect):
            start = start - 1

        if oBird.birdRect.colliderect(topPipe2Rect):
            start = start - 1

        if oBird.birdRect.colliderect(pipe3Rect):
            start = start - 1

        if oBird.birdRect.colliderect(topPipe3Rect):
            start = start - 1

        if oBird.birdRect.colliderect(pipe4Rect):
            start = start - 1

        if oBird.birdRect.colliderect(topPipe4Rect):
            start = start - 1

        if oBird.birdRect.colliderect(pipe5Rect):
            start = start - 1

        if oBird.birdRect.colliderect(topPipe5Rect):
            start = start - 1

        if x5Pipe < 25:
            start = start - 1

		#9 - Clear the window
        window.fill(black)

		#10 - Draw all window elements
        oBird.draw()
        window.blit(pipeImage, (xPipe,500))
        window.blit(topPipeImage, (xPipe,-800))
        window.blit(pipeImage, (x2Pipe,700))
        window.blit(topPipeImage, (x2Pipe,-600))
        window.blit(pipeImage, (x3Pipe,700))
        window.blit(topPipeImage, (x3Pipe,-600))
        window.blit(pipeImage, (x4Pipe,400))
        window.blit(topPipeImage, (x4Pipe,-900))
        window.blit(pipeImage, (x5Pipe,850))
        window.blit(topPipeImage, (x5Pipe,-450))	
		#11 - Update the window


    pygame.display.update()
    #12- slow things down
    clock.tick(FRAMES_PER_SECOND)
