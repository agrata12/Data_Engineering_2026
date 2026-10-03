# print("Hello")
# # print(len("Hello"))
# num_char=len("Hello")
# print(num_char)

# def my_function(name):
#     print("Hello",name)
# my_function("Agrata")

# def add(a,b):
#     result=a+b
#     return result
# sum=0
# sum=add(10,21)
# print(sum)

# number=1
# while number <=5:
#     print(number)
#     number+=1

# password=""
# while password!="ABC":
#     password=input("Password=")
#     # print("Input correct password",password)
# print("Access Granted")

# def greet():
#     print("Hello, Welcome to Python!")
# greet()
# greet()
# greet()

# def your_name():
#     name=input("Enter your name=")
#     print("Hello",name)
# your_name()

# square=0
# def square():
#     number=int(input("Enter number="))
#     square=number**2
#     return square
# result=square()
# print(result)

# max_no=10
# while max_no >=0:
#     print(max_no)
#     max_no -=1

# number=20
# while number >=2:
#     if number %2==0:
#         print(number)
#     number-=1

# password=""
# while password!="ABC":
#     password=input("Input correct password=")
# # print("Access")
# secret_number=0
# while secret_number!=7:
#     secret_number=int(input("Try Again.\nEnter Secret Number:"))
# print("Yes. You Got It!")

import random
letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"]
numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols=["!", "#", "$", "%", "&", "*", "@", "?", "+", "="]
print("Welcome to the Password Generator!")
count_letter=int(input("How many Letters in your password? "))
count_symbol=int(input("How many symbols in your password? "))
count_number=int(input("How many numbers in your password? "))

def generate_password():
    password_list=[]
    for char in range(0,count_letter):
        password_list.append(random.choice(letters))
    for char in range(0,count_symbol):
        password_list.append(random.choice(symbols))
    for char in range(0,count_number):
        password_list.append(random.choice(numbers))
    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    password=""
    for char in password_list:
        password+=char
    return password

my_password=generate_password()
print(my_password)