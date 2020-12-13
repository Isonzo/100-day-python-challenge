print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure, while avoiding CBT (Cock and ball torture).\n\n")

print("During your journey to find that which you most crave, you find yourself lost.")
print("In front of you is an intersection, and you can choose to go either left or right.")
print("On the right, an alluring smell catches your attention, but the leftmost path is more discreet.")
intersection = input("Which path should you choose? (left or right)\n")

if intersection.lower() == "left":
    print("\nYou do not let yourself be distracted by that sweet aroma, and you trudge left into an alleyway\n")
    print("Suddenly, you find yourself near a queue for free cock and ball examinations by a licensed professional\n")
    cock_check = input("Should you go get checked? Or is it just a fiend to perform CBT? (Y or N)\n")

    if cock_check.lower() == "y":
        print("\nYou decide to wait in queue for the free cock and ball examination.\n.\n.\n.\nHours pass.\n.\n.\n. \nDays pass\n.\n.\n.\n It's almost your turn. You look ahead, and see that the professional is actually examining some harlot commit CBT!\nThe shock of having misread the sign gives you a heart attack and the medical professional, too engrossed in observing CBT, does not come to your aid.\n\nYou died.")

    else:
        print("You know your cock and balls well enough to know that they're perfectly fine, and you don't need to expose them to someone who may want to do some CBT on you.")
        print("Finally, you reach your destination, the holy magazine stand. There stands 3 magazines, and you may pick one")
        print("However, you realize that a sign near the stand says 'now stocking CBT'.\nThis means you must be careful to not choose the incorrect magazine!")
        choice = input("\nThere's a red magazine, a blue magazine, and a yellow magazine. Which one should be chosen? (red, blue, or yellow)\n")

        if choice.lower() == "yellow":
            print("\nYou hungrily open the magazine, and you find the holy treasure: CVT (Clit and Vagina Torture). \nNow you can go home and relax\n\nYou win!")

        elif choice.lower() == "blue":
            print("\nYou hungrily open the magazine, but you find yourself looking at tortured balls. \n\nThe horror!\n\nA passerby sees you looking at that, and being a well-intentioned citizen, assumes you're into CBT and crushes your balls with a rock.\n\nYou died")

        elif choice.lower() == "red":
            print("\nYou hungrily open the magazine, but find yourself looking at a tortured cock \n\nThe tragedy!\n\nThe clerk, upon seeing that you will take away his most prized possesion, challenges you to a duel. Before you can react, he pulls out a fun and shoots your cock.\n\nYou died")

        else:
            print(f"\nYou always knew not learning the basic colours would spell doom for you one day. That day is today.\n\nBeing unable to choose a relevant colour, instead opting for {choice}, you had a stroke. \n\nYou died.")
else:
    print("\nOh no! That sweet scent was actually a devious fiend trying to lure you for CBT! \nYou try to shield your cock and balls but unfortunately they are crushed by a massive rock\n\nYou died.")
