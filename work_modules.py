import turtle
import random

turtle.shape('turtle')
turtle.pensize(2)
turtle.speed('fastest')

turtle.pencolor('red')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.pencolor('green')
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.pencolor('blue')
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
for i in range(5):
    turtle.forward(100)
    turtle.right(72)

turtle.penup()
turtle.goto(-50, -150)
turtle.pendown()

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.goto(-50, -150)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()

turtle.fillcolor('red')
turtle.begin_fill()
for _ in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.pendown()

for _ in range(36):
    turtle.pencolor(random.randint(0,255)/255, random.randint(0,255)/255, random.randint(0,255)/255)
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)

turtle.done()