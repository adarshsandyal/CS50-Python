
items={}
while 1:
    try:
        grocery = input().upper()
        if grocery:
            items[grocery]=items.get(grocery, 0) +1
    except EOFError:
        break
    
sort = dict(sorted(items.items()))
for i , j in sort.items():
    print(f"{j} {i}")
