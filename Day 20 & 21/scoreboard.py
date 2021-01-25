from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.update_score()

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
