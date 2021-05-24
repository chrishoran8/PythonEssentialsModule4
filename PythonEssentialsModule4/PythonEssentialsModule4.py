def is_year_leap(year):
    retValue = None
    if year % 4 == 0 :
        retValue = True
    else:
        retValue = False
        
    if year % 100 ==0:
        if year % 400 == 0:
            retValue = True
        else: 
            retValue = False
    return retValue


def days_in_month(year, month):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    retValue = days[month-1]
    if is_year_leap(year) and month==2:
        retValue = 29
    return retValue

def day_of_year(year, month, day):
    totalDays = 0
    for i in range (month):
        totalDays = totalDays + days_in_month(year,i)
    return totalDays

print(is_year_leap(3))
print(days_in_month(1900,2))

print(day_of_year(1999, 12, 31))