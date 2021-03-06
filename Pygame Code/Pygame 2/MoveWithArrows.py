# Always import pygame and sys (system)
import pygame, sys
from pygame.locals import *

# Always initialize before any other pygame code
pygame.init()

# Now we begin the "stuff that is done once."

# Create a window surface object
canvas = pygame.display.set_mode((640,480))
# You can set a caption at the top of the window
pygame.display.set_caption("Move with Arrows")

# Make some color variables
teal = pygame.Color(11, 130, 100)
slate = pygame.Color(23, 43, 56)

# Make the position values for the circle variable
x = 320
y = 240

# Also make variables for the rate of change ("delta") of the position
dx = 1
dy = 1

# Now we begin the "stuff that's done every game loop."

# Our game loop is a while True loop
while True:
    # fill fills in the entire window with the designated color
    canvas.fill(slate)

    # we want to draw our shapes below canvas.fill(), because otherwise, we'd be filling over our shapes
    pygame.draw.circle(canvas, teal, (x, y), 50)
            
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

    # Instead of constantly moving the circle, move it only upon key presses
    pressed = pygame.key.get_pressed()
    if pressed[K_UP] == True:
        y -= dy
    if pressed[K_DOWN] == True:
        y += dy
    if pressed[K_LEFT] == True:
        x -= dx
    if pressed[K_RIGHT] == True:
        x += dx
    
    # update draws the window (and its contents) at the end of every loop
    pygame.display.update()
