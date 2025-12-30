# A single variable that holds multiple items in a specific order.
# Computers start counting at 0, not 1 and lists are 0 indexed (first element is at 0 position)

fruits = ["Apple", "Banana", "Cherry"]

print(fruits[0])  # Prints "Apple"
print(fruits[1])  # Prints "Banana"
print(fruits[2])  # Prints "Cherry"


# ------------LIST METHODS---------------
# specific tasks list
tasks = ["Homework", "Clean room"]

# Adding a task
tasks.append("Walk the dog")
print(tasks)
# Output: ['Homework', 'Clean room', 'Walk the dog']

# Removing a task
tasks.remove("Homework")
print(tasks)
# Output: ['Clean room', 'Walk the dog']
