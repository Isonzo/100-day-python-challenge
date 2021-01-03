rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random


options = [rock, paper, scissors]

choice = int(input("Input 0 for rock, 1 for paper, or 2 for scissors.\n"))


cpu_choice = random.randint(0,2)

if cpu_choice == choice:
    print(f"You chose:\n{options[choice]}")
    print(f"The CPU chose:\n{options[cpu_choice]}")
    print("\nNo one wins")
else:
    if cpu_choice == 0 and choice == 1:
        print(f"You chose:\n{options[choice]}")
        print(f"The CPU chose:\n{options[cpu_choice]}")
        print("You win!")
    elif cpu_choice == 0 and choice == 2:
        print(f"You chose:\n{options[choice]}")
        print(f"The CPU chose:\n{options[cpu_choice]}")
        print("You lose")
    elif cpu_choice == 1 and choice == 0:
        print(f"You chose:\n{options[choice]}")
        print(f"The CPU chose:\n{options[cpu_choice]}")
        print("You lose")
    elif cpu_choice == 1 and choice == 2:
        print(f"You chose:\n{options[choice]}")
        print(f"The CPU chose:\n{options[cpu_choice]}")
        print("You win!")
    elif cpu_choice == 2 and choice == 0:
        print(f"You chose:\n{options[choice]}")
        print(f"The CPU chose:\n{options[cpu_choice]}")
        print("You win!")
    elif cpu_choice == 2 and choice == 1:
        print(f"You chose:\n{options[choice]}")
        print(f"The CPU chose:\n{options[cpu_choice]}")
        print("You lose")
    else:
        print("You picked an invalid number, you lose!")
