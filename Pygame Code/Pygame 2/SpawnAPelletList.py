# Always import pygame and sys (system)
import pygame, sys, random
from pygame.locals import *

# Always initialize before any other pygame code
pygame.init()

# Now we begin the "stuff that is done once."

# Create a window surface object
canvas = pygame.display.set_mode((640,480))
# You can set a caption at the top of the window
pygame.display.set_caption("SpawnAPelletList")

# Make some color variables
teal = pygame.Color(11, 130, 100)
slate = pygame.Color(23, 43, 56)

pelletList = []

# Now we begin the "stuff that's done every game loop."

# Our game loop is a while True loop
while True:
    # fill fills in the entire window with the designated color
    canvas.fill(slate)
            
    # We need a for loop to handle events
    for event in pygame.event.get(): #get() returns a list of all the events that occurred since last time it was called
        # We have 2 methods for closing the window. You can use 1 or both of them.
        # Method #1 for closing the window: closing by clicking the X
        if event.type == QUIT:
            pygame.quit() # quit is the opposite of init
            sys.exit()
        # Method #2 for closing the window: closing by pressing the escape key
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        # We'll also handle keydown events and check for the "p" key to spawn a pellet
        if event.type == KEYDOWN:
            if event.key == K_p:
                x = random.randint(10,630)
                y = random.randint(10,470)
                pelletList.append((x,y))
                
    for point in pelletList:
        pygame.draw.circle(canvas, teal, point, 10)
    
    # update draws the window (and its contents) at the end of every loop
    pygame.display.update()
