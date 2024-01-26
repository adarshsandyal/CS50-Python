while 1:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    try:
        date = input("Date: ")
        dateparts = date.split()
        if len(dateparts)==3:
            month, day, year =dateparts
            if day.isdigit():
                raise ValueError
            else:
                day= day.strip(',')
            month= month.capitalize()
            if month in months:
                month = int(months.index(f"{month}")+1)
        elif len(dateparts)==1:
            month, day, year = dateparts[0].split('/')
            if month.isdigit():
                month = int(month)
            else:
                raise ValueError
        day= int(day)
        year=int(year)
        if 0 < day > 31 or 0 < month > 12 :
            raise ValueError
        else: break
    except ValueError:
        print("Invalid date")
        pass
print(f"{year:04d}-{month:02d}-{day:02d}")
