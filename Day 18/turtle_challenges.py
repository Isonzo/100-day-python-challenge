from turtle import Turtle, Screen

import random


turtle = Turtle()
turtle.shape("turtle")

# Challenge 1: A square

# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# Challenge 2: Dashed line

# for _ in range(10):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# Challenge 3: Different shapes

# for sides in range(4, 11):
#     angle = 360/sides
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     turtle.color(R, G, B)
#     for _ in range(sides):
#         turtle.forward(85)
#         turtle.right(angle)

# Challenge 4: Random walk

# turtle.pensize(10)
# turtle.speed("fastest")
#
#
# def random_angle():
#     directions = [0, 90, 180, 270]
#     return random.choice(directions)
#
#
# while True:
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     turtle.color(R, G, B)
#     turtle.right(random_angle())
#     turtle.forward(40)

# Challenge 5: Spirograph}

turtle.speed("fastest")
angle = 5


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


for _ in range(72):
    turtle.color(random_color())
    turtle.circle(150)
    turtle.right(angle)

screen = Screen()
screen.exitonclick()
