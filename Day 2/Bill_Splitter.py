print("Welcome to the bill calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people are splitting the bill? "))

bill_tip = bill * (1 + tip/100)

pay = round(bill_tip/people, 2)

pay = "{:.2f}".format(pay)

print(f"Everyone should pay ${pay}")
