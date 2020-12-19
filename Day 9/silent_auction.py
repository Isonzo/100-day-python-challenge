import os

from silent_auction_art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


auction_record = {}


def check_highest_bidder(auction_record):
    highest_bid = 0
    for bidder in auction_record:
        bid_amount = auction_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Highest bidder was {winner} at ${highest_bid}.")



end_of_auction = False


print(logo)

print("Welcome to the secret auction!")

while not end_of_auction:
    name = input("\nInput your name: ")

    bid = int(input("\nInput your bid: $"))

    auction_record[name] = bid

    decision = input("\nAre there more bidders? (type yes or no)\n").lower()

    if decision == "no":
        end_of_auction = True

    clear()

check_highest_bidder(auction_record)
