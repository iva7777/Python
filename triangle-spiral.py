import turtle
colors = ['aqua', 'green', 'yellow', 'aqua', 'green', 'yellow']
t = turtle.Pen()
t.hideturtle()
t.speed(0)
turtle.bgcolor('white')

for x in range(400):
    t.pencolor(colors[x % 6])
    t.width(x // 15 + 1)
    t.forward(x)
    t.left(122)

turtle.done()