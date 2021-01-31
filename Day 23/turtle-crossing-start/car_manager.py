from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_TIMER = 5


class CarManager:
    def __init__(self):
        self.carlist = []
        self.increment = 0
        self.car_timer = CAR_TIMER

    def make_car(self):
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_len=2)
        y_position = random.randint(-12, 13)
        car.goto(300, y_position*20)
        car.setheading(180)
        self.carlist.append(car)

    def car_spawn_timer(self):
        if self.car_timer > 0:
            self.car_timer -= 1
        else:
            self.car_timer = CAR_TIMER
            self.make_car()

    def move_cars(self):
        for car in self.carlist:
            car.forward(STARTING_MOVE_DISTANCE + self.increment)

    def increase_speed(self):
        self.increment += MOVE_INCREMENT
