# Python Day 3 — Conditional Statements, Logical Operators, Code Blocks and Scope

## 1. Conditional Statements

Conditional statements allow Python to make decisions based on whether a condition is True or False.

Basic syntax:

if condition:
    # code to execute if condition is True

Example:

age = 18

if age >= 18:
    print("You are an adult.")


## 2. if Statement

The if statement executes code only when a condition is True.

Example:

age = 20

if age >= 18:
    print("You can vote.")

## 3. Comparison Operators

Comparison operators compare two values.

>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to
==  Equal to
!=  Not equal to

Examples:

5 > 3       # True
5 < 3       # False
5 == 5      # True
5 != 3      # True
5 >= 5      # True
4 <= 3      # False


## 4. if / else

else is executed when the if condition is False.

Example:

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


## 5. if / elif / else

elif means "else if".

It allows us to check multiple conditions.

Example:

age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

## 6. Nested if Statements

An if statement can be placed inside another if statement.

Example:

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required.")
else:
    print("Entry not allowed.")


## 7.  Multiple if Statements

if Condition1:
    do A
if Condition2: 
    do B
if Condition 3:
    do C

eg: Roller Coaster program

## 8. Logical Operators

Logical operators combine conditions.

### AND

Both conditions must be True.

Example:

age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed.")


### OR

At least one condition must be True.

Example:

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


### NOT

Reverses True/False.

Example:

is_raining = False

if not is_raining:
    print("You don't need an umbrella.")


## 9. Modulo Operator %

The % operator gives the remainder after division.

Examples:

10 % 2 = 0
10 % 3 = 1
7 % 2 = 1

It can be used to check whether a number is even or odd.

Example:

number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


## 10. Indentation

Indentation is very important in Python.

Example:

if age >= 18:
    print("Adult")

The print statement is indented because it belongs to the if block.

Python uses indentation to define blocks of code.

## 11. Important Difference: = vs ==

= is the assignment operator.

Example:

age = 34

It assigns 34 to age.

== is the comparison operator.

Example:

age == 34

It checks whether age is equal to 34.


## 12. Truth Values

Conditions evaluate to either:

True
False

Example:

print(10 > 5)

Output:

True


## 13. Other practice Examples

Example 1: BMI Calculator 

height=float(input("enter height in m="))
weight=float(input("Enter Weight in Kg="))
bmi=round(weight/(height**2),2)
if bmi < 18.5:
    print(f"Your BMI = {bmi}. You are underweight")
elif bmi < 25:
    print(f"Your BMI = {bmi}. You are normal weight")
elif bmi >=25:
    print(f"Your BMI = {bmi}. You are overweight")


## 14. Important Things to Remember

- if is used to make decisions.
- elif checks another condition when the previous condition is False.
- else runs when all previous conditions are False.
- else is optional.
- Python uses indentation to define blocks.
- = assigns a value.
- == compares values.
- and requires all conditions to be True.
- age>=45 and age<=55 can also be written as 45<=age<=55
- or requires at least one condition to be True.
- not reverses a Boolean value.
- % gives the remainder.
- exit() function helps to terminate the program after a condition.
- to insert ASCII art, we use print and single quotes. three single quotes help in multiline printing. link of ascii art 
https://ascii.co.uk/art
- backslash used to escape symbol. eg: print('You\'re at crossroads.')
- lower() converts to lower case

## 15. Practice Problems

### Problem 1 — Even or Odd

Ask the user for a number and determine whether it is even or odd.

n=float(input("Enter number="))
if n% 2 == 0:

     print("Even")
else:
     print("Odd")

### Problem 2 — Age Checker in Roller Coaster

print("Welcome to Roller Coaster")
height=float(input("Enter your height in cm="))
bill = 0
if height >=150:
    age=int(input("Enter your age="))
    if age <= 12:
        bill +=10
        print("You can Ride. Child Ticket $10")
    elif age >13 and age<=18:
         bill+= 15
         print("You can Ride. Youth Ticket $15")
    elif age >=45 and age <=55:
        bill +=0
        print("You can Ride. Lucky Free Ticket")
    else: 
        bill+=20
        print("You can ride. Adult Ticket $20")
    wants_photo=input("Do you want a picture? Type y for Yes and n for No=")
    if wants_photo == "y" or wants_photo=="Y":
        bill+=3 
        print("Your photo cost $3.")
    elif wants_photo == "n" or wants_photo=="N":
        print("No Photo")
    print(f"Total Bill= ${bill}")
else:
    print("Better Luck Next Time.")


### Problem 3 — Pizza Order

Ask the user whether they want a small, medium or large pizza and calculate the price.

print("Welcome to Pizza Deliveries!!!")
pizza_size=input("What pizza size do you want? Small S, Medium M or Large L=")
bill=0
if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
elif pizza_size == "L":
    bill = 25
else:
    print("Wrong input. Select S , M or L. ")
    exit()
pepperoni= input("Do you want pepproni? Y or N=")
extra_cheese = input("Do you want extra cheese? Y or N=")
if pepperoni == "Y":
    if pizza_size == "S":
        bill+=5
    else:
        bill+=10
if extra_cheese == "Y":
    bill +=5
print(f"Your Total Bill = Rs {bill}")


## 16. Mini Project

### Project: Treasure Island / Adventure Game

What I built:


print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
      ''' )
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
your_choice=input("Lets Play!\nDo you want to go Left or Right? Write L or R = ")
if your_choice == 'l' or your_choice == 'L':
    swim=input("Welcome to the River. Do you wish to swim or wait for boat? Write S for Swim and W for wait = ")
    if swim == "W" or swim == "w":
        door= input("Which door you wish to enter. R for Red, B for Blue or Y for Yellow = ")
        if door == "Y" or door == "y":
            print("YOU WIN.")
        elif door == "R" or door == "r":
            print("FIRE. GAME OVER.")
        elif door == "B" or door == "b":
            print("WATER. GAME OVER.")    
        else: 
            print("Make better choices. GAME OVER!")
    elif swim == "S" or swim == "s":
        print("Sorry. Attacked by Trout. GAME OVER")
    else:
        print("Wrong Input. Write S for Swim and W for wait.")
elif your_choice == 'r' or your_choice == 'R':
    print("You are in a hole. GAME OVER") 
else: 
    print("Wrong Input. Write L for Left or R for Right.")    


Concepts used:

- input()
- variables
- if
- elif
- else
- comparison operators
- logical operators
- indentation
- ASCII Art

## 16. Day 3 Reflection

What was confusing: implicit data conversion