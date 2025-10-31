# -----------------------------------------------
# Hangman Game
# This program chooses a random word from a list.
# The player must guess letters one by one.
# The game ends when the player guesses the word
# or makes 6 wrong guesses.
# Concepts used: random, while loop, if-else, strings, lists.
# -----------------------------------------------
import random

words = ["python", "hangman", "variable", "function", "algorithm"]
word = random.choice(words)

max_wrong = 6
wrong_guesses = 0
guessed = []

print("Welcome to Hangman!")

while wrong_guesses < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display)
    print("Guessed letters:", guessed)
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    
    letter_input = input("Enter a letter: ").lower()
    
    if letter_input in guessed:
        print("You already guessed that letter!")
        continue
    
    guessed.append(letter_input)
    
    if letter_input in word:
        print("Yes! Correct letter.\n")
    else:
        print("No! Wrong letter.\n")
        wrong_guesses += 1
    
    finished = True
    for letter in word:
        if letter not in guessed:
            finished = False
            break
    if finished:
        print("Congratulations! You guessed the word:", word)
        break
else:
    print("Game Over! The word was:", word)
