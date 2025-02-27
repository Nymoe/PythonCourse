#Let's get it !
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.


chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Choose a letter\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for letter in chosen_word:
#     if letter == guess:
#         print("True")
#     else:
#         print("False")

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# display = []
#
# for letter in chosen_word:
#     display.append("_")


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# position = 0
# for letter in chosen_word:
#     if letter == guess:
#         display[position] = letter
#     position += 1

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# print(display)

#TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
display = []
lives = 6
correct_guess = False

for letter in chosen_word:
    display.append("_")

while display.count("_") > 0 and lives > 0:
    guess = input("Choose a letter\n").lower()
    position = 0
    correct_guess = False
    for letter in chosen_word:
        if letter == guess:
            display[position] = letter
            correct_guess = True
        position += 1
    if not correct_guess:
        lives -= 1
    print(stages[lives])
    print(f"{display} \n")
if lives == 0:
    print(f"You lost...\nThe word is \"{chosen_word}\"")
else:
    print("You win !")

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.



# TODO-2: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."



# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.