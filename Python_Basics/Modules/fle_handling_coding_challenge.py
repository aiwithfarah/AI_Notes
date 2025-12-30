# CODING CHALLENGE
# Ask the user for their name (input).
# Use with open... and the Append mode ("a") to open a file named "guestbook.txt".
# Write the user's name into the file. (Don't forget to add "\n" after the name so the next person starts on a new line!).
# Bonus: After writing, open the file again in Read mode ("r") and print everything inside to prove it worked.

user_name = input("Enter your name: ")

with open('guestbook.txt', 'a') as file:
    file.write(f'{user_name}\n')

with open('guestbook.txt', 'r') as file:
    content = file.read()
    print(content)
