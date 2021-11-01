"""
#####################################################################
                       secret auction
#####################################################################
"""

from art import logo
# HINT: You can call clear() to clear the output in the console.

# create object to store name & bid_amount
all_bidders = {}

# function to find highest bidder


def find_highest_bidder(bidding_record):
    # bidding_record ex: {'jim': 123, 'tim': 321}
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:  # gives the key of everyone in bidding_record
        # gives access to the value from the key
        bid_price = bidding_record[bidder]
        # if bid price is greater than highest bid, highest bid becomes the bid price
        # winner is the bidder witht he highest bid
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder
    print(
        f'the winner with the highest bid is {winner} with a bid of ${highest_bid}')


# inputs asking for name and  bids
# using a while loop to keep track of all bidders
add_another_bidder = True  # variable to keep track of while loop

while add_another_bidder:
    bidder_name = input('What is your name?: ')
    bid_amount = int(input('How much would you like to bid? $'))
    add_bidder = input('Are there other bidders? Type: yes or no \n').lower()

    # storing the name and amount as key/value pair inside of all_bidders dictionary
    all_bidders[bidder_name] = bid_amount

    if add_bidder == 'no':
        add_another_bidder = False
       #  call the function and pass in the dictionary of bidders
        find_highest_bidder(all_bidders)
    elif add_bidder == 'yes':
        clear()
