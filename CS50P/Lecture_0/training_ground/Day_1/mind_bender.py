# 1. Create a list (The Object) and put a label 'a' on it
a = [1,2,3]

# 2. Put label 'b' on the SAME object as 'a'
b = a

# 3. Change the object using label 'b'
b.append(4)

# print a
# If 'a' was a separate box, it should still be [1, 2, 3].
print(a) #[1, 2, 3, 4]

# id() shows the actual memory address (where it lives in RAM).
print(f"Address of a {id(a)}")
print(f"Address of b {id(b)}")

# Address of a 2656645004544
# Address of b 2656645004544

