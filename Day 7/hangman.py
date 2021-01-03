import random

import hangman_art

import word_list

word_list = word_list.word_list

print(hangman_art.logo)

stages = hangman_art.stages

lives = 6

display = []

word = random.choice(word_list)

#print(f"Psst, the answer is {word}")


for _ in word:
    display += "_"

print(f"{' '.join(display)}")

end_of_game = False

while not end_of_game:
    guess = input("\nGuess a letter\n").lower()

    if guess in display:
        print(f"you already guessed {guess}.")

    for position in range (len(word)):
        if guess == word[position]:
            display[position] = guess

    if guess not in word:
        lives -=1
        print(f"Sorry, {guess} is not in the word. You lose a life")
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(stages[lives])
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

input("\n\nPress anything to quit.\n")
