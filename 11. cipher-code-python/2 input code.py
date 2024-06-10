# List of alphabets to use in the Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# User input for direction (encode/decode), message, and shift number
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Function to encrypt plain text using the Caesar cipher
def encrypt(plain_text, shift_amount):
    cipher_text = ""  # Variable to store the encrypted text
    for letter in plain_text:
        if letter in alphabet:  # Check if the character is an alphabet
            position = alphabet.index(letter)  # Find the position of the letter in the alphabet
            new_position = (position + shift_amount) % 26  # Calculate the new position after shifting
            new_letter = alphabet[new_position]  # Get the new letter from the alphabet
            cipher_text += new_letter  # Append the new letter to the cipher text
        else:
            cipher_text += letter  # If the character is not an alphabet, keep it unchanged
    print(f"The encoded text is {cipher_text}")

# Function to decrypt cipher text using the Caesar cipher
def decrypt(cipher_text, shift_amount):
    plain_text = ""  # Variable to store the decrypted text
    for letter in cipher_text:
        if letter in alphabet:  # Check if the character is an alphabet
            position = alphabet.index(letter)  # Find the position of the letter in the alphabet
            new_position = (position - shift_amount) % 26  # Calculate the new position after shifting
            new_letter = alphabet[new_position]  # Get the new letter from the alphabet
            plain_text += new_letter  # Append the new letter to the plain text
        else:
            plain_text += letter  # If the character is not an alphabet, keep it unchanged
    print(f"The decoded text is {plain_text}")

# Ensure the shift number is within the range of the alphabet (0-25)
shift %= 26

# Check if the direction is 'encode' or 'decode' and call the respective function
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_amount=shift)
