# def even_odd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# n=int(input("Enter number to check even or odd: "))
# print(even_odd(n))

# def find_max(num1,num2):
#     return max(num1,num2)
# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# print(f"Max number is: {find_max(n1,n2)}")

# def countdown(num):
#     for i in range(num,0,-1):
#         print (i)
# n=int(input("Enter countdown number: "))
# # countdown(n)

# def countdown(n): #countdown using recurssion
#     if n == 0:
#         return
#     print(n)
#     countdown(n - 1)

# countdown(10)


def prime_check(num):
    is_prime=True
    if num < 2:
        is_prime=False

    for i in range (2,num):
        if num % i ==0:
            is_prime=False
            break
        else:
            is_prime=True
        # return is_prime
    if is_prime == True:
        print("Prime")
    else:
        print("Not prime")
n=int(input("Enter number to check prime:"))
prime_check(n)