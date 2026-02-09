huge_number = 1000000000000.0
tiny_number = 0.0000000000001

result = huge_number + tiny_number

print(f"Result {result}") #1000000000000.0
print(f"Did it change? {result != huge_number}") #False