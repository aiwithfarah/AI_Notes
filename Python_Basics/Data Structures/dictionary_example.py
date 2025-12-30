# Key : Value pairs
# Syntax: We use curly braces {} and colons :.
# To access value we pass the key name
# Adding/Updating: It's the same syntax!
#     If the key exists, Python updates the value.
#     If the key does not exist, Python creates a new pair.


# --------CODING CHALLENGE--------
# Create a dictionary called person.
# Add these keys and values inside it:
# "first_name": (Put your name)
# "last_name": (Put your last name)
# "job": "Python Student"
# Print the following sentence using the dictionary values: "[first_name] [last_name] is a [job]." (Hint: Use an f-string f"{variable}..."!)

person = {
    'first_name': 'farah',
    'last_name': 'rubena',
    'job': 'failing entepreneur'
}

print(f'{person['first_name']} {person['last_name']} is a {person['job']}')
# farah rubena is a failing entepreneur
