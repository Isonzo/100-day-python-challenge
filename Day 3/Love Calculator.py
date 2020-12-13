print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

#TRUE count
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

#LOVE count
l = name.count("l")
o = name.count("o")
v = name.count("v")
e2 = name.count("e")


true = str(t + r + u + e)
love = str(l + o + v + e2)
print(true)
print(love)

true_love = int(true + love)



if true_love <= 10 or true_love >= 90:
    print(f"Your love score is {true_love}, you go together like coke and mentos.")
elif 40 < true_love < 50:
    print(f"Your love score is {true_love}, you are alright together")
else:
    print(f"Your love score is {true_love}")
