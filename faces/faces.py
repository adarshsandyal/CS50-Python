def main():
    text=input("what do you wanna say? ") #getting input from user
    picture= convert(text)
    print(picture)


def convert(emoji):
    A = emoji.replace(":)","🙂")
    B = A.replace(":(","🙁")
    return B
main()
