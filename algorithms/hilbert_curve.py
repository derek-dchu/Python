"""
Draw hilbert curve using turtle module.
"""


import turtle


class Mover:
    def __init__(self, t, l):
        self.t = t
        self.l = l

    def move(self, d):
        if d == "UP":
            self.t.left(90)
            self.t.fd(self.l)
            self.t.right(90)
        elif d == "RIGHT":
            self.t.fd(self.l)
        elif d == "LEFT":
            self.t.bk(self.l)
        else:
            self.t.right(90)
            self.t.fd(self.l)
            self.t.left(90)


def hilbert_curve(n, size):
    padding = 10
    # line length
    l = (size - padding*2) / (2**n)
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=size, height=size, startx=0, starty=0)
    t.penup()
    t.setpos(-size/2+padding, size/2-padding)

    mover = Mover(t, l)
    t.pendown()
    helper(n, mover)
    screen.exitonclick()

def helper(n, mover, d="UP"):
    if n == 1:
        if d == "LEFT":
            mover.move("RIGHT")
            mover.move("DOWN")
            mover.move("LEFT")
        elif d == "RIGHT":
            mover.move("LEFT")
            mover.move("UP")
            mover.move("RIGHT")
        elif d == "UP":
            mover.move("DOWN")
            mover.move("RIGHT")
            mover.move("UP")
        else:
            mover.move("UP")
            mover.move("LEFT")
            mover.move("DOWN")
    else:
        if d == "LEFT":
            helper(n-1, mover, "UP")
            mover.move("RIGHT")
            helper(n-1, mover, "LEFT")
            mover.move("DOWN")
            helper(n-1, mover, "LEFT")
            mover.move("LEFT")
            helper(n-1, mover, "DOWN")
        elif d == "RIGHT":
            helper(n-1, mover, "DOWN");
            mover.move("LEFT");
            helper(n-1, mover, "RIGHT");
            mover.move("UP");
            helper(n-1, mover, "RIGHT");
            mover.move("RIGHT");
            helper(n-1, mover, "UP");
        elif d == "UP":
            helper(n-1, mover, "LEFT");
            mover.move("DOWN");
            helper(n-1, mover, "UP");
            mover.move("RIGHT");
            helper(n-1, mover, "UP");
            mover.move("UP");
            helper(n-1, mover, "RIGHT");
        else:
            helper(n-1, mover, "RIGHT");
            mover.move("UP");
            helper(n-1, mover, "DOWN");
            mover.move("LEFT");
            helper(n-1, mover, "DOWN");
            mover.move("DOWN");
            helper(n-1, mover, "LEFT");


if __name__ == '__main__':
    hilbert_curve(2, 500)



