# List of alphabets to use in the Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, direction_cae):
    """
    Encrypts or decrypts the input text using the Caesar cipher technique.
    """
    end_text = ""
    # If decoding, reverse the shift amount
    if direction_cae == "decode":
        shift_amount *= -1
    
    # Iterate through each letter in the input text
    for letter in start_text:
        # Only shift letters, leave other characters unchanged
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position % 26]
        else:
            end_text += letter
    # Print the final result of encryption or decryption
    print(f"Here's the {direction_cae}d result: {end_text}")

# Print the ASCII art title
print('''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')

# Initialize the loop control variable
should_end = False

# Loop to repeatedly ask the user for input until they decide to stop
while not should_end:
    # Ask the user whether to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Ask the user for the text to process
    text = input("Type your message:\n").lower()
    # Ask the user for the shift number
    shift = int(input("Type the shift number:\n"))

    # Ensure the shift number is within the range of the alphabet
    shift = shift % 26

    # Call the caesar function with the user's input
    caesar(start_text=text, shift_amount=shift, direction_cae=direction)

    # Ask the user if they want to go again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
