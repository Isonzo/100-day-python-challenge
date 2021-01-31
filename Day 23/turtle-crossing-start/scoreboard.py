from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.level = 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_text()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
