from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race? (Choose a color of the rainbow)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=(-125+(index*50)))
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"The winner was {winning_color}, you've won!")
            else:
                print(f"The winner was {winning_color}, not {user_bet.lower()}! You've lost.")
        distance = random.randint(0, 5)
        turtle.forward(distance)

screen.exitonclick()
