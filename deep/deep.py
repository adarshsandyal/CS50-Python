question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

match question:
    case "fortytwo" | "forty two" |"42" |"forty-two" | "forty 2" | "forty_two" | "forty -two" :
        print("Yes")
    case _:
        print("No")