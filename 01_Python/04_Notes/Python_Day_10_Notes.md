# 🐍 Python Day 10 — Functions with Inputs, Outputs & Mini-Project


# ⭐ Day 10 — Points to Remember

### Functions

1. `def` is used to create a function.
2. **Parameter** = placeholder inside the function.
3. **Argument** = actual value passed to the function.
4. A function can have one or multiple inputs.

### Outputs

5. `print()` displays something.
6. `return` gives a value back.
7. A function without `return` gives `None`.
8. `return` immediately ends the function.

### New Concepts

9. **Docstring** = documentation written inside a function using `""" """`.
10. **Recursion** = a function calling itself.
11. Recursion needs a **stopping condition**.
12. Functions can be stored as dictionary values.
13. `add` → refers to the function.
14. `add()` → calls/runs the function.

### Most important idea

```text
Input
  ↓
Function
  ↓
Output / Action
```

And remember:

```text
add     → function reference
add()   → function call
```
-------------------------------------------------

## 1. Functions

A function is a reusable block of code.

```python
def greet():
    print("Hello!")

greet()
```

---

## 2. Functions with Inputs

A function can receive information through **parameters**.

```python
def greet(name):
    print(f"Hello {name}!")

greet("Agrata")
```

* `name` → parameter
* `"Agrata"` → argument

### Multiple Inputs

```python
def add(a, b):
    print(a + b)

add(5, 3)
```

---

## 3. Functions with NO Return

A function does not always need to return a value.

```python
def greet(name):
    print(f"Hello {name}!")

greet("Agrata")
```

This function performs an action — it prints something.

If there is no `return`, Python automatically returns:

```python
None
```

Example:

```python
def greet(name):
    print(f"Hello {name}!")

result = greet("Agrata")
print(result)
```

Output:

```text
Hello Agrata!
None
```

### Remember

```text
No return → performs an action
return → gives a value back
```

---

## 4. Functions with Outputs

Use `return` when you want the function to give a value back.

```python
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
```

Output:

```text
8
```

The returned value can be stored and used later.

```python
result = add(5, 3)
final = result * 2

print(final)
```

Output:

```text
16
```

---

## 5. `print()` vs `return`

```text
print  → SHOW me
return → GIVE me
```

Example:

```python
def add(a, b):
    print(a + b)
```

This displays the answer.

But:

```python
def add(a, b):
    return a + b
```

This gives the answer back so you can use it.

---

## 6. `return` Ends the Function

```python
def test():
    return 10
    print("Hello")
```

`"Hello"` will not run because `return` ends the function.

---

## 7. Doc Strings
- way for us yo create little bits of documentation as we code along in our functions. 
- the first intended line after we define function. 
- its in three quotation marks 

eg:
def format_name():
    """Take first and last name and format in title case."""

## *. Recursion
- calling a function within the function
eg: inside calculator function

## New concept today: 
- save in dictionary keys and pass functions as values. 
- eg: operations={ "+": add, } 
    # here add is the function name we using or you can say it refers to the add function already defined. 
    if we had added add() , it would have called the function. 

# 🧩 7. Real-World Mini-Project — Simple Bill Calculator

### Scenario

Imagine you are creating a small billing program for a shop.

The customer enters:

* Item price
* Quantity
* Discount percentage

The program calculates the final bill.

### Step 1 — Function with Inputs and Output

```python
def calculate_total(price, quantity):
    return price * quantity
```

Test it:

```python
total = calculate_total(100, 3)

print(total)
```

Output:

```text
300
```

---

### Step 2 — Add Discount

```python
def calculate_discount(total, discount_percent):
    discount = total * discount_percent / 100
    return discount
```

Example:

```python
discount = calculate_discount(300, 10)

print(discount)
```

Output:

```text
30.0
```

---

### Step 3 — Calculate Final Amount

```python
def calculate_final_amount(total, discount):
    return total - discount
```

Example:

```python
final_amount = calculate_final_amount(300, 30)

print(final_amount)
```

Output:

```text
270
```

---

# 🛒 Complete Mini-Project

```python
def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(total, discount_percent):
    discount = total * discount_percent / 100
    return discount


def calculate_final_amount(total, discount):
    return total - discount


price = float(input("Enter item price: ₹"))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount (%): "))


total = calculate_total(price, quantity)

discount = calculate_discount(total, discount_percent)

final_amount = calculate_final_amount(total, discount)


print(f"Total: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")
```

### Example Run

```text
Enter item price: ₹500
Enter quantity: 3
Enter discount (%): 10

Total: ₹1500
Discount: ₹150.0
Final Amount: ₹1350.0
```

---

# 🧠 What You Practiced

This mini-project uses:

* `input()`
* `int()`
* `float()`
* Functions
* Parameters
* Arguments
* `return`
* Variables
* Arithmetic
* Multiple functions
* f-strings

### Function flow

```text
Price + Quantity
       ↓
calculate_total()
       ↓
    Total
       ↓
calculate_discount()
       ↓
   Discount
       ↓
calculate_final_amount()
       ↓
 Final Amount
```

---

# ✏️ Day 10 Practice

### Practice 1

Create a function that takes a person's age and **prints** whether they are an adult.


def check_adult_age(age):
    # age=int(input("Enter your age:"))
    if age >=18:
        print("Adult")
    else:
        print("Child")
check_age=int(input("Enter your age:"))
check_adult_age(check_age)

### Practice 2

Create a function that takes two numbers and **returns** the larger number.


def highest_no(num1,num2):
    highest=0
    if num1<num2:
        highest=num2
    else:
        highest=num1
    return highest
high_no=0
n1=int(input("Enter Num1:"))
n2=int(input("Enter Num2:"))
high_no=highest_no(n1,n2)
print("Highest no is=",high_no)

