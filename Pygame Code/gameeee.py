import pygame, sys, random
from pygame.locals import *

pygame.init()

canvas = pygame.display.set_mode((640,480))

pygame.display.set_caption("Making a Window")

purple = pygame.Color(176,66,244)
teal = pygame.Color(11,130,100)
slate = pygame.Color(23, 43, 56)

x = 320
y = 240

clickList = []

while True:
    canvas.fill(slate)

    pygame.draw.circle(canvas, teal, (x,y), 50)
      
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos


        if event.type == MOUSEBUTTONDOWN:
            clickList.append(event.pos)
            if event.button in (1, 2, 3):
                rectColor = teal
            elif event.button in (4,5):
                rectColor = purple


    for click in clickList:
        pygame.draw.rect(canvas, rectColor, click + (20,40))
        
    pygame.draw.circle(canvas, teal, (mouseX, mouseY), 25)


        
    pygame.display.update()
