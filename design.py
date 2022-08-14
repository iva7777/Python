import turtle
import math

colors = ["red", "purple", "blue", "green", "orange", "yellow"]
pen = turtle.Pen()
turtle.bgcolor("black")
pen.speed(200)

for x in range(360):
    pen.pencolor(colors[x % 6])
    pen.width(x * 10/100 + 1)
    pen.left(97)
    pen.forward(x - 10)
    pen.backward(x)
    pen.right(90)