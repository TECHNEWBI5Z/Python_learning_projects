import random

# Game images for rock, paper, scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of game images
game_images = [rock, paper, scissors]

# Variable to control the game loop
end_game = False

while not end_game:
    choice1 = input("What option will you choose? 0 for rock, 1 for paper, 2 for scissors and 'Q' for quit:\n")

    if choice1 == 'Q':
        # End the game if the user wants to quit
        end_game = True
        print("Thanks for playing! Goodbye.")
        continue

    try:
        choice1 = int(choice1)
        if choice1 < 0 or choice1 > 2:
            print("Invalid choice. Please choose 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number (0, 1, 2) or 'Q' to quit.")
        continue

    # Display user's choice
    print(f"You chose:\n{game_images[choice1]}")

    # Generate the computer's choice
    choice2 = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[choice2]}")

    # Determine the winner
    if choice1 == choice2:
        print("It's a draw.")
    elif (choice1 == 0 and choice2 == 2) or (choice1 == 1 and choice2 == 0) or (choice1 == 2 and choice2 == 1):
        print("You've won!")
    else:
        print("You've lost.")
