from turtle import Turtle

class StateManager:
    def __init__(self):
        self.guess_list = []

    def draw_state(self, x, y, name):
        if name not in self.guess_list:
            state = Turtle()
            state.hideturtle()
            state.penup()
            state.goto(x, y)
            state.write(name)
            self.guess_list.append(name)
