
def main():

    bio = input("Enter your bio: ")
    x = clean_bio(bio)
    print(x)

def clean_bio(bio):

    if not bio or not bio.strip():
        return "Missing"
    
    return bio.strip()


main()