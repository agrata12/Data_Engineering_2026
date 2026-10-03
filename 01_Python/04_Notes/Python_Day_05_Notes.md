# Python Day 5 — For Loops, Range & Code Blocks

Date: 20 September 2026

---

# 1. What Is a Loop?

- A loop allows us to repeat a block of code multiple times.
- Things happen over and over again. 

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

we can use a loop:

```python
for i in range(5):
    print("Hello")
```

The loop repeats the code automatically.

---

# 2. For Loop

A `for` loop is used to repeat code for each item in a sequence.
- For loop, goes through each item in the list, perform some action with each item. 
- Loops allows us to execute same line of code again and again. 

Basic syntax:

```python
for item in sequence:
    # code to repeat
```

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Mango
```

The variable `fruit` takes the value of each item one at a time.

### How it works

First:

```text
fruit = "Apple"
```

Then:

```text
fruit = "Banana"
```

Then:

```text
fruit = "Mango"
```

The loop stops after all items have been processed.

---

# 3. For Loop with a String

A string is also a sequence, so we can loop through its characters.

```python
name = "Agrata"

for letter in name:
    print(letter)
```

Output:

```text
A
g
r
a
t
a
```

---

# 4. Range()

`range()` generates a sequence of numbers that can be used with a loop.

Example:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

### Important

`range(5)` starts at `0` and stops **before 5**.

So:

```python
range(5)
```

produces:

```text
0, 1, 2, 3, 4
```

It does not include `5`.

---

# 5. range(start, stop)

We can specify a starting number.

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

The `stop` value is excluded.

Therefore:

```python
range(1, 6)
```

means:

```text
Start at 1
Stop before 6
```

---

# 6. range(start, stop, step)

We can also specify a step.

```python
for number in range(1, 11, 2):
    print(number)
```

Output:

```text
1
3
5
7
9
```

The structure is:

```python
range(start, stop, step)
```

Example:

```python
range(2, 11, 2)
```

produces:

```text
2
4
6
8
10
```

---

# 7. Counting Backwards

A negative step can be used to count backwards.

```python
for number in range(10, 0, -1):
    print(number)
```

Output:

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

Notice that `0` is excluded.

---

# 8. Code Blocks

A code block is a group of statements that belong together.

Python uses **indentation** to define code blocks.

Example:

```python
if age >= 18:
    print("Adult")
    print("You can vote")
```

Both `print()` statements belong to the `if` block.

---

# 9. Indentation in For Loops

The code inside a `for` loop must be indented.

Correct:

```python
for number in range(5):
    print(number)
```

Incorrect:

```python
for number in range(5):
print(number)
```

Python will produce an indentation error.

### Standard indentation

Python normally uses **4 spaces** for indentation.

VS Code automatically handles this when you press Enter after a colon.

---

# 10. Colon and Code Blocks

Statements that begin a code block usually end with a colon `:`.

Examples:

```python
if condition:
```

```python
for item in items:
```

```python
while condition:
```

The indented lines below them belong to that block.

---

# 11. For Loop with a List

Example:

```python
friends = ["Alice", "Bob", "Charlie"]

for friend in friends:
    print(friend)
```

Output:

```text
Alice
Bob
Charlie
```

---

# 12. For Loop with range()

Example:

```python
for number in range(1, 6):
    print(number)
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

# 13. Performing Calculations in a Loop

We can perform calculations repeatedly.

Example:

```python
for number in range(1, 6):
    print(number * 2)
```

Output:

```text
2
4
6
8
10
```

---

# 14. Adding Numbers Using a Loop

We can use a variable to keep a running total.

```python
total = 0

for number in range(1, 6):
    total = total + number

print(total)
```

Output:

```text
15
```

The value changes during each iteration:

```text
Start: total = 0

After 1: total = 1
After 2: total = 3
After 3: total = 6
After 4: total = 10
After 5: total = 15
```

---

# 15. Loop with if

A loop can contain an `if` statement.

```python
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
```

Output:

```text
2
4
6
8
10
```

Here:

```python
number % 2 == 0
```

checks whether the number is even.

---

# 16. Nested Code Blocks

A code block can contain another code block.

Example:

```python
for number in range(1, 6):
    if number % 2 == 0:
        print(number)
```

There are two levels:

```text
for
    if
        print
```

Indentation shows which statement belongs to which block.

---

# 17. for Loop vs range()

These are different concepts.

### Loop through a list

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

The loop works directly with the items.

