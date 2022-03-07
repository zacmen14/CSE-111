# 1. Name: 
#    Justyn Mencl

# 2. Assignment Name: 
#    Lab 01: Python Review

# 3. Assignment Description:
#    A program that will allow the user to guess a number between 1 and a chosen
#    value with prompts to help them make their next guess.

# 4. What was the hardest part? Be as specific as possible.
#    This assignement was not overly difficult but there were a few things that didn't really make sense to me. I have never heard the term sentinal
#    before so I had to google it. There wasn't any clear documentation so I just assumed that it was the variable in relation to the loop and moved 
#    on with my life. The instructions were pretty clear and I was able to follow them aside from that one part. Where you probably wrote the template
#    I will make sure to ask specifically in class. I had to think about each reqirement for the template and really visualize what element could solve
#    that part of the program. Watching the loop and the random number generator come together after some trial and error was really satisfying and I 
#    feel like this assignment really helped my self-esteem as a novice programmer. Overall I enjoyed this assignment and look forward to the following one.

# 5. How long did it take for you to complete the assignment?
#    This assignment took me about an hour and a half to 2 hours. I had to google a few things but the program itself took maybe an hour to create. Figuring out 
#    the screen recording and the youtube channel took roughly 30 minutes and writing this summary took about 15 minutes. I am only estimating but overall I feel 
#    like I gave this assignment the amount of time it deserved.

import random

# Game introduction
print('This is the "guess a number" game.')
print("You try to guess a random number in the smallest number of attempts.")
print()

# Prompt the user for how difficult the game will be. Ask for an integer
value_max = int(input("Pick a positive integer: "))

# Generate a random number between 1 and the chosen value
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing
print("Guess a number between 1 and " + str(value_max) + ".")

# Initialize the sentinal and the array of guesses
guess = 0
guesses = []

# Play the guessing game

    # Prompt the user for a number
while guess != value_random:
    guess = int(input(">  "))
    

    # Store the number in an array so it can be displayed later
    guesses.append(guess)

    # Make a decision: was the guess too high, too low, or just right
    if guess > value_random:
        print("         Too High!")
        print()
    elif guess < value_random:
        print("         Too Low!")
        print()
    
        

# Give the user a report: How many guesses and what the guesses where
print("You were able to find the number in " + str(len(guesses)) + " guesses.")
print("The numbers you guessed were: " + str(guesses))