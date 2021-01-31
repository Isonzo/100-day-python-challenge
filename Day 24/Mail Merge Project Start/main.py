# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as f:
    raw_names = f.readlines()

names = []
for name in raw_names:
    name = name.strip("\n")
    names.append(name)
print(names)

with open("Input/Letters/starting_letter.txt") as f:
    letter_template = f.read()

for name in names:
    final_letter = letter_template.replace("[name]", name)
    filepath = "Output/ReadyToSend/Letter_to_" + name
    with open(filepath, mode="w") as f:
        f.write(final_letter)