### Loop through numbers

```python
for number in range(3):
    print(number)
```

The loop works with generated numbers.

---

# 18. Common Mistakes

## Mistake 1 — Forgetting the colon

Incorrect:

```python
for number in range(5)
    print(number)
```

Correct:

```python
for number in range(5):
    print(number)
```

## Mistake 2 — Incorrect indentation

Incorrect:

```python
for number in range(5):
print(number)
```

Correct:

```python
for number in range(5):
    print(number)
```

## Mistake 3 — Expecting range() to include the stop value

This:

```python
range(1, 5)
```

produces:

```text
1, 2, 3, 4
```

not:

```text
1, 2, 3, 4, 5
```

## Mistake 4 — Confusing item and index

Given:

```python
friends = ["Alice", "Bob", "Charlie"]
```

This gives the items:

```python
for friend in friends:
    print(friend)
```

This gives the indexes:

```python
for index in range(len(friends)):
    print(index)
```

Output:

```text
0
1
2
```

---

# Practice Problems

## Practice 1 — Print Numbers

Print numbers from 1 to 10 using a `for` loop.

for number in range(1,11):
    print(number)

---

## Practice 2 — Even Numbers

Print all even numbers from 1 to 20.

for number in range(1,21):
    if number%2==0:
        print(number)

---

## Practice 3 — Odd Numbers

Print all odd numbers from 1 to 20.

for number in range(1,21):
    if number%2!=0:
        print(number)

---

## Practice 4 — Countdown

Print:

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

using `range()`.


for number in range(10,0,-1):
    print(number)


---

## Practice 5 — Shopping List

Create a shopping list and print each item using a `for` loop.

```python
shopping_list = ["Milk", "Bread", "Apples", "Rice", "Paneer"]

for item in shopping_list:
    print(item)
```

shopping_list = ["Milk", "Bread", "Apples", "Rice", "Paneer"]
for item in shopping_list:
    print(item)
---

## Practice 6 — Sum of Numbers

Calculate the sum of numbers from 1 to 100.

Expected result:

```text
5050
```

total=0
for number in range(1,101):
    total+=number
print(total)

---

## Practice 7 — Multiplication Table

Ask the user for a number and print its multiplication table from 1 to 10.

Example:

```text
Enter a number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

number=int(input("Enter a number="))
result=0
for n in range(1,11):
    result=number*n
    print(f"{number}*{n}={result}")

---

# Mini Project — FizzBuzz

Create a program that prints numbers from 1 to 100.

Rules:

* If the number is divisible by 3, print `Fizz`.
* If the number is divisible by 5, print `Buzz`.
* If the number is divisible by both 3 and 5, print `FizzBuzz`.
* Otherwise, print the number.

You will need:

```python
for
range()
if
elif
else
%
```

### Important

Check the condition for **both 3 and 5 first**.

For example:

```python
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
```

for n in range(1,101):
    if n%3 == 0 and n%5==0:
        print("FizzBuzz") 
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)

---

# Day 5 Key Concepts

| Concept        | Example                       |
| -------------- | ----------------------------- |
| For loop       | `for item in items:`          |
| Range          | `range(5)`                    |
| Start and stop | `range(1, 6)`                 |
| Step           | `range(1, 10, 2)`             |
| Reverse range  | `range(10, 0, -1)`            |
| Indentation    | 4 spaces                      |
| Code block     | Statements belonging together |
| Nested block   | `for` containing `if`         |
| Modulo         | `number % 2`                  |
| Running total  | `total = total + number`      |

---
Summary: 

## Day 5 Summary

- A `for` loop is used to repeat code for each item in a sequence.
- A `for` loop goes through each item in a sequence, one item at a time, and performs an action with each item.
- Loops allow us to execute the same block of code repeatedly without writing it again and again.
- A `for` loop can be used with lists, strings, `range()`, and other sequences.
- Indentation is very important in Python because it defines code blocks.
- `range()` generates a sequence of numbers that can be used with a `for` loop.
- `range(start, stop, step)` allows us to control where the sequence starts, stops, and how much it changes each time.
- The `stop` value in `range()` is not included.
- `sum()` calculates the total of numbers in an iterable such as a list.
- `max()` returns the largest value in an iterable.
- `min()` returns the smallest value.
- `random.shuffle()` randomly changes the order of items in a list.
- `random.choice()` randomly selects one item from a sequence.
- `append()` adds an item to the end of a list.
- `"".join(list)` can combine a list of strings into one string.