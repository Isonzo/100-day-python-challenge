student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

code_data = pandas.read_csv("nato_phonetic_alphabet.csv")

code = {row.letter:row.code for (index, row) in code_data.iterrows()}

def nato_input():
    word = input("Enter a word\n").upper()
    try:
        result = [code[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters of the english alphabet")
        nato_input()
    else:
        print(result)
        nato_input()
nato_input()
