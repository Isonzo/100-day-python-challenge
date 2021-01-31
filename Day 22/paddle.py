from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self = Turtle("square")

        self.color("white")

        self.left(90)

        self.shapesize(stretch_wid=(1), stretch_len=(5))

        self.penup()

        self.goto(position)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)
