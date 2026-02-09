def main():

    x = int(input("What is X: "))
    y = int(input("What is Y: "))

    result = safe_ratio(x,y)
    print(f"The ratio is {result}")

def safe_ratio(x,y):

    return x/y if y else 0.0 

main()