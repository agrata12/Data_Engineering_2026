# Black Jack Game
import random

logo= '''  ___   ___   ___   ___   ___ 
 |A  | |K  | |Q  | |J  | |10 |
 |(`)| |(`)| |(`)| |(`)| |(`)|
 |_\_| |_\_| |_\_| |_\_| |_\_|
'''
print("Welcome to the Black Jack Table! ")

def deal_card():
    """returns random card from the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """takes a list of cards and returns the score calculated from the cards"""
    # if 11 in cards and 10 in cards and len(cards) == 2: #or we can also write it as:
    if sum(cards) == 21 and len(cards) == 2:
        return 0 #tells that computer got a black jack
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score,c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, user has a Black Jack !!"
    elif u_score == 0:
        return "User has a Black Jack. You WON."
    elif u_score > 21: 
        return "User went over. You lose."
    elif c_score > 21: 
        return "Comp went ovwe. You win."
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose."
def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    is_game_over =False
    user_score = -1
    computer_score=-1

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card) #short form can also be written as : user_cards.append(deal_card())

        new_computercard=deal_card()
        computer_cards.append(new_computercard)

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"{user_cards} and score={user_score}")
        print(f"{computer_cards[0]}")

        if user_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            user_should_deal=input("Type 'y' to deal another card, or n to pass:")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"{user_cards} and score={user_score}")
    print(f"{computer_cards} and {computer_score}")
    print(compare(user_score,computer_score))

keep_playing=input("Do you want to play the game of Black Jack? Type y or n.: ")
while keep_playing == "y":
    print("\n"*20)
    play_game()
    keep_playing=input("Do you want to play the game of Black Jack? Type y or n.: ")