### Practice 3

Create a function that takes `hours` and `rate_per_hour` and **returns** salary.

Example:

```python
salary = calculate_salary(8, 500)
print(salary)
```

Expected:

```text
4000
```


def calc_salary(hrs,rate):
    salary=0
    salary=hrs*rate
    return salary
working_hrs=int(input("Enter no of hrs working="))
rate=int(input("Enter rate per hour="))
total_salary=0
total_salary=calc_salary(working_hrs,rate)
print(f"your salary for {working_hrs} hrs at {rate} per hour is {total_salary}")


### Practice 4 — Mini Challenge

Modify the **Bill Calculator** so it also accepts a tax percentage.

Final calculation:

```text
Total
  ↓
Discount
  ↓
Amount after discount
  ↓
Tax
  ↓
Final Amount
```

def final_rate(price,q):
    total=price*q
    return total

def calc_discount(dis):
    discount=(dis/100)*total
    return discount

def total_bill(total,discount,tax):
    discounted_bill=total-discount
    final=discounted_bill+((tax/100)*discounted_bill)
    return final

item_price=float(input("Enter Item Price: "))
qty=float(input("Enter Quantity: "))
discount=float(input("Enter Discount %. if any: "))
tax=float(input("Enter tax %: "))

total=final_rate(item_price,qty)
discount=round(calc_discount(discount),2)
final_bill= round(total_bill(total,discount,tax),2)

print("\n")
print(f"Total: {total}")
print(f"Discount: {discount}")
print(f"Tax%: {tax}%")
print(f"Final Bill: Rs {final_bill}")

---

# ⭐ Day 10 Key Takeaways

```text
Parameter = placeholder
Argument  = actual value

print()  = displays something
return   = gives something back

No return = function returns None
```

### Main idea

```text
Input → Function → Output
```

And sometimes:

```text
Input → Function → Action
                 ↓
                print()
```
----------------------------------------------------------
# 🐍 Python Day 10 — Functions with Inputs, Outputs & More

## 1. Functions with Inputs

A function can receive information through **parameters**.

```python
def greet(name):
    print(f"Hello {name}!")

greet("Agrata")
```

* `name` → parameter
* `"Agrata"` → argument

### Multiple Inputs

```python
def add(a, b):
    print(a + b)

add(5, 3)
```

---

## 2. Functions with No Return

A function does not always need to return a value.

```python
def greet(name):
    print(f"Hello {name}!")

greet("Agrata")
```

This function performs an action but has no `return`.

If there is no `return`, Python automatically returns:

```python
None
```

---

## 3. Functions with Outputs

Use `return` when you want a function to give a value back.

```python
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
```

Output:

```text
8
```

### Remember

```text
print  → SHOW me
return → GIVE me
```

---

## 4. `return` Ends the Function

```python
def test():
    return 10
    print("Hello")
```

`"Hello"` will not run because `return` ends the function.

---

## 5. Docstrings

A **docstring** is a small piece of documentation that explains what a function does.

It is written immediately inside the function using **triple quotes**.

```python
def format_name(first_name, last_name):
    """Take first and last name and format in title case."""
```

The docstring explains the purpose of the function.

You can also see it using:

```python
help(format_name)
```

### Remember

```text
"""Documentation about the function."""
```

---

## 6. Recursion

**Recursion** means a function calls itself.

Simple example:

```python
def countdown(number):
    if number == 0:
        return

    print(number)
    countdown(number - 1)
```

Here:

```text
countdown(3)
    ↓
countdown(2)
    ↓
countdown(1)
    ↓
countdown(0)
```

A recursive function needs a **stopping condition**, otherwise it will keep calling itself.

---

## 7. Functions as Dictionary Values

Python allows us to store **functions as values in a dictionary**.

Example:

```python
operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}
```

Here:

```python
"+" → add function
"-" → sub function
```

`add` refers to the function already defined.

### Why not `add()`?

```python
"+": add
```

means:

> Store the function.

But:

```python
"+": add()
```

means:

> Call/run the function immediately.

### Using the stored function

```python
operation = operations["+"]
answer = operation(5, 3)

print(answer)
```

Output:

```text
8
```

You can also write:

```python
answer = operations["+"](5, 3)
```

---

# 🧩 8. Real-World Mini-Project — Simple Bill Calculator

```python
def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(total, discount_percent):
    discount = total * discount_percent / 100
    return discount


def calculate_final_amount(total, discount):
    return total - discount


price = float(input("Enter item price: ₹"))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount (%): "))

total = calculate_total(price, quantity)
discount = calculate_discount(total, discount_percent)
final_amount = calculate_final_amount(total, discount)

print(f"Total: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")
```

Example:

```text
Enter item price: ₹500
Enter quantity: 3
Enter discount (%): 10

Total: ₹1500
Discount: ₹150.0
Final Amount: ₹1350.0
```

---

# ⭐ Day 10 — Points to Remember

### Functions

1. `def` is used to create a function.
2. **Parameter** = placeholder inside the function.
3. **Argument** = actual value passed to the function.
4. A function can have one or multiple inputs.

### Outputs

5. `print()` displays something.
6. `return` gives a value back.
7. A function without `return` gives `None`.
8. `return` immediately ends the function.

### New Concepts

9. **Docstring** = documentation written inside a function using `""" """`.
10. **Recursion** = a function calling itself.
11. Recursion needs a **stopping condition**.
12. Functions can be stored as dictionary values.
13. `add` → refers to the function.
14. `add()` → calls/runs the function.

### Most important idea

```text
Input
  ↓
Function
  ↓
Output / Action
```

And remember:

```text
add     → function reference
add()   → function call
```
