import pygame
from pygame.locals import *
import sys

#creates a tuple to hold a value for color
#used to make the colors in RGB
colorBLACK = (0, 0, 0,)
colorBLUE = (0, 0, 255)
colorPINK = (255, 200, 200)
colorGREEN = (0, 255, 0)
colorRED = (255, 0, 0)
colorYELLOW = (255, 255, 0)
colorWHITE = (255, 255, 255)

#initializes the pygame module
pygame.init()

# creates the game screen and sets it to and 800 x 600 display
screen = pygame.display.set_mode((800, 600), 0, 32)

#sets a caption in our window
pygame.display.set_caption("Super Sidekick: The Cuddly Cat")

#creates a blue backaround
screen.fill(colorBLUE)

#prepare the font for the text
myFont = pygame.font.SysFont('None', 40)

# create a text object
firstText = myFont.render("The Cuddly Cat", True, colorRED, colorBLUE)

# create the surfave to write the text
firstTextRect = firstText.get_rect()
firstTextRect.left = 100
firstTextRect.top = 75

#blit the text to the window
screen.blit(firstText, firstTextRect)

#put an image of a cat on the screen
sidekick = pygame.Rect(100, 100, 200, 200)
cat = pygame.image.load('catImage.jpg')
thumbnail_cat = pygame.transform.scale(cat, (200, 200))
screen.blit(thumbnail_cat, sidekick)

#drawing a circle
pygame.draw.circle(screen, colorRED, (330, 475), 15, 1)
pygame.draw.circle(screen, colorYELLOW, (375, 475), 15, 15)
pygame.draw.circle(screen, colorPINK, (420, 475), 20, 10)
#drawing lines and rectangles
pygame.draw.rect(screen, colorYELLOW, (455, 470, 20, 20), 4)
pygame.draw.line(screen, colorRED, (300, 500), (500, 500), 1)
pygame.draw.line(screen, colorYELLOW, (300, 515), (500, 515), 1)
pygame.draw.line(screen, colorRED, (300, 530), (500, 530), 1)

# dreaws the new blue window to the screen
pygame.display.update()

# creates a varriable for if the game should quit or not
running = True

#loop that runs until the user decises to quit
# changes the value of running to false
# this ends the game

while True:
# get feedback from the player in the form of events
    for event in pygame.event.get():
        #if the player clicks the red 'x' it is consitered a quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # allows the cat to meow
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        meowText = myFont.render("Meow!", True, colorRED, colorBLUE)
                        meowTextRect = meowText.get_rect()
                        meowTextRect.left = 300
                        meowTextRect.top = 175
                        screen.blit(meowText, meowTextRect)
                        pygame.display.update()
        if event.type == pygame.KEYUP:
                    if event.key == pygame.K_m:
                        meowText = myFont.render("Meow!", True, colorBLUE, colorBLUE)
                        meowTextRect = meowText.get_rect()
                        meowTextRect.left = 300
                        meowTextRect.top = 175
                        screen.blit(meowText, meowTextRect)
                        pygame.display.update()




            
