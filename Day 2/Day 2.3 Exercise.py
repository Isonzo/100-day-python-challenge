age = input("What is your age? ")
t_age = input("How many years do you expect to live?")

target_age = int(t_age)

current_age = int(age)

difference = target_age - current_age

days = round(difference * 365.25)

weeks = round(difference * 52.142)

months = round(difference * 12)

print(f"You have:\n\n{days} days left\n{weeks} weeks left\n{months} months left\n\nAssuming you survive to {target_age} years old")
