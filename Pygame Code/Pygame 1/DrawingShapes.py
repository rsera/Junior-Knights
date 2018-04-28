# Always import pygame and sys (system)
import pygame, sys
from pygame.locals import *

# Always initialize before any other pygame code
pygame.init()

# Now we begin the "stuff that is done once."

# Create a window surface object
canvas = pygame.display.set_mode((640,480))
# You can set a caption at the top of the window
pygame.display.set_caption("Drawing Shapes")

# Make some color variables
purple = pygame.Color(176, 66, 244)
teal = pygame.Color(11, 130, 100)
slate = pygame.Color(23, 43, 56)

# Now we begin the "stuff that's done every game loop."

# Our game loop is a while True loop
while True:
    # fill fills in the entire window with the designated color
    canvas.fill(slate)

    # we want to draw our shapes below canvas.fill(), because otherwise, we'd be filling over our shapes
    pygame.draw.circle(canvas, teal, (320, 240), 50)
    pygame.draw.circle(canvas, teal, (320, 345), 50, 5)
    pygame.draw.rect(canvas, purple, (10, 10, 50, 100))
        
    # We need a for loop to handle events
    for event in pygame.event.get(): #get() returns a list of all the events that occurred since last time it was called
        # We have 2 methods for closing the window. You can use 1 or both of them.
        # Method #1 for closing the window: closing by clicking the X
        if event.type == QUIT:
            pygame.quit() # quit is the opposite of init
            sys.exit()
        # Method #2 for closing the window: closing by pressing the escape key
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Once we want to deal with other events (like the player clicking mouse buttons
        # or pressing keys), we'll use elif statements here, after the exit checks
        # to check for those events too

    
    # update draws the window (and its contents) at the end of every loop
    pygame.display.update()
