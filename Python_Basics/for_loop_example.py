# A FOR loop allows you to repeat an action for every item in a collection.

inventory = [1, 2, 3]
for item in inventory:
    print(item)

# item: This is a temporary variable. You can name it anything (x, thing, weapon). It holds the current item being processed.
# inventory: The list we are looping through.
# The Action: Everything indented here happens to every item, one by one.

# ----RANGE Function-----------
# Sometimes you just want to loop a specific number of times, not through a list.
# Python has a helper called range().
# range(5) creates a sequence: 0, 1, 2, 3, 4. (Stops before the number!)

for number in range(3):
    print("Hip Hip Hooray!")

# Hip Hip Hooray!
# Hip Hip Hooray!
# Hip Hip Hooray!

# ------------CODING TASK--------------
# Create a list called loot containing: "Gold Coin", "Dagger", "Ruby".
# Write a for loop that goes through the list.
# Inside the loop, print: "You found a [item name]!

loot = ["Gold Coin", "Dagger", "Ruby"]

for item in loot:
    print(f"You found a {item}")

# You found a Gold Coin
# You found a Dagger
# You found a Ruby
