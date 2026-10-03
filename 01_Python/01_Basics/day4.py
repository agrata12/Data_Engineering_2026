import random
# import my_module
#random_integer = random.randint(1,10)
#print(random_integer)
# random_float=random.random()
# print(random_float)
# random_range=random.random() *10 #gives no from 0 to 10
# print(random_range)
# print(my_module.my_fav_number)
# random_float= random.uniform(1,10)
# print(random_float)

# #Heads and Tails
# result=random.randint(1,2)
# if result == 1:
#     print("Heads!")
# else:
#     print("Tails!")

#Lists
# states_of_US=["texas","Florida","Delware", "New Jersey", "Georgia"]
# # # print(states_of_US[0][-2])
# # states_of_US[1]="florida"
# # print(states_of_US[1])
# states_of_US.append("Delaware")
# print(states_of_US)\
# fruits=["Apple","Orange","Mango"]
# # fruits.append("Banana")
# more_fruits=["Papaya", "Kiwi"]
# # fruits.extend(more_fruits)
# fruits.insert(2,"pear")
# # fruits.remove("mango")
# # fruits.pop(0)
# # fruits.reverse()
# fruits.sort()
# # print(fruits)
# stack = [3,4,5,6]
# # stack.append(7)
# stack.pop()
# print(stack)

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()                 # The first to arrive now leaves
# queue.popleft()                 # The second to arrive now leaves
# print(queue)

#Nested Lists
# dirty_dozen1=["Strawberry","Spinach","Kale","Apple", "Grapes"]
fruits=["Strawberry", "Apple", "Grapes"]
vege=["Spinach", "Kale"]
dirty_dozen2=[fruits,vege]
# print(dirty_dozen1)
print(dirty_dozen2[0][1])