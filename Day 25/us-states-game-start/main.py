import turtle
import pandas
from state_manager import StateManager

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True

state_manager = StateManager()

state_data = pandas.read_csv("50_states.csv")

states = state_data["state"].to_list()


while len(state_manager.guess_list) < 50:
    state_guess = screen.textinput(
                                f"{len(state_manager.guess_list)}/50 States guessed",
                                "What's another State's name?"
                                )

    state_guess = state_guess.capitalize()

    if state_guess == "Exit":
        break

    if state_guess in states:
        print("Hell yeah bro, you guessed correctly!")

        current_state = state_data[state_data.state == state_guess]
        state_manager.draw_state(float(current_state.x), float(current_state.y), state_guess)

ms = list(set(states) - set(state_manager.guess_list))

missing_states = pandas.Series(ms)

missing_states.to_csv("missed_states.csv")

screen.exitonclick()
