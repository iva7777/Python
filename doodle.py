import turtle
t = turtle.Turtle()
t.hideturtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
colors = ('yellow', 'red', 'pink', 'cyan', 'lightgreen', 'maroon')

for i in range(150):
    t.pencolor(colors[i%6])
    t.circle(190 - i / 2.9)
    t.lt(90)
    t.circle(190 - i / 2.9)
    t.lt(90)
    t.circle(190 - i / 3.9)
    t.lt(60)

turtle.done()