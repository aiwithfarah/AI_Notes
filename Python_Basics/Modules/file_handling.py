# So far, all our data lives in the variables. When you turn off the program,
#  the data disappears. Poof! 💨
# To save data permanently (like a high score or a save file),
# we need to write it to a File on your hard drive.

# FILE MODES
# "r" = Read (Open existing file to see what's inside).
# "w" = Write (Create a new file or overwrite an existing one).
# "a" = Append (Add text to the end of an existing file).

# WITH OPEN
# You can open a file and then remember to .close() it later.
# But if your program crashes before closing, the file might get corrupted.
# The with statement is a "Context Manager."
# It automatically closes the file for you, no matter what.

# TASK
# WRITING to a file
# This creates "diary.txt" and writes text into it

with open('diary.txt', 'w') as file:
    file.write("Dear Diary, \n")
    file.write("I learned Python today")

# reading a file
with open('diary.txt', 'r') as file:
    content = file.read()
    print(content)

# Careful with "w"! If you open an existing file with "w", Python wipes it clean before writing.
# If you want to add to it, use "a" (append).
