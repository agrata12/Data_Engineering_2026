# #loops
# fruits=["Apple", "Banana", "Mango"]
# for fruit in fruits:
#     print(fruit + " pie")
# print(fruits)

# for number in range(10,0,-1):
#     print(number)

# total=0
# for number in range(1,101):
#     total+=number
# print(total)

# shopping_list = ["Milk", "Bread", "Apples", "Rice", "Paneer"]
# for item in shopping_list:
#     print(item)

number=int(input("Enter a number="))
result=0
for n in range(1,11):
    result=number*n
    print(f"{number}*{n}={result}")