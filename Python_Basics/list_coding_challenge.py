# Create an empty list called inventory. (Hint: inventory = [])
# Use .append() to add "Sword" to the list.
# Use .append() to add "Potion" to the list.
# Use .append() to add "Shield" to the list.
# Print the inventory.
# The hero drinks the potion! Use .remove() to delete "Potion".
# Print the final inventory.

inventory = []
inventory.append('Sword')
inventory.append('Potion')
inventory.append('Shield')
print(inventory)  # ['Sword', 'Potion', 'Shield']
inventory.remove('Potion')
print(inventory)  # ['Sword', 'Shield']
