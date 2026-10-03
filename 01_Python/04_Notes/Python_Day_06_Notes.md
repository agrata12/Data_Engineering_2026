# Python Day 6 — Functions, Code Blocks & While Loops

**Date:**  22 Sep 2026

---

# 1. Functions

- A function is a reusable block of code that performs a particular task.
- Instead of writing the same code repeatedly, we can define it once and call it whenever we need it.
- https://docs.python.org/3/builtins/functions.html


Example:

```python
def greet():
    print("Hello!")
```

To run the function:

```python
greet()
```

Output:

```text
Hello!
```

---

# 2. Defining a Function

The basic syntax is:

```python
def function_name():
    # code block
```

Example:

```python
def my_function():
    print("Hello")
    print("Welcome to Python")
```

The function does not run just because we define it.

We need to **call** it:

```python
my_function()
```

---

# 3. Function Call

Calling a function means asking Python to execute the code inside the function.

```python
def greet():
    print("Hello")

greet()
```

Here:

```text
def greet():
```

defines the function.

```text
greet()
```

calls the function.

---

# 4. Code Blocks

A code block is a group of statements that belong together.

Python uses **indentation** to define code blocks.

Example:

```python
def greet():
    print("Hello")
    print("How are you?")
```

Both `print()` statements are inside the function because they are indented.

---

# 5. Indentation

Python normally uses **4 spaces** for indentation.

Correct:

```python
def greet():
    print("Hello")
```

Incorrect:

```python
def greet():
print("Hello")
```

Indentation tells Python which statements belong to the function.

---

# 6. Functions with Parameters

A parameter allows us to give information to a function.

Example:

```python
def greet(name):
    print("Hello", name)
```

Call the function:

```python
greet("Agrata")
```

Output:

```text
Hello Agrata
```

Here:

```text
name
```

is the parameter.

```text
"Agrata"
```

is the argument passed to the function.

---

# 7. Multiple Parameters

A function can have more than one parameter.

```python
def add(a, b):
    print(a + b)
```

Call:

```python
add(5, 3)
```

Output:

```text
8
```

---

# 8. Return Statement

A function can return a value using `return`.

Example:

```python
def add(a, b):
    return a + b
```

We can store the returned value:

```python
result = add(5, 3)

print(result)
```

Output:

```text
8
```

### `print()` vs `return`

`print()` displays something on the screen.

```python
def add(a, b):
    print(a + b)
```

`return` sends the value back to the place where the function was called.

```python
def add(a, b):
    return a + b



    6. print() vs return

This is very important for Day 6.

print()	------------------------------------------ return
Displays something	                            Sends a value back
Mainly for showing output	                    Mainly for using a result
Doesn't give the value to the calling code.	    Gives the value to the calling code
Function can continue after print()	            Function ends when return executes

Example:

def add(a, b):
    print(a + b)

versus:

def add(a, b):
    return a + b

With return, you can do:

answer = add(10, 20)

if answer > 25:
    print("Large result")

That's why return is so useful.
```

---

# 9. Why Use Functions?

Functions help us:

* Reuse code.
* Avoid repeating code.
* Organise programs.
* Make code easier to read.
* Break a large problem into smaller problems.
* Make code easier to test and debug.

---

# 10. While Loop

A `while` loop repeatedly executes a block of code **as long as a condition is true**.

Basic syntax:

```python
while condition:
    # code to repeat
```

Example:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Output:

```text
1
2
3
4
5
```

---

# 11. How a While Loop Works

Consider:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Python does this:

```text
number = 1
↓
Is 1 <= 5? Yes
↓
Print 1
↓
number becomes 2
↓
Is 2 <= 5? Yes
↓
Print 2
↓
...
↓
number becomes 6
↓
Is 6 <= 5? No
↓
Stop
```

---

# 12. Important — Avoid Infinite Loops

A `while` loop needs something that eventually makes its condition become false.

This can create an infinite loop:

```python
number = 1

while number <= 5:
    print(number)
```

`number` never changes, so the condition remains true forever.

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

---

# 13. While Loop with User Input

A `while` loop is useful when we don't know exactly how many times we need to repeat something.

Example:

```python
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")
```

The loop continues until the correct password is entered.

---

# 14. While Loop vs For Loop

### `for` loop

Use a `for` loop when you generally know what you want to iterate through.

Example:

```python
for number in range(1, 6):
    print(number)
```

### `while` loop

Use a `while` loop when repetition depends on a condition.

Example:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

### Simple way to remember

**For loop:**

> Repeat for each item / for a known sequence.

**While loop:**

> Keep repeating while this condition is true.

---

# 15. While Loop and Code Blocks

A `while` loop creates a code block.

```python
while condition:
    statement1
    statement2
```

The indented statements belong to the loop.

Example:

```python
number = 1

while number <= 3:
    print("Number:", number)
    print("Inside loop")
    number += 1

print("Outside loop")
```

---

# 16. Functions Can Contain Loops

A function can contain a `while` or `for` loop.

Example:

```python
def countdown():
    number = 5

    while number > 0:
        print(number)
        number -= 1

countdown()
```

Output:

```text
5
4
3
2
1
```

---

# 17. Loops Can Be Used Inside Functions

Example:

```python
def print_numbers():
    for number in range(1, 6):
        print(number)

print_numbers()
```

The function contains a `for` loop.

---

# 18. Functions Can Call Other Functions

One function can call another function.

```python
def greet():
    print("Hello")

def start_program():
    greet()
    print("Program started")

start_program()
```

Output:

```text
Hello
Program started
```

---

# 19. Local Variables

A variable created inside a function is generally local to that function.

Example:

```python
def my_function():
    name = "Agrata"
    print(name)

my_function()
```

