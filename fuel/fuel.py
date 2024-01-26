while True:
    try:
        x,y=map(int,input("Fraction: ").split('/'))
        if x < 0 or y <= 0 or x > y:
            raise ValueError
        fraction= round((x/y)*100)
        if 1< fraction<99:
            print(f"{fraction}%")
        elif 0<= fraction <=1:
            print("E")
        elif 99<= fraction<=100:
            print("F")
        else:
            raise ValueError
        break
    except(NameError, ValueError, ZeroDivisionError):
        pass
