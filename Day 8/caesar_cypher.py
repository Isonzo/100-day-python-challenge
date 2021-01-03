alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import caesar_art

print(caesar_art.logo)


def caesar(direction, text, shift):
    end_text = ""
    shift %= 26
    for letter in text:
        if letter not in alphabet:
            end_text += letter
            continue

        position = alphabet.index(letter)

        if direction == "encode":
            new_position = position + shift
            if new_position > 26:
                new_position -= 26
        elif direction == "decode":
            new_position = position - shift
            if new_position < 0:
                position += 26
        end_text += alphabet[new_position]
    print(f"Your {direction}d message is: {end_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    restart = input("\nWould you like to restart the program? type 'yes' or 'no'\n").lower()
    if restart != "yes":
        break
