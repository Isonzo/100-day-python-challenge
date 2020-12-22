############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from art import logo

import random

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def blackjack():
    computer_hand = []

    player_hand = []

    player_win = False
    comp_win = False
    comp_lose = False

    def deal_card(player):
        player.append(random.choice(cards))

    def start_game():
        for _ in range(2):
            deal_card(computer_hand)
            deal_card(player_hand)


    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    will_to_play = input("\nDo you want to play blackjack? 'y' or 'n'\n").lower()

    if will_to_play == "n":
        quit()



    start_game()

    #Player Turn
    while True:
        clear()
        player_score = sum(player_hand)
        print(f"Dealer's first card: {computer_hand[0]}")
        print(f"Your cards: {player_hand}. Your current score is {player_score}")

        #Natural Blackjack Check
        if sum(player_hand) == 21 and len(player_hand) == 2:
            player_win = True
        else:
            player_win = False

        hit_me = input("Would you like another card? 'y' or 'n'\n").lower()
        if hit_me == "y":
            deal_card(player_hand)
        else:
            break

        if sum(player_hand) > 21 and 11 in player_hand:
            ace = player_hand.index(11)
            player_hand[ace] = 1
        elif sum(player_hand) > 21:
            print("Bust! You went over 21.")
            print(f"Dealer's cards: {computer_hand}, score = {sum(computer_hand)}")
            print(f"Your cards: {player_hand}, score = {sum(player_hand)}\n")

            input()
            clear()
            blackjack()

    #Computer Turn
    print("Now it's the dealer's turn...")
    while True:
        if sum(computer_hand) < 17:
            deal_card(computer_hand)

        elif sum(computer_hand) < sum(player_hand):
            deal_card(computer_hand)

        elif sum(computer_hand) == 21 and len(computer_hand) == 2:
            comp_win = True
            break

        elif sum(computer_hand) == 21:
            break

        elif sum(computer_hand) > 21 and 11 in computer_hand:
            ace = player_hand.index(11)
            computer_hand[ace] = 1
        elif sum(computer_hand) > 21:
            comp_lose = True
            break
        else:
            break

    #Score Comparison

    if comp_win and player_win:
        print("You both had a natural blackjack. \nWhat incredible odds! \nIt's still a draw though.\n")

    elif comp_win:
        print("Rats! The dealer had a natural blackjack.\n")

    elif player_win:
        print("You had a natural blackjack! You win!\n")

    elif comp_lose:
        print("Dealer bust. You win!\n")

    elif sum(player_hand) > sum(computer_hand):
        print("You win!\n")

    elif sum(player_hand) < sum(computer_hand) and not comp_lose:
        print("You lose.\n")

    else:
        print("I guess it's a draw...\n")

    print(f"Dealer's cards: {computer_hand}, score = {sum(computer_hand)}")
    print(f"Your cards: {player_hand}, score = {sum(player_hand)}\n")

    input()
    clear()
    blackjack()



blackjack()
