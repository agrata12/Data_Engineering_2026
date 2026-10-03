print("Welcome to Pizza Deliveries!!!")
pizza_size=input("What pizza size do you want? Small S, Medium M or Large L=")
bill=0
if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
elif pizza_size == "L":
    bill = 25
else:
    print("Wrong input. Select S , M or L. ")
    exit()
pepperoni= input("Do you want pepproni? Y or N=")
extra_cheese = input("Do you want extra cheese? Y or N=")
if pepperoni == "Y":
    if pizza_size == "S":
        bill+=5
    else:
        bill+=10
if extra_cheese == "Y":
    bill +=5
print(f"Your Total Bill = Rs {bill}")