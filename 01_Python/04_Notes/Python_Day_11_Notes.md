# 🐍 Python Day 11 — Blackjack Capstone Project

## 🃏 1. Project Goal

Build a simple **Blackjack game** where:

* Player gets 2 cards.
* Computer gets 2 cards.
* Player can choose to **hit** or **pass**.
* Cards are added to the player's hand.
* Whoever is closest to **21** without going over wins.

---

# 2. Important Blackjack Rules

### Card Values

```text
2–10 → face value
J, Q, K → 10
A → 11 or 1
```

### Winning

* Score > 21 → Bust ❌
* Score = 21 → Blackjack 🃏
* Closest to 21 → Winner
* Both same score → Draw

---

# 3. Main Project Structure

The project can be divided into functions:

```python
def deal_card():
    pass


def calculate_score(cards):
    pass


def compare(user_score, computer_score):
    pass
```

Each function has a specific job.

### `deal_card()`

Returns a random card.

### `calculate_score(cards)`

Calculates the total score of a hand.

### `compare()`

Decides the winner.

---

# 4. Lists and Random Choice

Cards can be stored in a list:

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

Get a random card:

```python
random.choice(cards)
```

Add it to a hand:

```python
user_cards.append(random.choice(cards))
```

---

# 5. Functions with Outputs

`deal_card()` can return a card:

```python
def deal_card():
    return random.choice(cards)
```

Then:

```python
card = deal_card()
```

The function **returns a value** that can be stored in a variable.

---

# 6. Calculating the Score

Example:

```python
def calculate_score(cards):
    return sum(cards)
```

If:

```python
cards = [10, 5]
```

Then:

```text
sum(cards) → 15
```

---

# 7. The Ace Problem

An Ace can be:

```text
11
```

or:

```text
1
```

If the score goes above 21 and the hand contains an Ace:

```python
if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
```

This changes:

```text
[11, 9, 5]
```

from:

```text
25
```

to:

```text
15
```

---

# 8. Blackjack

If the first two cards total 21:

```python
if sum(cards) == 21 and len(cards) == 2:
    return 0
```

In the project, `0` can be used internally to represent **Blackjack**.

---

# 9. While Loop

The player continues drawing cards while they want to play.

```python
while should_continue:
    user_choice = input("Type 'y' to get another card, or 'n' to pass: ")

    if user_choice == "y":
        user_cards.append(deal_card())
```

The loop continues until the player chooses to stop or goes over 21.

---

# 10. Function as Dictionary Value

This connects with the concept from Day 10.

```python
operations = {
    "+": add,
    "-": subtract
}
```

Remember:

```text
add   → function reference
add() → calls the function
```

---

# 11. Main Game Flow

```text
Start Game
    ↓
Deal 2 cards to player
    ↓
Deal 2 cards to computer
    ↓
Calculate scores
    ↓
Player chooses:
    ↓
Hit → deal another card
Pass → computer plays
    ↓
Calculate final scores
    ↓
Compare scores
    ↓
Display result
```

---

# ⭐ Day 11 — Important Points to Remember

### Python Concepts

1. `random.choice()` → selects a random item from a list.
2. `.append()` → adds an item to a list.
3. `sum()` → adds numbers in a list.
4. `len()` → counts items in a list.
5. `while` → repeats code while a condition is true.
6. `return` → sends a value back from a function.
7. Functions can be used to divide a large program into smaller tasks.
8. A function can call another function.
9. Lists can be passed into functions.
10. A dictionary can store functions as values.
11. user_score = -1 and computer_score = -1 → initial placeholder values before scores are calculated. 
    The reason for setting both to -1 outside the while loop is mainly to give them an initial value before the loop starts.

    Why -1 specifically?

    Because a valid Blackjack score can be:

    0 → often used internally for Blackjack in this project
    1 and above → normal scores
    -1 → not a valid game score

    So -1 works as a placeholder meaning: "We haven't calculated the score yet."
12. Rename parameter: Right-click parameter → Refactor → Rename → updates the parameter and its related references in the function.

### Blackjack Concepts

11. Ace can be **11 or 1**.
12. More than 21 = **Bust**.
13. 21 with two cards = **Blackjack**.
14. The goal is to get as close to 21 as possible without going over.
15. The game requires handling different possible situations, not just one fixed path.

---

