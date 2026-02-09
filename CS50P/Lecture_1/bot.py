
def main():

    feeling = input("How are you feeling?: ").strip().lower()
    is_feeling(feeling)
    
def is_feeling(feeling):
    match feeling:

        case "happy":
            print("Listen to this Tech Podcast")
        case "sad":
            print("Knocky-Knocky")
        case "angry":
            print("Take a deep breath")
        case _:
            print("Hmmmm")

main()