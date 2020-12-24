import random

from art import logo, vs

from game_data import data

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def higher_lower():
    score = 0

    game_not_lost = True

    def pick_celebrity():
        """Picks a random celebrity from data"""
        return random.choice(data)

    def extract_data(x_data):
        """Returns name, follower, description, and country. To be paired with pick_celebrity()"""
        name = x_data["name"]
        follower = x_data["follower_count"]
        description = x_data["description"]
        country = x_data["country"]
        return name, follower, description, country

    def compare(choice, a_is_bigger):
        if choice == "a" and a_is_bigger:
            return True

        elif choice == "b" and not a_is_bigger:
            return True

        else:
            return False



    while game_not_lost:
        print (logo)

        if score != 0:
            print(f"Your current score is {score}")

        #Assign A and B

        a_data = pick_celebrity()

        b_data = pick_celebrity()

        while a_data == b_data:
            a_data = pick_celebrity()
            b_data = pick_celebrity()

        a_name, a_follower, a_description, a_country = extract_data(a_data)

        b_name, b_follower, b_description, b_country = extract_data(b_data)








        print(f"Compare A: {a_name}, a {a_description}, from {a_country}")
        print(vs)
        print(f"Against B: {b_name}, a {b_description}, from {b_country} ")

        choice = input("Which one has more followers? 'A' or 'B'? ").lower()

        a_is_bigger = a_follower > b_follower

        if compare(choice, a_is_bigger):
            score += 1
            clear()
        else:
            game_not_lost = False
            break

    clear()
    print (logo)
    print(f"You were wrong. You've lost.Your final score was {score}")
    play_again = input("Press 'y' to start again or 'n' to quit.").lower()

    if play_again == "y":
        clear()
        higher_lower()

higher_lower()
