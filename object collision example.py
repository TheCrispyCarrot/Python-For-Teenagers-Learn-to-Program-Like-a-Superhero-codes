import pygame
from pygame.locals import *
import sys
import random

pygame.init()

#creating colors stored in tuples
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)

# creates and names the window that is created
gameWindow = pygame.display.set_mode((800, 600))

# captions the text in the top of the window
pygame.display.set_caption('Colliding Objects')

#creating two sprite rectagles
rect1 = pygame.sprite.Sprite()
rect1.rect = pygame.Rect(300, 300, 50, 50)

rect2 = pygame.sprite.Sprite()
rect2.rect = pygame.Rect(100, 100, 100, 150)

gameQuit = False

# game loop
while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit = True
            pygame.quit()
            sys.exit()
        # activats esc as a quit button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameQuit = True
                pygame.quit()
                sys.exit()
        # activats q as a quit button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameQuit = True
                pygame.quit()
                sys.exit()


        # movement of the sprite
        if event.type == pygame.KEYDOWN:
            #moves object left with left arrow
            if event.key == pygame.K_LEFT:
                rect1.rect.x = rect1.rect.x - 10
            # moves object right with right arrow
            if event.key == pygame.K_RIGHT:
                rect1.rect.x = rect1.rect.x + 10
            # moves object up with up arrow
            if event.key == pygame.K_UP:
                rect1.rect.y = rect1.rect.y - 10
            # moves object down with down key
            if event.key == pygame.K_DOWN:
                rect1.rect.y = rect1.rect.y + 10

    # checking for colision between sprites
    #if collision detected, relocate rect1
    if pygame.sprite.collide_rect(rect1, rect2):
        rect1.rect.x = 400
        rect1.rect.y = 400



    # fill the screen white
    gameWindow.fill(colorWHITE)

    # blit a black rectangle on the screen
    pygame.draw.rect(gameWindow, colorBLACK, rect1)
    pygame.draw.rect(gameWindow, colorBLACK, rect2)
    
    # update the screen
    pygame.display.update()    
















