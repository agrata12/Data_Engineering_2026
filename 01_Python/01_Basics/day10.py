# def check_adult_age(age):
#     # age=int(input("Enter your age:"))
#     if age >=18:
#         print("Adult")
#     else:
#         print("Child")
# check_age=int(input("Enter your age:"))
# check_adult_age(check_age)

# def highest_no(num1,num2):
#     highest=0
#     if num1<num2:
#         highest=num2
#     else:
#         highest=num1
#     return highest
# high_no=0
# n1=int(input("Enter Num1:"))
# n2=int(input("Enter Num2:"))
# high_no=highest_no(n1,n2)
# # print("Highest no is=",high_no)

# def calc_salary(hrs,rate):
#     salary=0
#     salary=hrs*rate
#     return salary
# working_hrs=int(input("Enter no of hrs working="))
# rate=int(input("Enter rate per hour="))
# total_salary=0
# total_salary=calc_salary(working_hrs,rate)
# print(f"your salary for {working_hrs} hrs at {rate} per hour is {total_salary}")

def format_name():
    """Take first and last name and format in title case."""
    fname=input("Enter First name:")
    lname=input("Enter Last name:")
    return fname.title(),lname.title()
output=format_name()
print(output)