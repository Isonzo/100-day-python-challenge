import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(player.hop, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_spawn_timer()
    car_manager.move_cars()
    if player.finish():
        car_manager.increase_speed()
        player.reset_position()
        scoreboard.increase_level()

# CHECK FOR COLLISION

    for car in car_manager.carlist:
        if car.distance(player) <= 20:
            print("Game Over")
            scoreboard.game_over()
            game_is_on = False
            car.pensize(10)
            car.pendown()

while not game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
