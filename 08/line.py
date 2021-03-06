import turtle
import random
from math import cos, sin, radians


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(20)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


# def draw_line_basic(p1, p2):
#     draw_big_point(p1)
#     draw_big_point(p2)
#
#     x1, y1 = p1[0], p1[1]
#     x2, y2 = p2[0], p2[1]


def draw_line(a, b):
    # draw_big_point(a)
    # draw_big_point(b)
    for i in range(0, 100 + 1, 20):
        t = i / 100
        x = (a[0] - b[0]) * cos(radians(t)) + b[0] * cos(t * (a[0] / b[0] - 1))
        y = (a[1] - b[1]) * sin(radians(t)) - b[1] * sin(t * (a[1] / b[1] - 1))
        k = a[1] / b[1]
        draw_point((x, y))

    prepare_turtle_canvas()
    draw_line((250, 100), (250, 100))


prepare_turtle_canvas()
draw_line((-200, -100), (300, 150))

turtle.done()
