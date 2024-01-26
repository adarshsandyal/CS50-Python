def main():
    mass = int(input("Enter mass: "))
    calculate(mass)


def calculate(m):
    c= 300000000 #speed of light in m/s
    Energy = m*c*c
    print(f"Energy: {Energy}") #we can use print(f."energy: {energy:, }") for commas in output .2f to limit decimal digits

main()