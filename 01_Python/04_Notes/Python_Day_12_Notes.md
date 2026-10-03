# 🐍 Python Day 12 — Scope, Practice & Number Guessing Game

## 1. Scope in Python

**Scope** means where a variable can be accessed.

### Local Scope

A variable created inside a function is available only inside that function.

```python
def my_function():
    number = 10
    print(number)

my_function()
```

`number` is a **local variable**.

### Global Scope

A variable created outside a function can be accessed throughout the program.

```python
number = 10

def my_function():
    print(number)

my_function()
```

`number` is a **global variable**.

### Local vs Global

```python
number = 10

def test():
    number = 5
    print(number)

test()
print(number)
```

Output:

```text
5
10
```

The local variable does not change the global variable.

---

## 2. Global Keyword

`global` allows a function to modify a global variable.

```python
score = 0

def increase_score():
    global score
    score += 1
```

Avoid using `global` unnecessarily. Passing values into functions and using `return` is usually cleaner.

---

# 🧩 3. Practice Problems

### Practice 1 — Even or Odd

Create a function:

```python
def check_even_odd(number):
    # your code
```

Return `"Even"` if the number is even, otherwise `"Odd"`.

---

### Practice 2 — Maximum of Two Numbers

Create:

```python
def find_max(a, b):
    # your code
```

Return the larger number.

---

### Practice 3 — Countdown

Create a function that prints numbers from the given number down to 1.

Example:

```text
countdown(5)

5
4
3
2
1
```

---

# 🔢 4. Prime Number Checker

A **prime number** is a number greater than 1 that has only **two factors: 1 and itself**.

Examples:

```text
2, 3, 5, 7, 11, 13 → Prime
4, 6, 8, 9, 10 → Not Prime
```

### Function

```python
def prime_checker(number):
    is_prime = True

    if number < 2:
        is_prime = False

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
```

### Important Logic

```python
number % i == 0
```

means the number is **completely divisible** by `i`.

If it is divisible by any number other than 1 and itself → **not prime**.

---

# 🎯 5. Number Guessing Game

The computer chooses a random number between 1 and 100.

```python
import random

answer = random.randint(1, 100)
```

The player keeps guessing until:

* The correct number is guessed
* Attempts run out

### Game Flow

```text
Choose difficulty
      ↓
Generate random number
      ↓
Set attempts
      ↓
Make a guess
      ↓
Too high / Too low / Correct
      ↓
Reduce attempts
      ↓
Repeat
```

### Checking the Guess

```python
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("You got it!")
```

### Attempts

```python
while attempts > 0:
    print(f"You have {attempts} attempts remaining.")

    guess = int(input("Make a guess: "))

    if guess == answer:
        print("You got it!")
        break

    attempts -= 1
```

---

# ⭐ Day 12 — Points to Remember

1. **Scope** = where a variable can be accessed.
2. **Local variable** → created inside a function.
3. **Global variable** → created outside a function.
4. Local and global variables can have the same name.
5. `global` allows a function to modify a global variable.
6. `return` is usually cleaner than changing global variables.
7. `random.randint(1, 100)` → random integer from 1 to 100.
8. `while` → repeats while a condition is `True`.
9. `attempts -= 1` → decreases attempts by 1.
10. `break` → exits the loop immediately.
11. **Prime number** → greater than 1 and divisible only by 1 and itself.
12. `%` checks the remainder.
13. `number % i == 0` → number is completely divisible by `i`.
14. Day 12 combines **scope + functions + loops + conditions + randomisation + user input**.

## 🧠 Main Lesson

```text
Variables → Scope
Functions → Local variables + parameters + return
Loops → Repetition
Conditions → Decision making
Random → Random numbers
```

Together, these concepts allow you to build complete programs like the **Number Guessing Game**.