def date_check():
    date = input("Enter the Date : ")
    
    dates = date.split('/')
    
    day = int(dates[0])
    month = int(dates[1])
    year = int(dates[2])
    
    if month not in range(1,13):
        print("Invalid Month")
        return
    
    if month in (4,6,9,11) and (day < 1 or day > 30):
        print("Invalid Date ")
        return
    if month not in (2,4,6,9,11) and (day < 1 or day > 31):
            print("Invalid Date ")
            return
    
    is_leap = False
    
    if year % 400 == 0 or year % 4 == 0 and year %100 != 0:
        is_leap = True
    if (month == 2 and is_leap == True) and (day <1 or day > 29 ):
        print("Cannot be more than 29 days !")
    
    if (month == 2 and is_leap == False) and (day < 1 or day >28 ):
        print("Not a leap Year, days cannot be more than 28")
    
    all_months = ("January", "Februray","March","April", "May", "June", "July", "August", "September", "October", "November", "December")
    
    month_name = all_months[month - 1]
    
    
    print(f"{month_name} {day}, {year}")
    
date_check()