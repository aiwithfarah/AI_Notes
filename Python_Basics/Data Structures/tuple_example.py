# An ordered collection of items that cannot be changed (immutable)
# Why use it? It's faster than a list and safer for data that shouldn't change,
# like days of the week or geographic coordinates.
# The Rule: If you try to change it: coordinates[0] = 50, Python will give you a TypeError.

# A tuple of coordinates (x, y)
coordinates = (10, 20)

print(coordinates[0])  # Prints 10
