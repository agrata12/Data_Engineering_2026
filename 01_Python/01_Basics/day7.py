#hangman
import random
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
stages=["""
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,

    # Stage 1 - head
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,

    # Stage 2 - head + body
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    # Stage 3 - one arm
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    # Stage 4 - two arms
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    # Stage 5 - one leg
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    # Stage 6 - two legs / game over
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""]

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
    guess = input("Guess a letter:").lower()
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
        lives-=1
        if lives == 0:
            game_over=True
            print("You lose.")
    if "_" not in display:
        game_over=True
        print("You win.")
    print(stages[6-lives])


# display_word=[]
# for _ in range(len_chosen_word):
#     display_word.append("_")
# display=""
# for char in display_word:
#     display+=char
# print("Word to Guess:",display)

# guess = input("Guess a letter:").lower()
# print(guess)