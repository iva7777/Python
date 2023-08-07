import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
def design():
    h = 0
    n = 10
    for i in range(290):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 1 / n
        t.pencolor('black')
        t.pensize(2)
        t.rt(89)
        t.circle(i,159,steps=1)
        t.fillcolor(c)
        t.begin_fill()
        t.rt(208)
        t.bk(20)
        t.circle(i,290,steps=1)
        t.end_fill()
    for y in range(26):
        t.penup()
        t.goto(0,0)
        t.down()
        t.color(c)
        t.rt(19)
        t.circle(i,346,steps=1)
        t.rt(80)

design()
t.done()