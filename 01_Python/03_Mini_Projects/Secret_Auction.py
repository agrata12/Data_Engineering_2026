print(""""
                         
                            ______
                           (____  )________
                            /      \       )
                           /________\_____/
                               |  |
                               |  |
                         ______|  |______
                        (________________)
""")
print("Welcome to the Secret Auction!")

def find_highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")

bids={}
continue_bidding=True
while continue_bidding:
    name=input("What is your name? ")
    price=int(input("What is your bid? $"))
    bids[name]=price
    should_continue=input("Are there any more bidders? Yes or no?\n ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)

# more_bidders=input("Are there any more bidders? Yes or no? ").lower()
# while more_bidders != "no":
#     name=input("What is your name? ")
#     bid=int(input("What is your bid? "))
#     secret_auction[name]=bid
#     more_bidders=input("Are there any more bidders? Yes or no? ").lower()

# print(secret_auction)
# highest_bid=0
# winner=""

# for key in secret_auction:
#     if  secret_auction[key] > highest_bid:
#         highest_bid=secret_auction[key]
#         winner=key
# print(f"{winner} wins the auction.")