# No Duplicates Allowed: If you add the same thing twice, it ignores the second one.
# Unordered: The items don't have a fixed position (no index [0]).
# Syntax: Curly braces {} (like a dictionary, but just values, no colons :).
# Creating a set

ids = {101, 102, 103, 101}  # Notice 101 is there twice

print(ids)
# Output: {101, 102, 103}  <-- Duplicate removed!

# Common Use Case: Quickly removing dupes from a list
names = ['Alex', 'Bon', 'Alex']
print(set(names))  # {'Alex', 'Bon'}


# --------CODING CHALLENGE---------
# Create a list called guests with these names (including duplicates): ["Alice", "Bob", "Alice", "Charlie", "Bob"].
# Print the original list.
# Convert the list into a Set to remove duplicates and print the set.
# Hint: unique_guests = set(guests)
# (Bonus) Create a Tuple containing the coordinates (90.0, 180.0) and print it.

guests = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
print(guests)
unique_guests = set(guests)
print(unique_guests)
tup = (90.0, 180.0)
print(tup)

# ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
# {'Charlie', 'Alice', 'Bob'}
# (90.0, 180.0)
