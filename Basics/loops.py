# A for loop tells the computer: "Take this list, and for every single item inside it,
#  do the exact same thing."

import numpy as np
data = [10, 20, 30, 40, 50]

# Task: print every number in your data list
for number in data:
    print(number)
# 10
# 20
# 30
# 40
# 50


# Scalar Multiplication (Mathematical operation fundamental to Neural Networks)
# Imagine you have a digital photo that is too dark. To brighten it,
# you might want to double the value of every single pixel. In math, this is multiplying a Vector (the list of pixels)
# by a Scalar (the number 2).

print(data * 2)
# [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# In "pure" Python, lists behave like text strings. If you multiply the word "hello" by 2, you get "hellohello".
# Python does the exact same thing with lists—it just repeats the sequence.
# To do actual math (like multiplying every number inside the list),
#  we need a library designed for it. In AI, that library is NumPy (Numerical Python).
#  It is the backbone of almost all AI systems because it treats lists like mathematical vectors.

vector = np.array(data)  # converts list to a math vector (array)
print(vector * 2)  # [ 20  40  60  80 100]
# The missing commas are NumPy's way of telling you, "I am a mathematical vector
