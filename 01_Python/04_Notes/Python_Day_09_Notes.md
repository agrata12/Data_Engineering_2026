# 🐍 Python Day 9 — Dictionaries, Nesting & Secret Auction

## 1. Dictionaries

A **dictionary** stores data as **key-value pairs**.
- allow us to group together related pieces of data
- more than one {Key:Value}pairs are separated in dictionary usiing comma. 
- Syntax: 
{Key:Value}
eg: {"Bug":"An error in the program that prevents the program from running as expected",
"Function":"Code that you can call again and again",
"Loop":"Action of doing something again and again"}

- for ease of reading, it can be indented. 
- best case practoce to end each line with comma, in case we need to add more lines later
- can be considered as table.
- to access the value in the dictionary we have to access it using Key. 
- KeyError comes if the key is either misspelled or missing or etc
- common error is with data types
- each key can only have one value unless it is a list or any other nested dictionary


### Basic syntax

```python
student = {
    "name": "Angela",
    "age": 25,
    "course": "Python"
}
```

Think of it as:

```text
key       value
----------------
name  →   Angela
age   →   25
course →  Python
```

Unlike a list, a dictionary uses a **key** to access a value.

### List vs Dictionary

```python
fruits = ["apple", "banana", "mango"]
```

List:

```python
print(fruits[0])
```

Result:

```text
apple
```

Dictionary:

```python
student = {
    "name": "Angela",
    "age": 25
}

print(student["name"])
```

Result:

```text
Angela
```

---

# 2. Creating a Dictionary

```python
student = {
    "name": "Agrata",
    "age": 34,
    "city": "Mohali"
}
```

Keys:

```text
"name"
"age"
"city"
```

Values:

```text
"Agrata"
34
"Mohali"
```

- A dictionary can contain different data types.

```python
person = {
    "name": "Agrata",
    "age": 34,
    "student": True
}
```

---

# 3. Accessing Values

Use the key inside square brackets:

```python
print(person["name"])
print(person["age"])
```

Output:

```text
Agrata
34
```

### Important

This:

```python
person["name"]
```

means:

> Find the value associated with the key `"name"`.

---

# 4. Adding a New Item

You can add a new key-value pair:

```python
person["country"] = "India"
```

Now:

```python
print(person)
```

gives something like:

```text
{
    "name": "Agrata",
    "age": 34,
    "student": True,
    "country": "India"
}
```

---

# 5. Changing a Value

You can change an existing value using its key.

```python
person["age"] = 35
```

The value of `"age"` is now `35`.

### Important idea

The same syntax can:

* add a new key
* change an existing key

```python
dictionary["key"] = value
```

If the key already exists → **update**

If the key doesn't exist → **add**

---

# 6. Empty Dictionary

You can create an empty dictionary:

```python
student = {}
```

Then add information:

```python
student["name"] = "Agrata"
student["age"] = 34
```

This is useful when building a dictionary gradually.

---

# 7. Removing Items

Use `del`:

```python
del person["age"]
```

The `"age"` key and its value are removed.

You can also remove everything:

```python
person.clear()
```

---

# 8. Looping Through a Dictionary

Example:

```python
student = {
    "name": "Agrata",
    "age": 34,
    "city": "Mohali"
}
```

### Loop through keys

```python
for key in student:
    print(key)
```

Output:

```text
name
age
city
```

### Loop through values

```python
for value in student.values():
    print(value)
```

Output:

```text
Agrata
34
Mohali
```

### Loop through both

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Agrata
age 34
city Mohali
```

---

# 9. Dictionary Methods

### `.keys()`

```python
student.keys()
```

Gives the keys.

### `.values()`

```python
student.values()
```

Gives the values.

### `.items()`

```python
student.items()
```

Gives key-value pairs.

Example:

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

---

# 10. Nesting

**Nesting means putting one data structure inside another.**

You can nest:

* dictionary inside dictionary
* list inside dictionary
* dictionary inside list
* list inside list

---

## Dictionary inside a Dictionary

```python
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    }
}
```

Here:

```text
travel_log
    ↓
France
    ↓
cities_visited → list
total_visits → 12
```

Access:

```python
print(travel_log["France"]["total_visits"])
```

Result:

```text
12
```

---

# 11. List Inside a Dictionary

```python
student = {
    "name": "Agrata",
    "subjects": ["Python", "SQL", "Excel"]
}
```

Access the list:

```python
print(student["subjects"])
```

Result:

```text
["Python", "SQL", "Excel"]
```

Access an individual item:

```python
print(student["subjects"][0])
```

Result:

```text
Python
```

Notice the two levels:

```python
student["subjects"][0]
```

First:

```text
student["subjects"]
```

finds the list.

Then:

```text
[0]
```

gets the first item from that list.

---

# 12. List of Dictionaries

Another common structure:

```python
students = [
    {
        "name": "Alice",
        "age": 25
    },
    {
        "name": "Bob",
        "age": 30
    }
]
```

Access Bob's name:

```python
print(students[1]["name"])
```

Result:

```text
Bob
```

Think:

```text
students
   ↓
