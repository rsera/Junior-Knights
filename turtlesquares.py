import turtle
import random

length = 5
numLayers = 100
colors = ["red", "black", "green", "yellow", "blue", "purple"]
turtle.speed(0)

for i in range(numLayers):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(90)
    length = length + 5
    turtle.pencolor(colors[random.randint(0,5)])

    
