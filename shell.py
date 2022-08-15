import turtle

t = turtle.Turtle()

list1 = ["purple", "red", "light green", "pink", "orange", "blue", "aqua", "green", "cyan", "yellow"]
turtle.bgcolor("black")

for i in range(300):
    t.color(list1[i%10])
    t.pensize(2)
    t.forward(i)
    t.left(10)
    t.right(80)