import random
print("Welcome to Higher-Lower Project!")
data=[{
    "name":"Ronaldo",
    "no_of_followers":200,
},
{
    "name":"Messi",
     "no_of_followers":300,   
},
{
    "name":"Obama",
    "no_of_followers":1000,
},
{
    "name":"Modi",
    "no_of_followers":2000,
}
]
def compare(a,b):
    if a["no_of_followers"] > b["no_of_followers"]:
        return a["name"]
    else:
        return b["name"]

playerA=random.choice(data)
playerB=random.choice(data)
score=0
should_continue=True

while should_continue:
    print(f"{playerA["name"]} \n vs \n{playerB["name"]}\n")
    user_input=input("Who do you think has more followers: ").lower()
    result=compare(playerA,playerB)

    if "user_input" == "result":
        score+=1
        print(f"Correct Answer. Score = {score} ")
        new_player=random.choice(data)
        playerA = playerB
        playerB = new_player
        # compare(playerA,playerB)
    else:
        print(f"Wrong Answer. Final Score= {score}")
        should_continue=False

# print(result)


# new_data=[]
