from turtle import Turtle, Screen

player = Turtle()
screen = Screen()


def move_forwards():
    player.forward(10)


def move_backwards():
    player.backward(10)


def turn_right():
    player.right(10)


def turn_left():
    player.left(10)


def clear():
    player.reset()



screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkeypress(clear, "c")
screen.exitonclick()
