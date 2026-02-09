name = input("Enter your name: ")
print(f"Hello {name}") #Hello          farah  

# .Strip() --> removes whitespace from string
name = name.strip()

print(f"Hello, {name}") #Hello, farah

# Capitalize's users name
name = name.capitalize()
print(f"Hello, {name}")
#Hello, Farah

#Capitalize first letter of each word
name = name.title() #farah rubena
print(f"Hello, {name}")
#Hello, Farah Rubena

# Chaining methods
name = name.strip().title() #     farah ruBena    
print(f"Hello {name}")
#Hello Farah Rubena        

# .split() --> Splits a string (on space) into a list of substrings seperated by commas 
sentence = "Hello my name is farah"
print(sentence.split())
# ['Hello', 'my', 'name', 'is', 'farah']
