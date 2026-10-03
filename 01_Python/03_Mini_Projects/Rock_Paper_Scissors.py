import random
print("Welcome to Rock-Paper-Scissors!\nPress 0 for Rock, 1 for Paper and 2 for Scissors=")

rock='''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''
paper=''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''
scissors='''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

           '''
game_images=[rock,paper,scissors]
your_choice=int(input("What is your choice?="))
if your_choice >=0 or your_choice <=2:
    print(game_images[your_choice])
computer_choice=random.randint(0,2)
print(game_images[computer_choice])
if your_choice >=3 and your_choice <0:
    print("Invalid input. You lose")
elif your_choice == 0 and computer_choice == 2:
    print("You win")
elif your_choice >computer_choice:
    print("You win")
elif computer_choice == 0 and your_choice == 2:
    print("You lose.")
elif computer_choice == your_choice:
    print("Draw")
elif computer_choice > your_choice:
    print("Computer win. You lose")

# your_choice = int(input("What is your choice? "))

# if your_choice < 0 or your_choice > 2:
#     print("Invalid input. You lose.")
# else:
#     print(game_images[your_choice])

#     computer_choice = random.randint(0, 2)
#     print(game_images[computer_choice])

#     if your_choice == computer_choice:
#         print("Draw")
#     elif your_choice == 0 and computer_choice == 2:
#         print("You win")
#     elif your_choice == 1 and computer_choice == 0:
#         print("You win")
#     elif your_choice == 2 and computer_choice == 1:
#         print("You win")
#     else:
#         print("You lose")