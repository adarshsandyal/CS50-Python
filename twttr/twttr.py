text= input("Input: ")
vowels = 'aeiouAEIOU'
strin = ""
for char in text :
    if char not in vowels:
        strin += char
print(f"Output: {strin}", end=" ", sep="")