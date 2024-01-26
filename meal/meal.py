def main():
    time= input("What time is it? ")
    t = convert(time)
    X(t)



def X(t):
    if 7.0 <= t <= 8.0:
        print("breakfast time")
    elif 12.0 <= t <= 13.0 :
        print("lunch time")
    elif 18.0 <= t <= 19.0:
        print("dinner time")
    else:
        print()

def convert(time1=0.0):
    hours, minutes = time1.split(":")
    time2 = float(hours) + int(minutes)/60 #converts minutes in deciaml format
    time2 = float(time2)
    return time2
if __name__ == "__main__":
    main()
