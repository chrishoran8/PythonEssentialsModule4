
#labs for 4.3.1.6 - 4.3.1.8

def is_year_leap(year):
    #return true if leap year
    modByFour = year%4
    modByHundred = year % 100
    modByfourHundred = year % 400
    if year <1582:
        #print("Not within greg cal")
        return False
    elif modByFour != 0: # not divisible by four? 
        #print("common year") #common year
        return False
    elif modByHundred != 0: # not divisible by 100? 
        #print("leap year") # leap year
        return True
    elif modByfourHundred != 0: #not divisible by 400?
        #print("common year")
        return False
    else:
        #print("leap year")
        return True
    
    #just in case
    return False


def days_in_month(year, month):
    retValue = 0
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    retValue = days[month-1] #that will change normal month index, to our month index
    if is_year_leap(year) and month ==2:
        retValue = 29
    return retValue

def day_of_year(year, month, day):
    if(month>12):
        return None
    #if the days are greater than the month allows
    if day > days_in_month(year,month):
        return None
    
        
    totalDays = 0 #this tracks the total days added so far
    for i in range(month-1):
        totalDays = totalDays + days_in_month(year,i+1)
    return totalDays + day

print(day_of_year(2001, 2, 29))


#print(is_year_leap(3))
#print(days_in_month(1900,2))
#print(day_of_year(1999, 12, 31))



#4.3.1.9 LAB
def is_prime(num):
    for i in range(2,num-1):
        if num%i == 0:
            return False
    return True
            
#test case    
for i in range(1, 200):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


