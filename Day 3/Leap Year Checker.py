year = int(input("Enter year to learn if it is a leap year\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year")
