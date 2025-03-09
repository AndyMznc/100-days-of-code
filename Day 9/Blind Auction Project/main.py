# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added


def compare_highest_bid(bidder):
    highest_bid = 0
    # name_of_highest_bidder = ""

    if bid > highest_bid:
        highest_bid = bid
        # name_of_highest_bidder = name


bidder = {}
still_continue = True
while still_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    more_bidder = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    bidder[name] = bid
    compare_highest_bid(bidder)

    if more_bidder == "no":
        still_continue = False
        print(bidder)
        # print("The winner is a with a bid of $11")


# TODO-4: Compare bids in dictionary
