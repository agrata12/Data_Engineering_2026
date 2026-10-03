# import random
# letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
#     "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
#     "u", "v", "w", "x", "y", "z",
#     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
#     "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
#     "U", "V", "W", "X", "Y", "Z"]
# numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# symbols=["!", "#", "$", "%", "&", "*", "@", "?", "+", "="]
# print("Welcome to the Password Generator!")
# count_letter=int(input("How many Letters in your password? "))
# count_symbol=int(input("How many symbols in your password? "))
# count_number=int(input("How many numbers in your password? "))

# # password=""
# # for char in range(0,count_letter):
# #     password+=random.choice(letters)
# # for char in range(0,count_number):
# #     password+=random.choice(numbers)
# # for char in range(0,count_symbol):
# #     password+=random.choice(symbols)

# # print(password)

# password_list=[]
# for char in range(0,count_letter):
#     password_list.append(random.choice(letters))
# for char in range(0,count_number):
#     password_list.append(random.choice(numbers))
# for char in range(0,count_symbol):
#     password_list.append(random.choice(symbols))

# print(password_list)
# random.shuffle(password_list)
# print(password_list)
# password=""
# for char in password_list: #convert list back to string
#     password+=char
# print(password)


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