The variable `name` belongs to the function.

Trying to use it outside the function may result in:

```text
NameError
```

---

# 20. Function With Return Value

Example:

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

Output:

```text
25
```

The function takes an input and gives an output.

```text
Input → Function → Output
  5   → square() → 25
```

---

# Practice Problems

## Practice 1 — Simple Function

Create a function called `greet()` that prints:

```text
Hello, welcome to Python!
```

Call the function three times.



def greet():
    print("Hello, Welcome to Python!")
greet()
greet()
greet()

---

## Practice 2 — Name Function

Create a function that accepts a name and prints:

```text
Hello Agrata
```

Example:

```python
def greet(name):
    print("Hello", name)
```


def your_name():
    name=input("Enter your name=")
    print("Hello",name)
your_name()


---

## Practice 3 — Add Two Numbers

Create a function that accepts two numbers and returns their sum.

Example:

```python
def add(a, b):
    return a + b
```


def add(a,b):
    result=a+b
    return result
sum=0
sum=add(10,21)
print(sum)
---

## Practice 4 — Square Number

Create a function that accepts a number and returns its square.

Example:

```python
def square(number):
    return number * number
```


square=0
def square():
    number=int(input("Enter number="))
    square=number**2
    return square
result=square()
print(result)
---

## Practice 5 — Countdown

Use a `while` loop to print:

```text
10
9
8
7
6
5
4
3
2
1
```

max_no=10
while max_no >=0:
    print(max_no)
    max_no -=1

---

## Practice 6 — Even Numbers

Use a `while` loop to print even numbers from 2 to 20.


number=20
while number >=2:
    if number %2==0:
        print(number)
    number-=1

---

## Practice 7 — Password

Create a program that repeatedly asks the user for a password until the correct password is entered.

password=""
while password!="ABC":
    password=input("Input correct password=")
print("Access")

---

## Practice 8 — Number Guessing

Choose a secret number.

Ask the user to guess the number repeatedly until they guess correctly.

Example:

```text
Guess the number: 5
Try again.

Guess the number: 8
Try again.

Guess the number: 7
Correct!
```

secret_number=0
while secret_number!=7:
    secret_number=int(input("Try Again.\nEnter Secret Number:"))
print("Yes. You Got It!")

---

# Mini Project — Password Generator

Extend your Day 5 password generator.

Create a function:

```python
def generate_password():
    # password generation code
```

Inside the function:

1. Select random letters.
2. Select random numbers.
3. Select random symbols.
4. Shuffle the characters.
5. Convert the list into a string.
6. Return the password.

Example structure:

```python
def generate_password():
    password_list = []

    # add random characters

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += char

    return password
```

Then:

```python
password = generate_password()

print(password)
```

import random
letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"]
numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols=["!", "#", "$", "%", "&", "*", "@", "?", "+", "="]
print("Welcome to the Password Generator!")
count_letter=int(input("How many Letters in your password? "))
count_symbol=int(input("How many symbols in your password? "))
count_number=int(input("How many numbers in your password? "))

def generate_password():
    password_list=[]
    for char in range(0,count_letter):
        password_list.append(random.choice(letters))
    for char in range(0,count_symbol):
        password_list.append(random.choice(symbols))
    for char in range(0,count_number):
        password_list.append(random.choice(numbers))
    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    password=""
    for char in password_list:
        password+=char
    return password

my_password=generate_password()
print(my_password)


---

# Key Concepts

| Concept         | Example                            |
| --------------- | ---------------------------------- |
| Define function | `def greet():`                     |
| Call function   | `greet()`                          |
| Parameter       | `def greet(name):`                 |
| Argument        | `greet("Agrata")`                  |
| Return value    | `return result`                    |
| While loop      | `while condition:`                 |
| Infinite loop   | Condition never becomes false      |
| Code block      | Indented statements                |
| Local variable  | Variable created inside a function |
| For loop        | `for item in items:`               |
| Function + loop | Loop inside a function             |

---

# Common Mistakes

## Mistake 1 — Defining but not calling a function

```python
def greet():
    print("Hello")
```

Nothing happens until:

```python
greet()
```

---

## Mistake 2 — Forgetting indentation

Incorrect:

```python
def greet():
print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

---

## Mistake 3 — Infinite while loop

Incorrect:

```python
number = 1

while number <= 5:
    print(number)
```

Correct:

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

---

## Mistake 4 — Confusing print and return

`print()` displays a value.

`return` sends a value back from the function.

Example:

```python
def add(a, b):
    return a + b
```

---

# Day 6 Summary

* A function is a reusable block of code designed to perform a specific task.
* `def` is used to define a function.
* A function runs when it is called.
* Parameters allow functions to receive input.
* Arguments are the actual values passed to parameters.
* `return` sends a value back from a function.
* Python uses indentation to define code blocks.
* A `while` loop repeats code while a condition remains `True`.
* A `while` loop must eventually become `False` to avoid an infinite loop.
* `for` loops are useful for iterating through a sequence or a known range.
* `while` loops are useful when repetition depends on a condition.
* Functions can contain loops.
* Loops can be used inside functions.
* Functions can call other functions.

---

# Day 6 Reflection

## What I learned

*

## What was easy

*

## What was confusing

*

## What mistakes did I make?

*

## What did I practice?

*

## My self-score

**__/10**

## One thing I can explain without looking at my notes

>

---

# Day 6 Mini Project

**Project:** Password Generator using a Function

**Completed:** ☐

**What I found easy:**

>

**What I found difficult:**

>

**What I need to practice again:**

>

Hurdles game: 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
number_hurdles=6
while number_hurdles >0:
    hurdle()
    number_hurdles -=1
    print(number_hurdles)
    
        