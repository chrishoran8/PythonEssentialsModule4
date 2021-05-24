#from an earlier lab
def strange_list_fun(n):
    strange_list = []    
    for i in range(0, n):
        strange_list.insert(0, i)    
    return strange_list

#print(strange_list_fun(5))


#labs for 4.3.1.6 - 4.3.1.8

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

#print(is_year_leap(3))
#print(days_in_month(1900,2))
#print(day_of_year(1999, 12, 31))



#4.3.1.9 LAB
def is_prime(num):
    for i in range(3,num-1):
        if num%i == 0:
            return False
    return True
            
#test case    
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()