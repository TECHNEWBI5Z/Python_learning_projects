# LET'S begin
# Solution
import random

stages = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# Condition to end the game
end_game = False

# Word list
word_list = ["Faizan", "Furqan", "Zeeshan", "Ali", "Arhaan", "Ayan", "Ahemad"]

# Random choice of word by the system and the function .lower() is used to convert the word into lowercase
word = random.choice(word_list).lower()

# Use len function to start coding
ran_word = len(word)

# In the game we are giving two options: 1. Win and 2. Lose
lives = 6

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|

""")
# In code "display" function is used for "-" symbol
# whereas "position" is used to give the position of the word
# Creation of _ (blank) symbol in a random word
display = []
for _ in range(ran_word):
    display += "_"

# While loop to run the game loop asks the user to guess the letter again & again
while not end_game:
    guess = input("Guess a letter: ").lower()

    # 1. IF GUESS IS IN WORD = THEN WHAT TO DO?
    if guess in display:
        print(f"The chosen letter is already in the word: {guess}")

    # For loop to check the letter in the random word
    for position in range(ran_word):
        letter = word[position]
        # Position the letter in the blank symbol
        if letter == guess:
            display[position] = letter

    # 2. IF GUESS IS NOT IN WORD = THEN WHAT TO DO?
    if guess not in word:
        print("The chosen letter is not in the word, so you lose a life.")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")

    # Merge all the guessed words in the blank symbol
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You won")
    print(stages[lives])
