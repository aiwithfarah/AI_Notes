# if-elif-else
#following elif statement(s) are only checked (ont by one) if IF evaluates to False
#the moment any statement returns True, it exits the loop 

x = int(input("What's X: "))
y = int(input("What's Y: "))

if x > y :
    print('X is Greater')
elif x < y:
    print("X is Smaller")
else:
    print("X is equal to Y") 

