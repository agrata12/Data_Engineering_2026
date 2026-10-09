# Day 14 — Higher or Lower Game Project

## 1. Project Overview

**Higher or Lower** is a guessing game where the player compares two randomly selected accounts/items.

The player must guess which one has a **higher value**.

For this project, the value is **number of followers**.

Example:

```text
Compare A: Instagram
vs
Against B: YouTube

Who has more followers?

Type 'A' or 'B':
```

If the player guesses correctly, they continue playing.

If they guess incorrectly, the game ends.

---

# 2. Concepts Used

This project combines several Python concepts learned so far:

* Functions
* Parameters
* Return values
* Dictionaries
* Lists
* Randomization
* `if / elif / else`
* `while` loops
* User input
* Boolean values
* Variables
* Comparison operators
* Importing modules
* Code organization

---

# 3. Project Structure

The project can be divided into:

```text
Game
│
├── Display first account
│
├── Display second account
│
├── Ask user for A or B
│
├── Compare their values
│
├── Check user's answer
│
├── Increase score
│
└── Continue or end game
```

---

# 4. Data Structure

Each account can be stored as a dictionary.

Example:

```python
{
    "name": "Instagram",
    "follower_count": 700,
    "description": "Social media platform",
    "country": "Worldwide"
}
```

The dictionary stores information about one account.

For example:

```python
account["name"]
```

returns:

```text
Instagram
```

And:

```python
account["follower_count"]
```

returns:

```text
700
```

---

# 5. Comparing Two Values

Suppose:

```python
A = 500
B = 800
```

We can compare them:

```python
if A > B:
    print("A is higher")
else:
    print("B is higher")
```

The game uses this idea to determine the correct answer.

---

# 6. Finding the Correct Answer

The program needs to determine which account has more followers.

Example:

```python
if account_a["follower_count"] > account_b["follower_count"]:
    correct_answer = "a"
else:
    correct_answer = "b"
```

Now the program knows the correct answer.

---

# 7. Checking the Player's Answer

The player enters:

```python
guess = input("Who has more followers? Type 'A' or 'B': ").lower()
```

Then:

```python
if guess == correct_answer:
    print("You're right!")
else:
    print("Sorry, that's wrong.")
```

`.lower()` converts the input to lowercase.

So:

```text
A → a
B → b
```

This makes it easier to compare the answer.

---

# 8. Keeping Score

Create a score variable:

```python
score = 0
```

When the player answers correctly:

```python
score += 1
```

This is the same as:

```python
score = score + 1
```

The score increases after every correct answer.

---

# 9. Using a While Loop

The game should continue while the player is correct.

Example:

```python
game_should_continue = True

while game_should_continue:
    # play one round

    if correct:
        score += 1
    else:
        game_should_continue = False
```

This allows the game to continue for multiple rounds.

---

# 10. Random Selection

We don't want the same accounts every time.

Python's `random` module can help:

```python
import random
```

For example:

```python
random.choice(data)
```

selects one random item from a list.

---

# 11. Important Game Logic

The game needs two accounts:

```text
Account A
Account B
```

After the player gets the answer correct:

```text
Account B becomes Account A
```

Then a new Account B is selected.

Conceptually:

```text
Round 1

A → Instagram
B → YouTube

Player chooses B ✅

Round 2

A → YouTube
B → Facebook

Player chooses A ✅

Round 3

A → Facebook
B → TikTok
```

This makes the game continue naturally.

---

# 12. Functions

The project becomes easier to understand when we divide it into functions.

For example:

```python
def format_data(account):
    # display account information
```

and:

```python
def check_answer(guess, follower_a, follower_b):
    # determine whether the guess is correct
```

A function should ideally have **one clear responsibility**.

---

# 13. Example Function — Check Answer

```python
def check_answer(guess, follower_a, follower_b):

    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"
```

The function returns:

```text
True
```

if the player is correct and:

```text
False
```

if the player is wrong.

---

# 14. Game Flow

The complete game follows this logic:

```text
Start
  ↓
Choose two accounts
  ↓
Display A and B
  ↓
Ask player for A/B
  ↓
Compare follower counts
  ↓
Correct?
 ┌───────┴───────┐
Yes              No
 ↓                ↓
Increase score   Game Over
 ↓
B becomes A
 ↓
Choose new B
 ↓
Play again
```

---

# 15. Important Programming Lessons

### `.lower()`

```python
answer = input("A or B? ").lower()
```

Makes input easier to compare.

---

### `+=`

```python
score += 1
```

means:

```python
score = score + 1
```

---

### Dictionary access

```python
account["name"]
account["follower_count"]
```

gets values from a dictionary.

---

### `random.choice()`

```python
random.choice(data)
```

selects a random item from a list.

---

### Boolean values

```python
True
False
```

are useful for controlling the game loop.

Example:

```python
game_should_continue = True
```

---

# 16. Debugging Practice

While building the project, deliberately check for common problems.

### Problem 1

What happens if the player enters:

```text
A
```

instead of:

```text
a
```

Solution:

```python
.lower()
```

---

### Problem 2

What happens if both accounts are the same?

You may need to make sure:

```python
account_a != account_b
```

---

### Problem 3

What happens if the game never ends?

Check the condition controlling:

```python
while
```

---

### Problem 4

What happens if the score doesn't increase?

Check:

```python
score += 1
```

---

# 17. Project Challenge

After completing the basic version, try adding:

### Challenge 1

Display the current score:

```text
You're right!
Current score: 3
```

### Challenge 2

Prevent duplicate accounts.

### Challenge 3

Add more accounts to the data.

### Challenge 4

Create a separate function for checking the answer.

### Challenge 5

Create a separate function for displaying an account.

---

# Key Takeaways

The **Higher or Lower game** is important because it combines many concepts you've already learned.

```text
Functions
   +
Dictionaries
   +
Lists
   +
Randomization
   +
Conditionals
   +
Loops
   +
User Input
   +
Boolean Logic
   ↓
Complete Python Project
```

The goal isn't just to make the game work.

The goal is to understand **how several small Python concepts work together to create a complete program**.

## Day 14 Practice Goal

Build the game yourself first.

Don't copy the complete solution immediately.

Try to create:

1. The data
2. Two random accounts
3. The comparison
4. User input
5. Answer checking
6. Score
7. Game loop
8. Game-over condition

Then use debugging skills from **Day 13** whenever something doesn't work.
