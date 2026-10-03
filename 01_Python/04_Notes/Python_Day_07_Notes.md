# 🐍 Python Day 7 — Hangman Project

**Date:** 24 September 2026
**Topic:** Hangman Game
**Course:** 100 Days of Python

---

## 🎯 What I Learned Today

Today I built a **Hangman game** using concepts learned in previous days.

This project combines:

* Variables
* Lists
* Strings
* `random`
* `for` loops
* `if / elif / else`
* `while` loops
* Functions
* `return`
* String indexing
* Membership operators
* Boolean values
* Code blocks
* User input

---

# 🎮 What is Hangman?

Hangman is a word-guessing game.

The computer chooses a secret word.

The player guesses letters one at a time.

For every correct guess, the letter is revealed.

For every incorrect guess, the player loses one life.

The player wins when all letters have been guessed.

The player loses when all lives are used.

- Flowcharts are useful in creating the complex games. 

---

# 1. Choosing a Random Word

First, create a list of possible words.

```python
import random

word_list = ["apple", "banana", "computer", "python", "school"]

chosen_word = random.choice(word_list)

print(chosen_word)
```

### Important

```python
random.choice(word_list)
```

randomly selects **one item** from the list.

For example:

```text
python
```

---

# 2. Finding the Length of a Word

We can use `len()` to find how many letters are in the word.

```python
word_length = len(chosen_word)

print(word_length)
```

If:

```python
chosen_word = "python"
```

then:

```python
len(chosen_word)
```

gives:

```text
6
```

---

# 3. Creating the Display

At the beginning, the player shouldn't see the secret word.

Instead, we show blanks.

For example:

```text
_ _ _ _ _ _
```

If the word is:

```text
python
```

we need 6 blanks.

We can create this using a loop.

```python
display = []

for _ in range(word_length):
    display.append("_")

print(display)
```

Output:

```text
['_', '_', '_', '_', '_', '_']
```

---

# 4. Why Use `_` in the Loop?

You may see:

```python
for _ in range(word_length):
```

The `_` is a variable name that means:

> "I don't need to use this value."

We only need the loop to repeat a certain number of times.

For example:

```python
for _ in range(6):
    print("Hello")
```

prints `Hello` six times.

---

# 5. Getting a Guess From the User

```python
guess = input("Guess a letter: ").lower()
```

### `.lower()`

Converts the user's input to lowercase.

For example:

```text
A → a
P → p
Z → z
```

This makes comparisons easier if our word list contains lowercase words.

---

# 6. Checking Every Letter

We need to check whether the guessed letter appears in the secret word.

Example:

```python
chosen_word = "apple"
guess = "p"
```

We can loop through the word:

```python
for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter
```

### What is happening?

Suppose:

```text
chosen_word = "apple"
```

The positions are:

```text
 a  p  p  l  e
 0  1  2  3  4
```

If the user guesses:

```text
p
```

Python checks:

```text
position 0 → a → not p
position 1 → p → yes
position 2 → p → yes
position 3 → l → not p
position 4 → e → not p
```

The display becomes:

```text
_ p p _ _
```

---

# 7. Strings Can Be Indexed

Strings work similarly to lists when using indexes.

```python
word = "python"

print(word[0])
print(word[1])
print(word[2])
```

Output:

```text
p
y
t
```

Indexing starts from `0`.

```text
p  y  t  h  o  n
0  1  2  3  4  5
```

---

# 8. Lists Can Be Changed

This is important for the Hangman display.

We can change an item in a list:

```python
display = ["_", "_", "_", "_"]

display[1] = "a"

print(display)
```

Output:

```text
['_', 'a', '_', '_']
```

This is why using a **list** for `display` is useful.

---

# 9. Checking Whether a Letter Has Already Been Guessed

We can use:

```python
if guess in guessed_letters:
```

The `in` operator checks whether something exists inside a collection.

Example:

```python
guessed_letters = ["a", "e", "i"]

if "a" in guessed_letters:
    print("Already guessed")
```

Output:

```text
Already guessed
```

---

# 10. The `in` Operator

Examples:

```python
"a" in "apple"
```

Result:

```text
True
```

```python
"z" in "apple"
```

Result:

```text
False
```

It can also be used with lists:

```python
"apple" in ["apple", "banana"]
```

Result:

```text
True
```

---

# 11. Keeping the Game Running

Hangman needs to continue until the player wins or loses.

A `while` loop is useful.

Example:

```python
game_over = False

while not game_over:
    # game continues here
```

The loop keeps running while:

```python
game_over == False
```

---

# 12. Lives

We can give the player a number of lives.

```python
lives = 6
```

When the player makes an incorrect guess:

```python
lives -= 1
```

This is shorthand for:

```python
lives = lives - 1
```

Example:

```text
6 → 5 → 4 → 3 → 2 → 1 → 0
```

---

# 13. Checking for an Incorrect Guess

```python
if guess not in chosen_word:
    lives -= 1
```

`not in` means:

> The item does NOT exist in the collection.

Example:

```python
if "z" not in "python":
    print("Wrong guess")
```

---

# 14. Checking if the Player Won

We can check whether there are any blanks left.

```python
if "_" not in display:
    print("You win!")
```

If:

```text
display = ["p", "y", "t", "h", "o", "n"]
```

there is no `_`.

Therefore:

```python
"_" not in display
```

is:

```text
True
```

---

# 15. Checking if the Player Lost

```python
if lives == 0:
    print("You lose!")
```

The game ends when the player has no lives remaining.

---

# 🧩 Main Hangman Logic

The basic structure is:

