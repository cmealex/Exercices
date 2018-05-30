import turtle

myt = turtle.Turtle()
myt.speed(0)


def square(length, angle):
    for i in range(4):

        myt.forward(length)
        myt.right(angle)

for i in range(30):

    square(100, 90)
    myt.right(10)


