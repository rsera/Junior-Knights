# Always import pygame and sys (system)
import pygame, sys
from pygame.locals import *

# Always initialize before any other pygame code
pygame.init()

# Now we begin the "stuff that is done once."

# Create a window surface object
canvas = pygame.display.set_mode((640,480))
# You can set a caption at the top of the window
pygame.display.set_caption("Making a Window")

# Make some color variables
purple = pygame.Color(176, 66, 244)

# Now we begin the "stuff that's done every game loop."

# Our game loop is a while True loop
while True:
    # fill fills in the entire window with the designated color
    canvas.fill(purple)
    # update draws the window (and its contents) at the end of every loop
    pygame.display.update()



    
