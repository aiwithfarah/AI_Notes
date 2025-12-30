# Right now, your code runs in a straight line from top to bottom.
# But smart programs need to make choices. We call this Control Flow.

# ------------------------TASK-------------------------
# Let's build a Password Checker.

# The Goal:
# Create a variable called secret_password and set it to "open sesame".
# Ask the user to input a password.
# If the user's input matches the secret password, print "Access Granted".
# Else (if it doesn't match), print "Access Denied".

secret_password = "open sesame"
user_password = input("Enter the password: ")

if user_password == secret_password:
    print("Access Granted!")
else:
    print("Access Denied")
