camelCase = input("camelCase: ")
empty =""
for ind, value in enumerate(camelCase):
    if value.isupper():
        empty= empty + "_" + value.lower()
    else:
        empty = empty+value
print(empty)
