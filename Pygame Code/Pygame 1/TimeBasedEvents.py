# timer
import pygame, sys, random
from pygame.locals import *

pygame.init()

canvas = pygame.display.set_mode((640,480))
pygame.display.set_caption("Time-based Events")

purple = pygame.Color(176,66,244)
teal = pygame.Color(11,130,100)
slate = pygame.Color(23, 43, 56)

spawnEvent = pygame.USEREVENT
t = 1000
pygame.time.set_timer(spawnEvent, t)

location = []

while True:
    canvas.fill(slate)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            
        if event.type == spawnEvent:
            x = random.randint(10,630)
            y = random.randint(10,470)
            #if location:
            #    del location[0]
            location.append((x,y))

    for loc in location:
        pygame.draw.circle(canvas, teal, loc, 10) 
    pygame.display.update()
