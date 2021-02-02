with open("file1.txt") as f:
    numbers_1 = f.readlines()

with open("file2.txt") as f:
    numbers_2 = f.readlines()


result = [int(n) for n in numbers_1 if n in numbers_2]
# Write your code above 👆

print(result)
