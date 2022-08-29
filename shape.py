import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.hideturtle()
t.pensize(3)
t.speed(0)

n = 36
h = 0
t.goto(-60, 0)
for i in range(20):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.pencolor(c)
    t.circle(105, 103)
    t.backward(98)
    t.right(60)
    t.circle(70, 68)
    t.left(87)
    t.backward(108)
    t.forward(150)
r = 110
t.penup()
t.goto(0, -67)
t.pendown()
for j in range(100):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.pencolor(c)
    t.circle(r + j, 20)

turtle.done()