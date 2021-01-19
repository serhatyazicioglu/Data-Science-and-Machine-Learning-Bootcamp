# Drawing a spiral using the Turtle library

import turtle

def make_spiral():
    turtle.clearscreen()
    t = turtle.Turtle()
    t.shape("turtle")
    turtle_color = input("choose turtle's color")
    turtle_speed = int(input("choose turtle's speed"))

    t.color(turtle_color)
    t.speed(turtle_speed)

    t.fillcolor(turtle_color)
    t.begin_fill()

    for i in range(75):
        t.forward(i)
        t.right(30)

    t.hideturtle()
    t.end_fill()


make_spiral()
