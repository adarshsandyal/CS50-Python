def main():
    expression = input("Expression: ")
    a, sign, c = expression.split()
    A = calculate(float(a), sign, float(c))
    print(f"A: {A:.1f}")

def calculate(x, operator , z):
    if (operator == "+"):
        return x+z
    elif(operator == "-"):
        return x-z
    elif(operator == "*"):
        return x*z
    elif operator =="/" :
        if z == 0:
            print("Division by zero is not allowed.")
            quit()
        else:
            return x/z
main()
