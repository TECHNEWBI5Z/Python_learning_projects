from art import logo, vs
from random import choice
from replit import clear
from game_data import data

print(logo)

# Initial score
score = 0

# Function to format account data
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

# Function to check if the guess is correct
def check_answer(guess, a_followers, b_followers):
    """Takes the account data and returns if the guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Starting point of the game
game_should_continue = True
account_b = choice(data)

while game_should_continue:
    # Assign account_a to the previous account_b
    account_a = account_b
    # Ensure the next account_b is different from account_a
    account_b = choice(data)
    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Get user's guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if the user's guess is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen
    clear()

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
