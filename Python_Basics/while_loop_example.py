# The for loop is great when you know how many times you want to loop (like "for every item in this list").
# But what if you don't know the number? What if you want to loop until something happens?
# Enter the while loop

# If you ever get stuck in an infinite loop, press Ctrl + C in your terminal to force-stop it!


# # ----------------TASK---------------------
# Create a variable called mana and set it to 10.
# Write a while loop that runs as long as mana is greater than 0.
# Inside the loop:
# Print "Casting spell! Mana is now [current mana]"
# Subtract 2 from mana. (Hint: mana = mana - 2)
# After the loop finishes, print "Out of mana!".

mana = 10

while mana > 0:
    print(f"Casting spell! Mana is now {mana}")
    mana -= 2
print("Out of mana!")

# Casting spell! Mana is now 10
# Casting spell! Mana is now 8
# Casting spell! Mana is now 6
# Casting spell! Mana is now 4
# Casting spell! Mana is now 2
# Out of mana!
