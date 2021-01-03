row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#get coordinates
vertical = int(position[1]) - 1
horizontal = int(position[0]) -1

#print map with "X"
map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")
