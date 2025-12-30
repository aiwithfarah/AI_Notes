# If a VECTOR is a single lit of numbers(like a row in excel)
# MATRIX is a whole spreadsheet (row and columns)
# In Python, we create a matrix by putting lists inside a list.
# Structure: [[Row 1], [Row 2], [Row 3]]


# TASK: Create a variable called grades using np.array() that holds both of these rows?

# Imagine we have the test scores for 2 students on 3 different exams.

# Student A: [85, 90, 75]

# Student B: [70, 80, 95]
import numpy as np

student_A = [85, 90, 75]
student_B = [70, 80, 95]

grades = np.array([student_A, student_B])
print(grades)

# [[85 90 75]
#  [70 80 95]]
