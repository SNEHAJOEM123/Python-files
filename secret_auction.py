print("Welcome to the Secret Auction")

choice="yes"
bids={}

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        if bidding_record[bidder]>highest_bid:
            highest_bid=bidding_record[bidder]
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while choice=="yes":
    name=input("What is your name?:")
    price=int(input("What is your bid?: $"))
    bids[name]=price
    choice=input("Are there any other bidders? Type 'yes' or 'no'")
find_highest_bidder(bids)


