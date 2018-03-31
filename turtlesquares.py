import turtle
import random

def square():
    for i in range(4):
        turtle.pendown()
        turtle.forward(50)
        turtle.right(90)

def spiralSquare(color):
    length = 5
    numLayers = 100
    colors = ["red", "black", "green", "yellow", "blue", "purple"]
    turtle.speed(0)

    for i in range(numLayers):
        turtle.pendown()
        turtle.forward(length)
        turtle.right(90)
        length = length + 5
        if(color == True):
            turtle.pencolor(colors[random.randint(0,5)])

spiralSquare(True)
    
