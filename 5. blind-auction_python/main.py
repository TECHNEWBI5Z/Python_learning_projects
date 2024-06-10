from replit import clear
from art import logo

# Display the logo
print(logo)

# Dictionary to store the bids
bids = {}

# Flag to control the bidding process
end_of_bids = False

def find_highest_bidder(bidding_record):
    """Finds the highest bidder from the bidding record."""
    highest_bid = 0
    winner = ""
    # Iterate over the bidding record to find the highest bid
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Loop to collect bids until there are no more bidders
while not end_of_bids:
    # Get the name and bid price from the user
    name = input("What is your name?\n")
    bid_price = int(input("What is your bid price?\n"))
    # Store the bid in the bids dictionary
    bids[name] = bid_price
    # Ask if there are any other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    # If no more bidders, find the highest bidder and end the loop
    if should_continue == "no":
        end_of_bids = True
        find_highest_bidder(bids)
    # If there are more bidders, clear the screen for the next bidder
    elif should_continue == "yes":
        clear()
