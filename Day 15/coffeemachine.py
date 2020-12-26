from menu import MENU

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

water = 0

milk = 200

coffee = 100

money = 0.0


def can_make_coffee(order, water, milk ,coffee):
    """Returns True if there are enough resources for coffee"""
    for ingredient in MENU[order]["ingredients"]:
        if ingredient == "water" and MENU[order]["ingredients"][ingredient] >= water:
            print(f"Unfortunately, there is not enough water for a {order}")
            return False

        elif ingredient == "milk" and MENU[order]["ingredients"][ingredient] >= milk:
            print(f"Unfortunately, there is not enough milk for a {order}")
            return False

        elif ingredient == "coffee" and MENU[order]["ingredients"][ingredient] >= coffee:
            print(f"Unfortunately, there is not enough coffee for a {order}")
            return False

    return True

def input_coins():
    """Allows user to input coins and returns the total value"""
    quarters = int(input("Input amount of quarters: "))*0.25
    dimes = int(input("Input amount of dimes: "))*0.1
    nickels = int(input("Input amount of nickels: "))*0.05
    pennies = int(input("Input amount of pennies: "))*0.01

    return quarters + dimes + nickels + pennies

def make_coffee(order):
    global water, milk, coffee
    for ingredient in MENU[order]["ingredients"]:

         if ingredient == "water":
             water -= MENU[order]["ingredients"][ingredient]

         elif ingredient == "milk":
             milk -= MENU[order]["ingredients"][ingredient]

         elif ingredient == "coffee":
             coffee -= MENU[order]["ingredients"][ingredient]




def coffee_machine():
    global money

    prompt = input("What would you like? Espresso ($1.50), Latte ($2.50), Cappuccino ($3.00) : ").lower()

    if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":

        if can_make_coffee(prompt, water, milk, coffee):

            payment = input_coins()

            if payment >= MENU[prompt]["cost"]:
                money += MENU[prompt]["cost"]
                change = payment - MENU[prompt]["cost"]
                make_coffee(prompt)
                print(f"Enjoy your {prompt}, and take your ${round(change, 2)} of change")
                input()
                clear()
                coffee_machine()

            else:
                print("You don't have enough money for this drink, unfortunately")
                input()
                clear()
                coffee_machine()


        else:
            input()
            clear()
            coffee_machine()


    elif prompt == "off":
        quit()

    elif prompt == "report":
        print(f"Currently, there is:\n    Water: {water} \n    Milk: {milk}\n    Coffee: {coffee} \n    Money: {money}")
        coffee_machine()
coffee_machine()
