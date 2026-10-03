# Subscripting 
# print("Hello"[-5])

# # String 
# print("123"+"456")

# # Integers = Whole numbers
# print(123+456)
# print(123_456_789)
# # Float 
# print(123.4)
# # Boolean
# print(True)

# Type Error
# print(len(123)) 
# # Type
# print(type("Hello"))
# print(type(123))
# print(type(123.456))
# print(type(True))

# type cast
# print("123"+"456")
# print(int("123")+int("456"))

# print("No of letters in your name:" +str(len(input("Enter your name:"))))

# price = "4000.50"
# price = print(float(price))

# print(10 + 5)
# print(10 - 6)
# print(10 * 5)
# print(10 // 5)
# print(10 / 3)
# print(10 % 3)
# print(2 ** 3)

# print(3*(3+3)/3-3)

# # BMI Calculator
# height=float(input("enter height in m"))
# weight=float(input("Enter Weight in Kg"))
# bmi=weight/(height**2)
# print("BMI=",round(bmi,2))

# # f-Strings
# score=0
# height = 1.5
# is_winning=True
# print(f"Your Score = {score}, height = {height} and you are winning {is_winning}")

#  Tip Calculator
print("Welcome to the Tip Calculator")
bill= float(input("What was the total bill?"))
tip=float(input("How much tip you would like to give?"))
number_of_people= int(input("How many people to split bill?"))
# if tip == 12:
#     print("Each person should pay=",round(bill*1.12/number_of_people,2))
# elif tip == 15:
#     print("Each person should pay=",round(bill*1.15/number_of_people,2))
# elif tip == 20: 
#     print("Each person should pay=",round(bill*1.2/number_of_people,2))
# else: 
#     print("No tip. Each person should pay=",round(bill/number_of_people,2))
total_bill= bill + (tip / 100 * bill)
share_per_person = round(total_bill/ number_of_people,2)
print("Total Bill = ", round(total_bill,2))
print(f"Each person should pay {share_per_person}")