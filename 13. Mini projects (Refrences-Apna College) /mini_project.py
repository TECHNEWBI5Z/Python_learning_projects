
# -------------------------------------------------------------------------------------------------------------------
# 1. guess number game
# -------------------------------------------------------------------------------------------------------------------
import random  # Import the random module to generate a random number

# Generate a random number between 1 and 100 (inclusive)
target_num = random.randint(1, 100)

# Keep looping until the user guesses the correct number or quits the game
while True:
    guess = input("Guess the number or type 'Q' to quit: ")  # Prompt the user to guess the number or quit
    if guess.upper() == 'Q':  # Check if the user wants to quit (case-insensitive)
        print("You are out of the game. Goodbye!")  # Inform the user that they quit the game
        break  # Exit the loop if the user quits

    guess = int(guess)  # Convert the user's input to an integer
    if guess == target_num:  # Check if the user's guess matches the target number
        print("Correct guess! Congratulations!")  # Inform the user that they guessed the correct number
        break  # Exit the loop if the user guesses correctly
    elif guess < target_num:  # Check if the user's guess is less than the target number
        print("Your guess is too low.")  # Inform the user that their guess is too low
    else:  # If the guess is not equal to or less than the target number
        print("Your guess is too high.")  # Inform the user that their guess is too high

print("Game over")  # Display "Game over" when the game ends



# -------------------------------------------------------------------------------------------------------------------
# 2. generate Random passwords
# -------------------------------------------------------------------------------------------------------------------


# Variables containing all the characters in list format for random.choice

# uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# symbols = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
import random
import string

# Define the character set for the password (letters, punctuation, and digits)
character_set = string.ascii_letters + string.punctuation + string.digits

# Specify the desired password length
password_length = 12

# Initialize an empty string to store the generated password
password = ""

# Generate the password using a loop
for i in range(password_length):
    # Append a random character from the character set to the password string
    password += random.choice(character_set)

# Print the generated password
print(password)

# Alternatively, you can use list comprehension to generate the password
# Define the character set for the password (letters, punctuation, and digits)
character_set = string.ascii_letters + string.punctuation + string.digits

# Specify the desired password length
password_length = 12

# Generate the password using list comprehension
password_list = [random.choice(character_set) for i in range(password_length)]

# Convert the list of characters to a string
password = "".join(password_list)

# Print the generated password
print(password)