index 1
   ↓
Bob's dictionary
   ↓
"name"
   ↓
Bob
```

---

# 13. Travel Log Example

A useful nested structure:

```python
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 5
    }
]
```

This is:

```text
List
 ├── Dictionary
 │    ├── country
 │    ├── cities_visited → List
 │    └── total_visits
 │
 └── Dictionary
      ├── country
      ├── cities_visited → List
      └── total_visits
```

This is an important real-world data structure because APIs and databases often return data in similar nested forms.

---

# 🔨 Secret Auction Project

The Secret Auction project combines several things you've already learned:

* functions
* loops
* conditionals
* dictionaries
* user input
* comparison
* Boolean values

The goal:

> Several people enter their names and bids. At the end, the program finds the person with the highest bid.

---

# 14. Basic Auction Dictionary

Example:

```python
bids = {
    "Alice": 100,
    "Bob": 150,
    "Charlie": 120
}
```

Here:

```text
key       value
----------------
Alice  →  100
Bob    →  150
Charlie → 120
```

The **name** is the key.

The **bid** is the value.

---

# 15. Adding Bids

Start with:

```python
bids = {}
```

Get the user's information:

```python
name = input("What is your name? ")
bid = int(input("What is your bid? "))
```

Add it:

```python
bids[name] = bid
```

For example:

```text
name = Alice
bid = 100
```

creates:

```python
{
    "Alice": 100
}
```

Another person:

```text
name = Bob
bid = 150
```

becomes:

```python
{
    "Alice": 100,
    "Bob": 150
}
```

---

# 16. Asking for Another Bid

Use a Boolean variable:

```python
more_bidders = True
```

Then:

```python
while more_bidders:
```

Ask:

```python
name = input("What is your name? ")
bid = int(input("What is your bid? "))

bids[name] = bid

again = input("Are there any other bidders? yes/no: ").lower()

if again == "no":
    more_bidders = False
```

---

# 17. Finding the Highest Bid

Suppose:

```python
bids = {
    "Alice": 100,
    "Bob": 150,
    "Charlie": 120
}
```

We need to compare all the bids.

Start with:

```python
highest_bid = 0
winner = ""
```

Then:

```python
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder
```

Finally:

```python
print(f"The winner is {winner} with a bid of ${highest_bid}.")
```

---

# 18. Understanding the Winner Calculation

This is the most important part.

Given:

```python
bids = {
    "Alice": 100,
    "Bob": 150,
    "Charlie": 120
}
```

Start:

```text
highest_bid = 0
winner = ""
```

### Alice

```text
100 > 0
```

True.

So:

```text
highest_bid = 100
winner = Alice
```

### Bob

```text
150 > 100
```

True.

So:

```text
highest_bid = 150
winner = Bob
```

### Charlie

```text
120 > 150
```

False.

Nothing changes.

Final:

```text
winner = Bob
highest_bid = 150
```

---

# 19. Complete Secret Auction Program

```python
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
continue_bidding = True

while continue_bidding:

    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bids[name] = bid

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no': "
    ).lower()

    if should_continue == "no":
        continue_bidding = False

find_highest_bidder(bids)
```

---

# 20. Important New Concepts

### Dictionary

```python
bids = {}
```

Stores related information as:

```text
key → value
```

### Adding to dictionary

```python
bids[name] = bid
```

### Accessing dictionary value

```python
bids[bidder]
```

### Looping through dictionary

```python
for bidder in bids:
```

This gives you the **keys**.

### Getting the value

```python
bids[bidder]
```

gets the bid associated with that bidder.

### Finding maximum manually

```python
if bid_amount > highest_bid:
```

If the current bid is higher, replace the previous highest bid.

---

# 🧠 Day 9 Key Takeaways

```text
Dictionary
    ↓
key → value

Example:
"name" → "Agrata"
"age"  → 34
```

Access:

```python
person["name"]
```

Add/update:

```python
person["country"] = "India"
```

Loop:

```python
for key, value in person.items():
```

Nesting:

```python
dictionary → list
list → dictionary
dictionary → dictionary
```

Secret Auction:

```text
Collect bids
     ↓
Store in dictionary
     ↓
Loop through bids
     ↓
Compare each bid
     ↓
Keep highest bid
     ↓
Print winner
```

## ⭐ Concepts to remember from Day 9

1. Dictionary = **key + value**
2. `dictionary["key"]` gets a value.
3. `dictionary["new_key"] = value` adds an item.
4. Existing keys can be updated.
5. `.items()` gives key + value together.
6. Nesting means putting one data structure inside another.
7. A list can contain dictionaries.
8. A dictionary can contain lists.
9. `bids[name] = bid` stores auction data.
10. A loop + comparison can find the highest value.
11. `return` gives a result back from a function.
12. `print()` only displays the result.
