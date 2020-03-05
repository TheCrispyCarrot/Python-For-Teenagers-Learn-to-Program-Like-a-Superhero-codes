import pygame
from pygame.locals import *
import sys
import random

pygame.init()

# varriables
gameQuit = False
move_x = 300
move_y = 300

#creating colors stored in tuples
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)

# creates and names the window that is created
gameWindow = pygame.display.set_mode((800, 600))

# captions the text in the top of the window
pygame.display.set_caption('Box Animator 5000')


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

                
        if event.type == pygame.KEYDOWN:
            #moves object left with left arrow
            if event.key == pygame.K_LEFT:
                move_x -= 10
            # moves object right with right arrow
            if event.key == pygame.K_RIGHT:
                move_x += 10
            # moves object up with up arrow
            if event.key == pygame.K_UP:
                move_y -= 10
            # moves object down with down key
            if event.key == pygame.K_DOWN:
                move_y += 10

        #creates a teleport to a rendom spot when t is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == K_t:
                move_x = int(random.randint(1, 750))
                move_y = int(random.randint(1, 550))
                pygame.display.set_caption('Gnarly Teleport!')

                
    # fill the screen white
    gameWindow.fill(colorWHITE)

    # checking for collisions
    #right collision
    if move_x > 750:
        move_x -= 50
        pygame.display.set_caption('Right Collision!')
    # left collision
    if move_x <1:
        move_x += 50
        pygame.display.set_caption('Left Collision!')
    # bottom colision
    if move_y > 550:
        move_y -= 50
        pygame.display.set_caption('Bottom Collision!')
    # top colision
    if move_y < 1:
        move_y += 50
        pygame.display.set_caption('Top Collision!')


    # blit a black rectangle on the screen
    pygame.draw.rect(gameWindow, colorBLACK, [move_x, move_y, 50, 50])

    # update the screen
    pygame.display.update()







            
