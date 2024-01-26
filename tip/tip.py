def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    strip_dollarsign = float(d.strip("$")) #can also .removeprefix() to remove $
    return strip_dollarsign

def percent_to_float(p):
    strip_percentage =float(p.strip("%"))/100 #can also use .removesuffix() to reomve %
    return strip_percentage


main()