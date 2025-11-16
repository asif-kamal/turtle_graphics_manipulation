#####Turtle Intro######

import turtle as t


timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############

timmy_the_turtle.pendown()
timmy_the_turtle.pencolor("green")

# for _ in range(4):
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.right(90)

# for _ in range(25):
#     timmy_the_turtle.pu()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pd()
#     timmy_the_turtle.forward(5)

#triangle
for _ in range(3):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360/3)

#square
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360/4)

#pentagon
for _ in range(5):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360/5)

#6-sided
for _ in range(6):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360/6)

#7-sided
for _ in range(7):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360/7)

#octagon
for _ in range(8):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360/8)

#nonagon
for _ in range(9):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360/9)

#decagon
for _ in range(10):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360/10)

t.exitonclick()
