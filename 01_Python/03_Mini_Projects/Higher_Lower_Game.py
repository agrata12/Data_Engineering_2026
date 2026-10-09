import random
print("Welcome to Higher-Lower Project!")
data=[{
    "name":"Ronaldo",
    "no_of_followers":200,
    "country":"Portugal",
},
{
    "name":"Messi",
     "no_of_followers":300, 
     "country":"Argentina",  
},
{
    "name":"Obama",
    "no_of_followers":1000,
    "country":"US",
},
{
    "name":"Modi",
    "no_of_followers":2000,
    "country":"India",
}
]

def format_data(account):
    """Format data into printable format"""

    account_name=account["name"]
    account_country=account["country"]
    return f"{account_name}, from {account_country}."

def check_answer(user_guess,a_foll,b_foll):
    """takes the input and check with user followers and return high followers name"""
    if a_foll > b_foll:
        return user_guess == "a"
    else:
        return user_guess == "b"

score=0
game_continue = True
account_b= random.choice(data)


while game_continue:

    account_a= account_b
    account_b= random.choice(data)
    while account_a == account_b:
        account_b= random.choice(data)

    print(f"Compare A: {format_data(account_a)} \n vs \nAgainst B: {format_data(account_b)}")
    guess = input("Who do you think has more followers: Type A or B: ").lower()
    print("\n"*20)

    a_follower = account_a["no_of_followers"]
    b_follower = account_b["no_of_followers"]
    is_correct = check_answer(guess,a_follower,b_follower)
    if is_correct:
        score+=1
        print(f"Correct Answer. Current Score = {score}")
    else: 
        print(f"Sorry Wrong Answer.Final Score = {score}")
        game_continue = False