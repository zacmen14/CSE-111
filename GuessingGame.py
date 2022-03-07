# 1. Name: 
#    -Zachary Mencl-
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    -This program is meant to ask the user for a value, have the computer pick a random number 
#     from 1 up to that value inputed by user, and then have the user guess the number the computer picked.-
# 4. What was the hardest part? Be as specific as possible.
#    -This assingment I felt definetly made me had to go back and look over everything that I learned in CSE 110, and I still had to ask for help at the tutuor
# center. One of the terms I did not understand was the word Sentinal, so I assumed it meant the code I was going to use to set up the program. I also had to figure
# out how to enter in my variables into scentences and totally forgot how to do that. I think the hardest part of this whole assignment was trying to remember how to
# add variables to a list and have the program print said variables in list. -
# 5. How long did it take for you to complete the assignment?
#    -This assignment took me about two hours and a half hours, I had to go back and look over all of my previous assignments and had to look up how to reenter variables
# into lists. I also had to figure out how to send this assigment in by downloading an app on my computer that would let me show my screen and my face. That also
# took me about a half hour.-  

import random

# Game introduction
print('This is the "Guess a Number" game.')
print("You try to guess a random number in the smallest number of attempts.")
# Prompt the user for how difficult the game will be. Ask for an integer
value_max = int(input("Pick a positivie integer: "))
# Generate a random number between 1 and the chosen value
value_random = random.randint(1, value_max)
# Give the user instructions as to what he or she will be doing
print("Guess a number between 1 and " + str(value_max) + ".")

# Initialize the sentinal and the array of guesses

guess_num = 0
Total_guesses = []

# Play the guessing game

    # Prompt the user for a number
while guess_num != value_random:
    guess_num =int(input("> "))

    # Store the number in an array so it can be displayed later
    Total_guesses.append(guess_num)

    # Make a decision: was the guess too high, too low, or just right
    if guess_num > value_random:
        print("         Too High!")
        print()
    elif guess_num < value_random:
        print("         Too Low!")
        print()
# Give the user a report: How many guesses and what the guesses where
print("You were able to find the number in " + str(len(Total_guesses)) + " guesses.")
print("The numbers you guessed were: " + str(Total_guesses))