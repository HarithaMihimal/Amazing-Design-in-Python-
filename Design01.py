import turtle
turtle.bgcolor("black")

square = turtle.Turtle()
square.speed(20)
square.pencolor("white")
for i in range(400):
    square.forward(i)
    square.right(91)
