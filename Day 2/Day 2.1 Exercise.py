while True:
    number = input("Type a two digit number\n")
    if len(number) == 2:
        break
    else:
        print("Hey dumbass, type a TWO digit number, nothing more, nothing less.")
        pass

sum = int(number[0]) + int(number[1])

print("The sum of their two digits is " + str(sum) + ".")
