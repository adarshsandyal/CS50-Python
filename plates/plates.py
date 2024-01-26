def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s.isalnum():
        return False
    if not 2<= len(s) <=6:
        return False
    if not s[0:2].isalpha():
        return False
    indx = 0
    while indx < len(s):
        if s[indx].isalpha() == False:
            if s[indx] == "0":
                return False
            else:
                break
        indx += 1
    s= s.strip('1234567890')
    if not s.isalpha():
        return False
    return True
main()