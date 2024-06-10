import random
from art import logo

print(logo)

# Constants for the number of turns
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Checks the user's guess against the actual answer and returns the remaining turns."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Congratulations! You've got it right. The answer is {answer}.")
        return 0


def set_difficulty():
    """Sets the difficulty level and returns the number of turns."""
    level = input("Choose a difficulty 'easy' or 'hard':\n").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# Generate a random answer between 1 and 100
answer = random.randint(1, 100)

# Set the number of turns based on difficulty
turns = set_difficulty()

guess = 0
# Loop until the user guesses the correct answer or runs out of turns
while guess != answer and turns > 0:
    print(f"You have {turns} attempts remaining to guess the number.")

    # Get the user's guess
    guess = int(input("Make a guess: "))

    # Check the user's guess and update the number of turns remaining
    turns = check_answer(guess, answer, turns)

    # If no turns are remaining, the user loses
    if turns == 0:
        print("You've run out of guesses, you lose.")
    elif guess != answer:
        print("Guess again.")
