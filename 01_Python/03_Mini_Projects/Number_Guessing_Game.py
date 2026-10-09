import random
logo='''                      _                   
                      | |                  
 _ __  _   _ _ __ ___ | |__   ___ _ __ ___ 
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__/ __|
| | | | |_| | | | | | | |_) |  __/ |  \__ \
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|  |___/'''
print(logo)
# global attempts 
# def number_game(level):
#     while attempts !=0:
#         if level == "hard":
#             attempts = 5
#             guess = int(input("Guess the number:"))
#             if guess == "num":
#                 print("Correct guess. You won!")
#             else:

#                 attempts-=1
#                 guess = int(input("Guess the number:"))
#         elif level == "easy":
#             attempts = 10
#             guess = int(input("Guess the number:"))
#             if guess == "num":
#                 print("Correct guess. You won!")
#             else:
#                 attempts-=1
#                 guess = int(input("Guess the number:"))

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess,actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else: 
        print(f"Correct Guess. You won! The answer was {actual_answer}")
        exit()

def difficulty_level():
    global turns
    user_level=input("Enter difficulty level, easy or hard: ").lower()
    if user_level == "easy":
        return EASY_LEVEL_TURNS
    elif user_level == "hard":
        return HARD_LEVEL_TURNS


print("Welcome to the Number Guessing Game:\n I am thinking of a number between 1 and 100.")
num=random.randint(1,101)
print("I thought of ",num)
turns= difficulty_level()
while turns!=0:

    print(f"You have {turns} attempts remaining. ")
    guess = int(input("Guess the number:"))
    answer=check_answer(guess,num)
    turns-=1