from art import logo

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

import random



def generate_number():
    """Returns a random number from 1 to 100"""
    return random.randint(1, 101)

def choose_difficulty():
    """Returns 5 for 'hard', and 10 for 'easy'"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.\n").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        choose_difficulty()

def compare(guess, number):
    if guess == number:
        print(f"You {guess} was the correct number!\nYou win!\n")
        input()
        numberguesser()
    elif guess > number:
        print(f"{guess} is too high, guess again\n")
        return 1
    elif guess < number:
        print(f"{guess} is too low, guess again\n")
        return 1
    else:
        print("Something went horribly wrong")

def numberguesser():
    play = input("Would you like to play Number Guesser? 'y' or 'n'").lower()

    if play == "n":
        quit()

    clear()

    print(logo)

    number = generate_number()

    print("I'm thinking of a number between 1 and 100...")

    tries = choose_difficulty()

    while tries > 0:
        print(f"You have {tries} guesses remaining.\n")
        guess = int(input())
        tries -= compare(guess, number)
    print(f"You've run out guesses! You lose. The number was {number}")
    numberguesser()



numberguesser()
