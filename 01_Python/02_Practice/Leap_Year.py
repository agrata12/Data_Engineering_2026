# Write a program that returns True or False whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# This is how you work out whether if a particular year is a leap year. 
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder 
# - unless the year is also divisible by 400 with no remainder   
# If English is not your first language, or if the above logic is confusing, try using this flow chart.

# e.g. The year 2000: 

# 2000 ÷ 4 = 500 (Leap)  
# 2000 ÷ 100 = 20 (Not Leap)  
# 2000 ÷ 400 = 5 (Leap!)  
# So the year 2000 is a leap year. 

def leap_year(check_year):
    if check_year % 400 == 0:
        return True
    elif check_year % 100 == 0:
        return False
    elif check_year % 4 == 0:
        return True
    else:
        return False


year = int(input("Enter year to check if it is a leap year: "))

output = leap_year(year)

if output == True:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")