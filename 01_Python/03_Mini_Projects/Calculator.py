logo = ''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

(Regular Calculator)'''
# print(logo)
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide,
}
# print(operations["*"](4,8))

def calculator():
    print(logo)
    num1=float(input("Enter First Number: \n"))

    should_continue =True

    while should_continue:

        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick operation: \n")
        num2=float(input("Enter Second Number:\n"))

        result=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type y to continue calculations with {result} or type n to start a new calculation: ")
        if choice == "y":
            num1= result
        else:
            print("\n"*20)
            should_continue=False
            calculator() #recursion

calculator() #calling the main function 




# operation=input("Enter operation: \n+\n-\n*\n/ :\n")
# num2=float(input("Enter Second Number:\n"))
# result = 
# print(f"{num1} {operation} {num2}= {result}")

# def calculations(n1,n2,op):
#     if op == "+":
#         return n1+n2
#     elif op == "-":
#         return n1-n2
#     elif op == "*":
#         return n1*n2
#     elif op == "/":
#         return n1/n2
#     else:
#         print ("Wrong operation input")

# num1=float(input("Enter First Number: \n"))
# operation=input("Enter operation: \n+\n-\n*\n/ :\n")
# num2=float(input("Enter Second Number:\n"))
# result = calculations(num1,num2,operation)
# print(f"{num1} {operation} {num2}= {result}")
# should_continue=input(f"Type y to continue calculations with {result} or type n to start a new calculation")
# output_list=[]
# if should_continue == "y":
#     output_list.append(result)
# else 

    