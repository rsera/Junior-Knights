5# Always import pygame and sys (system)
import pygame, sys
from pygame.locals import *

# Always initialize before any other pygame code
pygame.init()

# Now we begin the "stuff that is done once."

# Make some color variables
purple = pygame.Color(176, 66, 244)
teal = pygame.Color(11, 130, 100) #only teal is used so far in this game
slate = pygame.Color(23, 43, 56)

# Make image variables
# The image file needs to be in the same folder as the python file
bkgrndImage = pygame.image.load("piggy.jpg")
ball = pygame.image.load("carrot.jpg")

# Initialize variables
score = 0
misses = 0

# set font
myFont = pygame.font.SysFont("monospace", 16)

# The resolution/dimensions of the screen, "canvas," will be used several times, so here are variables for it
cWidth = 650
cHeight = 475
resolution = (650, 475)

# The ball's position will be variable.
# Set the initial position to the middle of the screen
ballX = 325
ballY = 237

ballWidth = 39
ballHeight = 71

# Use dx, dy notation for the rate of change of the position of the ball
dx = 5
dy = 2

# Set up paddle
paddleLength = 71
paddleWidth = 10
# Initial position for the paddle is bottom right with this math
paddleX = (cWidth-paddleWidth)
paddleY = (cHeight-paddleLength)
# Start off with the paddle not moving
paddleDY = 0

#variable for tracking if a key is being held or not
keypressed = False

# Create a window surface object
canvas = pygame.display.set_mode(resolution)
# You can set a caption at the top of the window
pygame.display.set_caption("Piggie Pong")

# Now we begin the "stuff that's done every game loop."

# game loop
while True:
    # set the text for the score display
    # the arguments are the string of what to display,
    # 1 to have smooth edges,
    # and the RGB to display the text in
    scoreText = myFont.render("Score = "+str(score), 1, (0,0,0))

    # Track how many catches and misses there are
    # Three of either ends the game (either as a win or a loss)
    if score == 3:
        print("You win!", score, misses)
        pygame.quit()
        sys.exit()
    if misses == 3:
        print("Sorry, try again!", score, misses)
        pygame.quit()
        sys.exit()
        
    # for loop to handle the events
    for event in pygame.event.get():
        # Method #1 for closing the window: closing by clicking the X
        if event.type == QUIT:
            pygame.quit() # quit is the opposite of init
            sys.exit()
                
        # Now we're going to check for other events:
        if event.type == KEYDOWN:
            # Move paddle using up and down arrows
            if event.key == K_DOWN:
                paddleDY = 5
            if event.key == K_UP:
                paddleDY = -5
            keypressed = True
            
        if event.type == KEYUP:
            keypressed = False

    # The ball constantly moves every frame
    ballX += dx
    ballY += dy

    # move the paddle if the key is being held down and the potential move is in range
    if keypressed == True and (paddleY + paddleDY) < (cHeight-paddleLength) and (paddleY + paddleDY) >= 0:
        paddleY += paddleDY

    # Check for the ball going outside the screen and make it reverse direction if so
    if ballX >= (cWidth-ballWidth) or ballX <= 0:
        dx = -dx
        # Check for the ball hitting the paddle and increment the score if so
        if ballX >= (cWidth-ballWidth):
            if ballY + ballHeight >= paddleY and ballY <= (paddleY + paddleLength):
                score += 1
            else:
                misses += 1
                
    # Reverse the direction of the ball if it starts to go out of range        
    if ballY > (cHeight-ballHeight) or ballY < 0:
        dy = -dy
        
    # Draw the background and ball images and paddle rectangle
    canvas.blit(bkgrndImage, (0,0))
    canvas.blit(ball, (ballX, ballY))
    pygame.draw.rect(canvas, teal, (paddleX, paddleY, paddleWidth, paddleLength), 0)
    canvas.blit(scoreText, (5, 10))

    # Always update the display
    pygame.display.update()
