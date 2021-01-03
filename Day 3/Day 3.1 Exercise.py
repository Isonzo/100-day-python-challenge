while True:
    try:
        number = int(input("Type the number you want to check here.\n"))
        remainder = number % 2
        break
    except:
        print("Hey shitass, you have to input a number")



if remainder == 0:
    print(f"{number} is even!")
else:
    print(f"{number} is odd!")
