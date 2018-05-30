import turtle
myt = turtle.Turtle()
# myt.speed(0)

def curvemove():
    for i in range (200):
        myt.right(1)
        myt.forward(1)

    # color('red')
    # be

myt.color('red', 'red')
myt.begin_fill()
myt.left(140)
myt.forward(111)
curvemove()
myt.left(130)
curvemove()
myt.forward(111)
myt.end_fill()