```python
while game is not over:

    ask the user for a letter

    check the guessed letter

    reveal correct letters

    reduce lives for incorrect guesses

    check whether the player won

    check whether the player lost
```

---

# 🧠 Important New Concepts

## `in`

Checks whether something exists.

```python
if guess in chosen_word:
```

---

## `not in`

Checks whether something does NOT exist.

```python
if guess not in chosen_word:
```

---

## `-=`

Subtracts from a variable.

```python
lives -= 1
```

Same as:

```python
lives = lives - 1
```

---

## String indexing

```python
chosen_word[position]
```

Gets one character from a string.

---

## List item replacement

```python
display[position] = letter
```

Replaces an item in a list.

---

# 🏗️ Basic Hangman Version

```python
import random

word_list = ["apple", "banana", "python", "computer", "school"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []

for _ in range(word_length):
    display.append("_")

lives = 6
game_over = False

while not game_over:

    print(" ".join(display))

    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess!")
        print(f"You have {lives} lives left.")

    if "_" not in display:
        print("You win!")
        game_over = True

    if lives == 0:
        print("You lose!")
        print(f"The word was {chosen_word}.")
        game_over = True
```

---

# 🔍 Understanding the Main Loop

This:

```python
while not game_over:
```

means:

> Keep playing while the game is NOT over.

Inside the loop:

```python
guess = input("Guess a letter: ").lower()
```

gets the player's guess.

Then:

```python
for position in range(word_length):
```

checks every position in the word.

Then:

```python
if letter == guess:
```

checks whether the current letter matches the guess.

If it matches:

```python
display[position] = letter
```

reveals the letter.

---

# 🧪 Example Game

Secret word:

```text
python
```

Initially:

```text
_ _ _ _ _ _
```

User guesses:

```text
p
```

Display:

```text
p _ _ _ _ _
```

User guesses:

```text
o
```

Display:

```text
p _ _ _ o _
```

User guesses:

```text
z
```

Wrong guess.

Lives:

```text
5
```

Eventually:

```text
p y t h o n
```

No blanks remain.

```text
You win!
```

---

# ⚠️ Common Mistakes

### Mistake 1: Using square brackets with `random.choice`

❌ Wrong:

```python
random.choice[word_list]
```

✅ Correct:

```python
random.choice(word_list)
```

Remember:

* `()` → call a function
* `[]` → index/access an item

---

### Mistake 2: Forgetting that indexing starts at 0

For:

```python
word = "python"
```

The indexes are:

```text
p  y  t  h  o  n
0  1  2  3  4  5
```

---

### Mistake 3: Forgetting to decrease lives

```python
if guess not in chosen_word:
    lives -= 1
```

---

### Mistake 4: Checking only one letter

We need to check the **whole word**:

```python
for position in range(word_length):
```

---

### Mistake 5: Using `print()` instead of changing `display`

This:

```python
print(letter)
```

only displays the letter temporarily.

This:

```python
display[position] = letter
```

actually updates the game state.

---

# 🔄 Day 7 Concepts Connected to Previous Days

| Concept         | Previous Day | Used in Hangman         |
| --------------- | ------------ | ----------------------- |
| Variables       | Day 1        | `lives`, `guess`        |
| Strings         | Day 2        | `chosen_word`           |
| Lists           | Day 4        | `display`               |
| Random          | Day 4        | `random.choice()`       |
| `for` loop      | Day 5        | Checking letters        |
| Functions       | Day 6        | Can organize game logic |
| `return`        | Day 6        | Can return results      |
| `while` loop    | Day 6        | Keep game running       |
| `if/else`       | Day 3        | Win/lose decisions      |
| `in` / `not in` | Day 7        | Check letters           |

---

# 📝 Practice

## Practice 1

Create a list:

```python
fruits = ["apple", "banana", "orange"]
```

Randomly select one fruit.

---

## Practice 2

Print every letter of:

```python
word = "python"
```

using a `for` loop.

---

## Practice 3

Create a display containing 5 underscores:

```text
_ _ _ _ _
```

---

## Practice 4

Ask the user for a letter and check whether it exists in:

```python
word = "python"
```

---

## Practice 5

Create a lives system:

```python
lives = 3
```

Reduce lives whenever the user guesses incorrectly.

---

# 💡 My Key Learning Today

### `random.choice()`

Chooses a random item:

```python
random.choice(word_list)
```

### `in`

Checks whether something exists:

```python
guess in chosen_word
```

### `not in`

Checks whether something does not exist:

```python
guess not in chosen_word
```

### `while`

Repeats code while a condition is true:

```python
while not game_over:
```

### `-=`

Decreases a value:

```python
lives -= 1
```

### List replacement

```python
display[position] = letter
```

### String indexing

```python
chosen_word[position]
```

---

# ⭐ Day 7 Summary

Today I built a **Hangman game**.

The biggest new ideas were:

1. Using `random.choice()` to select a random word.
2. Using a list to store the hidden word display.
3. Using indexes to check each letter.
4. Using `in` and `not in`.
5. Using a `while` loop to keep the game running.
6. Using `lives -= 1`.
7. Updating a list using an index.
8. Combining many Python concepts into one project.

---

# 🤔 Reflection

**What did I understand well?**

*

**What confused me?**

*

**What error did I get?**

*

**How did I fix it?**

*

**What new concept did I learn?**

*

**Self-score:** ___ / 10

---

# 🚀 Mini Challenge

Try to improve the Hangman game by adding:

* Already-guessed letter detection
* A list of guessed letters
* Different stages of the hangman drawing
* A larger word list
* A message showing remaining lives
* A replay option

**Goal:** Don't just copy the code. Try to understand what each line is doing.