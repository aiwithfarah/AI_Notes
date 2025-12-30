# Python comes with "batteries included."
# This means it has a massive library of pre-written code that you can use immediately.
#  These are called Modules.
# COMMON MODULES
# random: For picking random numbers or choices (great for games!).
# math: For advanced math (square roots, pi, etc.).
# time: For adding delays or checking the time.

import random

# print number between 1 and 10
secret_num = random.randint(1, 10)
print(f"The secret number is {secret_num}")

# pick a random item from a list
choices = ["Rock", "Paper", "Scissors"]
user_choice = random.choice(choices)
print(f"User Choice : {user_choice}")
