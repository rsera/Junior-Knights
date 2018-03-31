import turtle

radius = 100
rotation = 126
turtle.speed(0)
turtle.pendown()
numCircles = 21

for i in range(numCircles):
    # set a different color and size, alternating every three circles
    if(i<6):
        turtle.pencolor("dark green")
        turtle.pensize(2)
    elif(i<12):
        turtle.pencolor("purple")
        turtle.pensize(2)
    else:
        turtle.pencolor("brown")
        turtle.pensize(2)
    #draw the circle
    turtle.circle(radius)
    #rotate the pen
    turtle.right(rotation)

