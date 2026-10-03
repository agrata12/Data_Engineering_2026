import random
from hangman_art import stages

print("Welcome to the Hangman game!")
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
lives=6
word_list=["apple", "banana", "pear", "mango", "plum"]

chosen_word=random.choice(word_list)
print(chosen_word)
len_chosen_word=len(chosen_word)

placeholder=""
for position in range(0,len_chosen_word):
    placeholder+="_"
print(placeholder)

game_over=False
correct_letters=[]

while not game_over:
    display=""
    print(f"**************Lives Left ={lives}/6**************")
    guess = input("Guess a letter:").lower()
    if guess in correct_letters:
        print("You have already guessed the letter.")
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
   
    if guess not in chosen_word:
        print(f"You guessed {guess}. Not in the chosen word.")
        lives-=1
        if lives == 0:
            game_over=True
            print(f"**************You lose. The word was {chosen_word}.**************")
    if "_" not in display:
        game_over=True
        print("**************You win.**************")
    print(stages[6-lives])