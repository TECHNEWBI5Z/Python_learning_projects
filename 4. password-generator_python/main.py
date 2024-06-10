import random

# Lists of characters to be used in the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message and input prompts for user
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for char in range(1, nr_letters + 1):
#    password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#    password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#    password += random.choice(numbers)
# print(password)

# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Create a list to hold the characters for the password
password_list = []

# Add the required number of letters to the password list
for char in range(nr_letters):
    password_list.append(random.choice(letters))

# Add the required number of symbols to the password list
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add the required number of numbers to the password list
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Print the password list before shuffling (for debugging)
print(password_list)

# Shuffle the characters in the password list to randomize the order
random.shuffle(password_list)

# Print the password list after shuffling (for debugging)
print(password_list)

# Convert the password list into a single string
password = ""
for char in password_list:
    password += char

# Print the final password
print(f"Your password is: {password}")
