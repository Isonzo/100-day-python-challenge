from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def input_coins():
    """Allows user to input coins and returns the total value"""
    quarters = int(input("Input amount of quarters: "))*0.25
    dimes = int(input("Input amount of dimes: "))*0.1
    nickels = int(input("Input amount of nickels: "))*0.05
    pennies = int(input("Input amount of pennies: "))*0.01

    return quarters + dimes + nickels + pennies


is_on = True

menu = Menu()


money_machine = MoneyMachine()

coffee_machine = CoffeeMaker()

while is_on:
    prompt = input("What would you like? Espresso ($1.50), Latte ($2.50), Cappuccino ($3.00) : ").lower()

    if prompt == "off":
        quit()

    elif menu.find_drink(prompt) != None:
        pass    
        if menu.is_resource_sufficient(prompt):
            order.name = prompt
            payment = input_coins()
