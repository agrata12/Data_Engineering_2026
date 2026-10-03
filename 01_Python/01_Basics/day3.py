print("Welcome to Roller Coaster")
height=float(input("Enter your height in cm="))
bill = 0
if height >=150:
    age=int(input("Enter your age="))
    if age <= 12:
        bill +=10
        print("You can Ride. Child Ticket $10")
    elif age >13 and age<=18:
         bill+= 15
         print("You can Ride. Youth Ticket $15")
    elif age >=45 and age <=55:
        bill +=0
        print("You can Ride. Lucky Free Ticket")
    else: 
        bill+=20
        print("You can ride. Adult Ticket $20")
    wants_photo=input("Do you want a picture? Type y for Yes and n for No=")
    if wants_photo == "y" or wants_photo=="Y":
        bill+=3 
        print("Your photo cost $3.")
    elif wants_photo == "n" or wants_photo=="N":
        print("No Photo")
    print(f"Total Bill= ${bill}")
else:
    print("Better Luck Next Time.")

# # Odd Even 
# n=float(input("Enter number="))
# if n% 2 == 0:

#     print("Even")
# else:
#     print("Odd")

# BMI Calculator
# height=float(input("enter height in m="))
# weight=float(input("Enter Weight in Kg="))
# bmi=round(weight/(height**2),2)
# if bmi < 18.5:
#     print(f"Your BMI = {bmi}. You are underweight")
# elif bmi < 25:
#     print(f"Your BMI = {bmi}. You are normal weight")
# elif bmi >=25:
#     print(f"Your BMI = {bmi}. You are overweight")
