due= 50
while due>0:
    cents = int(input("Insert coin: "))
    if cents in [25, 10, 5]:
        due -= cents
    if due> 0:
        print("Amount Due:", due)
    else:
        change = abs(due)
        print("Change Owed:", change)