import turtle

radius = 100
rotation = 126
turtle.speed(0)
turtle.pendown()

for i in range(20):
    # set a different color and size, alternating every three circles
    if(i%3==1):
        turtle.pencolor("dark green")
        turtle.pensize(2)
    elif(i%3==2):
        turtle.pencolor("purple")
        turtle.pensize(2)
    else:
        turtle.pencolor("brown")
        turtle.pensize(2)
    #draw the circle
    turtle.circle(radius)
    #rotate the pen
    turtle.right(rotation)

