import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_of_bankers = len(names)

chosen = names[random.randint(0, number_of_bankers - 1)]

print(f"\nSorry {chosen}, your time (with your wallet) is up.")
