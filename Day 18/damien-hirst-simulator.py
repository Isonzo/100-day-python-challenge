
from turtle import Turtle, Screen
import colorgram
import random


damien = Turtle()
damien.hideturtle()
screen = Screen()
screen.colormode(255)
damien.penup()
damien.setposition(-300, -250)
damien.speed("fastest")

colors = colorgram.extract("damien_hirst_source.jpg", 8)

color_list = []

for n in range(len(colors)):
    if colors[n].rgb[0] > 200 and colors[n].rgb[1] > 200 and colors[n].rgb[2] > 200:
        continue
    else:
        color_list.append(tuple(colors[n].rgb))

print(color_list)


def damien_hirst(width, height):
    vertical = -250
    rows = 0
    while rows != height:
        for _ in range(width):
            damien.color(random.choice(color_list))
            damien.dot(20)
            damien.forward(50)
        damien.penup()
        vertical += 50
        rows += 1
        damien.setposition(-300, vertical)


damien_hirst(5, 5)


screen.exitonclick()
