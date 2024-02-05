import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(8000)
t.color("purple")
a = 20

def motion():
    for i in range(4):
        t.forward(a)
        t.left(90)
def love():
    for i in range(75):
        motion()
        t.left(2)
        global a
        a = a + 2.5
    for i in range(75):
        motion()
        t.left(2)
        a = a - 2.5
t.penup()
t.left(75)
t.sety(150)
t.pendown()
love()
turtle.done()