import turtle

"""
setheading
0   - east
90  - north
180 - west
270 - south
"""
turtle.speed(10000000000000)


def move_up(steps=60):
    turtle.setheading(90)
    turtle.forward(steps)


def move_right(steps=60):
    turtle.setheading(0)
    turtle.forward(steps)


def move_down(steps=60):
    turtle.setheading(270)
    turtle.forward(steps)


def move_left(steps=60):
    turtle.setheading(180)
    turtle.forward(steps)


for i in range(4):

    for i in range(4):

        move_down(60)
        move_right(60)
        move_up(60)
        move_left(60)
        move_right(60)

        for i in range(60):
            move_right(1)
            move_down(60)
            move_up(60)

    move_down(60)

    for i in range(4):

        move_down(60)
        move_left(60)
        move_up(60)

        for i in range(60):
            move_left(1)
            move_down(60)
            move_up(60)

    move_down(60)

turtle.done()