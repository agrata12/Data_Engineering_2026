# Day 13 — Debugging & Finding/Fixing Errors

## 1. What is Debugging?

**Debugging** means finding and fixing errors (bugs) in a program.

A **bug** is a mistake in the code that causes:

* an error
* incorrect output
* unexpected behavior

### Basic debugging process

```text
Write code
   ↓
Run code
   ↓
Find the problem
   ↓
Understand the error
   ↓
Fix the code
   ↓
Run again
```

---

## 2. Types of Errors

### A. Syntax Error

A **syntax error** happens when Python cannot understand the structure of the code.

Example:

```python
print("Hello"
```

The closing `)` is missing.

```text
SyntaxError
```

### B. Runtime Error

The code is syntactically correct, but an error occurs while the program is running.

Example:

```python
number = 10 / 0
```

```text
ZeroDivisionError
```

Another example:

```python
number = int("hello")
```

```text
ValueError
```

### C. Logic Error

The program runs without an error, but produces the **wrong result**.

Example:

```python
age = 20

if age > 18:
    print("Child")
else:
    print("Adult")
```

The program runs, but the logic is wrong.

Correct version:

```python
if age > 18:
    print("Adult")
else:
    print("Child")
```

---

## 3. Read the Error Message

When Python gives an error, don't immediately change the code.

First read the error message.

Look for:

1. **File name**
2. **Line number**
3. **Error type**
4. **Error message**

---

## 4. Traceback

A **traceback** is Python's report showing where an error occurred.

It helps us trace the problem back to the code that caused it.

---

## 5. Using Print Statements for Debugging

One simple debugging technique is using `print()` to check variable values.

```python
age = 20
score = age * 2

print(age)
print(score)
```

You can also write:

```python
print("age =", age)
print("score =", score)
```

---

# 6. Beginner Debugging Practice Exercises

**Rule:** Try to find and fix the error yourself before looking at the answer.

---

## Exercise 1 — Syntax Error

Find and fix the error:

```python
name = "Agrata"
print(name
```

**Hint:** Check the brackets.

---

## Exercise 2 — NameError

Find and fix the error:

```python
name = "Agrata"

print(nam)
```

**Hint:** Compare the variable names.

---

## Exercise 3 — TypeError

Find and fix the error:

```python
age = 25

print("I am " + age + " years old")
```

**Hint:** Can you join a string and an integer directly?

---

## Exercise 4 — ZeroDivisionError

Find and fix the error:

```python
number = 10
result = number / 0

print(result)
```

**Hint:** What happens when you divide by zero?

---

## Exercise 5 — ValueError

Find and fix the problem:

```python
age = int(input("Enter your age: "))

print(age)
```

Try entering:

```text
twenty
```

**Question:** Why does this cause an error?

**Hint:** What type of value does `int()` expect?

---

## Exercise 6 — IndexError

Find and fix the error:

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[3])
```

**Hint:** Remember that Python list indexes start at `0`.

---

## Exercise 7 — Logic Error

The program runs, but gives the wrong result.

Find and fix the logic:

```python
number = 10

if number % 2 == 1:
    print("Even")
else:
    print("Odd")
```

**Expected output:**

```text
Even
```

---

## Exercise 8 — Debug the Function

Find the error:

```python
def add_numbers(a, b):
    result = a + b
    print(result)

answer = add_numbers(5, 10)

print(answer)
```

The output is:

```text
15
None
```

**Question:** Why is `None` printed?

**Hint:** Think about `return`.

---

## Exercise 9 — Debug the Loop

Find the error:

```python
for i in range(1, 6):
print(i)
```

**Hint:** Check indentation.

Expected output:

```text
1
2
3
4
5
```

---

## Exercise 10 — Debug the Prime Checker

Find the error in this code:

```python
def prime_check(num):

    is_prime = True

    for i in range(num):
        if num % i == 0:
            is_prime = False

    if is_prime:
        print("Prime")
    else:
        print("Not prime")

prime_check(11)
```

**Hints:**

1. Look carefully at `range()`.
2. What is the first value generated?
3. Can you use `%` with that value?

---

# 7. Debugging Challenge

Try to find **all the problems** in this program:

```python
def calculate_average(numbers):
    total = 0

    for number in numbers:
        total = total + numbers

    average = total / len(number)

    return average


scores = [80, 90, 70]

print(calculate_average(scores))
```


Correct Version: 

def calculate_average(numbers):
    total = 0

    for number in numbers:
        total = total + number

    average = total / len(numbers)

    return average


scores = [80, 90, 70]

print(calculate_average(scores))

### Questions

1. What type of error occurs?
2. Which line causes it?
3. Are there any other problems?
4. Can you fix the entire program?

Expected output:

```text
80.0
```

---

# 8. Debugging Checklist

When your code doesn't work:

```text
1. Read the error
       ↓
2. Find the line number
       ↓
3. Identify the error type
       ↓
4. Check the variables
       ↓
5. Check the logic
       ↓
6. Fix one thing
       ↓
7. Run again
```

### Remember

**Don't ask only:**

> "How do I remove this error?"

Ask:

> **"Why did Python give me this error?"**

That is how you become better at debugging.
