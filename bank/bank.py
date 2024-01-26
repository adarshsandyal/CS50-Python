def main():
    greeting = input("Greeting: ")
    split(greeting)

def split(greet):
    greet = greet.strip().lower()
    if greet.startswith("hello"):
        print("$0")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
