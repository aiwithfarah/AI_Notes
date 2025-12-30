# In real software, you don't want the whole program to crash just because of one small error.
#  We use Try/Except blocks to catch errors gracefully.
# Concept: "Try to do this code. If it crashes, don't stop—just run this other code instead."


try:
    # dangerous code goes here
    age = int(input("Enter your age: "))
    print(f"You are {age} years old!")
except ValueError:
    # safety net goes here
    print('Oops! That is not a valid number!')

# --------CODING CHALLENGE--------
# Generate a random number between 1 and 10 (save it in a variable).
# Ask the user to input a guess.
# Use a try/except block to handle the user input:
# Inside try: Convert their input to an int. If it matches the random number, print "You won!". If not, print "Wrong guess."
# Inside except: If they typed text (like "five") instead of a number, print "Please enter a number only!"

import random

random_num = random.randint(1, 10)
user_guess = input("Guess the random number: ")
try:
    user_guess = int(user_guess)
    if user_guess == random_num:
        print("You Won!")
    else:
        print("Wrong Guess!")
except:
    print("Please enter a number only!")
