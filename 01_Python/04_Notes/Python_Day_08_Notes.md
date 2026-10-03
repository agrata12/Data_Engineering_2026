# 🐍 Python Day 8 — Functions with Inputs & Caesar Cipher

**Date:** 27 September 2026
**Topic:** Functions with Inputs & Caesar Cipher
**Course:** 100 Days of Python

---

# 🎯 What I Learned Today

* Functions with inputs - Parameter and Arguments
* Parameter - name of the data in the function. 
* arguments - actual peice of data that is passed to the function. Actual value of data. 
* Multiple parameters
* Positional and keyword arguments
* Using `return` with function inputs
* Caesar Cipher
* Encryption and decryption
* String indexing
* `.index()`
* Modulo `%`
* Combining functions, loops and conditions
* Building a complete Caesar Cipher program

---

# 1. Functions with Inputs

A function can receive information when it is called.

```python
def greet(name):
    print("Hello " + name)

greet("Agrata")
```

Output:

```text
Hello Agrata
```

Here:

```python
def greet(name):
```

`name` is the **parameter**.

```python
greet("Agrata")
```

`"Agrata"` is the **argument**.

### Easy way to remember

**Parameter = placeholder**

**Argument = actual value**

---

# 2. Multiple Parameters

A function can receive more than one input.

```python
def greet(name, age):
    print("My name is " + name)
    print("I am " + str(age) + " years old.")

greet("Agrata", 34)
```

The values are matched by position:

```text
name → "Agrata"
age  → 34
```

---

# 3. Positional Arguments

The order matters when using positional arguments.

```python
def introduce(name, city):
    print(name)
    print(city)

introduce("Agrata", "Mohali")
```

Python matches:

```text
name → Agrata
city → Mohali
```

---

# 4. Keyword Arguments

We can explicitly specify which value belongs to which parameter.

```python
def introduce(name, city):
    print(name)
    print(city)

introduce(city="Mohali", name="Agrata")
```

The order no longer matters because the parameter names are specified.

---

# 5. Functions Can Process Inputs

A function can receive values, process them and return the result.

```python
def add(a, b):
    result = a + b
    return result

answer = add(5, 3)

print(answer)
```

Output:

```text
8
```

The flow is:

```text
5, 3
 ↓
add()
 ↓
8
 ↓
return
 ↓
answer
```

This combines the Day 6 concept of `return` with today's function inputs.

---

# 6. Caesar Cipher

The main project for Day 8 is the **Caesar Cipher**.

- A Caesar Cipher is a simple substitution technique where each letter is shifted by a fixed number of positions in the alphabet.

Alphabet:

```text
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

For a shift of `3`:

```text
a → d
b → e
c → f
d → g
```

---

# 7. Encryption and Decryption

### Encryption

Converts the original message into an encoded message.

```text
hello
  ↓ shift 3
khoor
```

### Decryption

Reverses the process.

```text
khoor
  ↓ shift 3 backwards
hello
```

The original readable message is called **plaintext**.

The encrypted message is called **ciphertext**.

---

# 8. Alphabet as a List

We can store the alphabet in a list:

```python
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]
```

Each letter has an index:

```text
a b c d e f ... z
0 1 2 3 4 5 ... 25
```

For example:

```python
alphabet.index("c")
```

returns:

```text
2
```

And:

```python
alphabet[2]
```

returns:

```text
c
```

---

# 9. Shifting a Letter

Suppose:

```python
letter = "c"
shift = 3
```

Find the current position:

```python
position = alphabet.index(letter)
```

`c` is at position `2`.

Add the shift:

```python
new_position = position + shift
```

So:

```text
2 + 3 = 5
```

Position `5` is:

```text
f
```

Therefore:

```text
c → f
```

---

# 10. Why We Need Modulo `%`

The alphabet only has indexes `0` to `25`.

What happens with:

```text
z + 3
```

`z` is index `25`.

```text
25 + 3 = 28
```

There is no index `28`.

We use:

```python
new_position = (position + shift) % 26
```

Because:

```text
28 % 26 = 2
```

Index `2` is `c`.

Therefore:

```text
z → c
```

### `%` means remainder

```python
28 % 26
```

gives:

```text
2
```

This allows the alphabet to **wrap around**.

---

# 11. Encoding

For encryption, move forward:

```python
new_position = position + shift
```

For example:

```text
a + 3 → d
```

---

# 12. Decoding

For decryption, move backward:

```python
new_position = position - shift
```

For example:

```text
d - 3 → a
```

---

# 13. Handling Spaces and Symbols

Not every character is in the alphabet.

For example:

```text
hello world!
```

contains:

* letters
* a space
* `!`

We only want to shift letters.

```python
if letter in alphabet:
    # shift the letter
else:
    # keep it unchanged
```

So:

```text
hello world!
```

with shift `3` becomes:

```text
khoor zruog!
```

The space and `!` remain unchanged.

---

# 14. Complete Caesar Cipher Program

```python
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]


def caesar(text, shift, direction):

    result = ""

    for letter in text:

        if letter in alphabet:

            position = alphabet.index(letter)

            if direction == "encode":
                new_position = position + shift

            elif direction == "decode":
                new_position = position - shift

            new_position = new_position % 26

            result += alphabet[new_position]

        else:
            result += letter

    return result


direction = input(
    "Type 'encode' to encrypt or 'decode' to decrypt: "
).lower()

text = input("Type your message: ").lower()

shift = int(input("Type the shift number: "))

output = caesar(text, shift, direction)

print(f"Result: {output}")
```

---

# 15. Understanding the Complete Program

### Step 1 — Alphabet

```python
alphabet = [...]
```

Stores the 26 letters.

### Step 2 — Function

```python
def caesar(text, shift, direction):
```

The function receives three inputs:

```text
text
shift
direction
```

### Step 3 — Empty result

```python
result = ""
```

We will build the encrypted/decrypted message here.

### Step 4 — Loop through the message

```python
for letter in text:
```

Checks every character one at a time.

### Step 5 — Check if it is a letter

```python
if letter in alphabet:
```

Only alphabet letters are shifted.

### Step 6 — Find the letter's position

```python
position = alphabet.index(letter)
```

### Step 7 — Encode or decode

```python
if direction == "encode":
    new_position = position + shift

elif direction == "decode":
    new_position = position - shift
```

### Step 8 — Wrap around

```python
new_position = new_position % 26
```

### Step 9 — Get the new letter

```python
result += alphabet[new_position]
```

### Step 10 — Keep spaces and symbols

```python
else:
    result += letter
```

### Step 11 — Return the result

```python
return result
```

The function sends the completed message back.

---

# 🧪 Example

### Encryption

Input:

```text
Type 'encode' to encrypt or 'decode' to decrypt: encode
Type your message: hello world
Type the shift number: 3
```

Output:

```text
Result: khoor zruog
```

### Decryption

Input:

```text
Type 'encode' to encrypt or 'decode' to decrypt: decode
Type your message: khoor zruog
Type the shift number: 3
```

Output:

```text
Result: hello world
```

---

# 🔑 Important Concepts

| Concept        | Example               | Meaning                         |
| -------------- | --------------------- | ------------------------------- |
| Parameter      | `text`                | Input placeholder in function   |
| Argument       | `"hello"`             | Actual value passed to function |
| `return`       | `return result`       | Sends result back               |
| `.index()`     | `alphabet.index("c")` | Finds position                  |
| `%`            | `% 26`                | Wraps around alphabet           |
| `in`           | `letter in alphabet`  | Checks membership               |
| `for`          | `for letter in text`  | Processes each character        |
| `if/elif/else` | Encode/decode         | Makes decisions                 |
| `int()`        | `int(input())`        | Converts text to integer        |

---

# ⚠️ Common Mistakes

### 1. Forgetting `int()`

❌

```python
shift = input("Shift: ")
```

`shift` becomes a string.

✅

```python
shift = int(input("Shift: "))
```

---

### 2. Using `[]` instead of `()`

❌

```python
random.choice[letters]
```

✅

```python
random.choice(letters)
```

Remember:

```text
() → call a function
[] → access/index something
```

---

### 3. Forgetting `return`

If the function needs to send the result back:

```python
return result
```

Then:

```python
output = caesar(text, shift, direction)
```

can store that returned value.

---

### 4. Forgetting `% 26`

Without modulo, shifting beyond `z` can create an invalid list index.

```python
new_position = new_position % 26
```

---

# 🧠 Day 8 Connection to Previous Days

| Previous Concept | Day 8 Use                    |
| ---------------- | ---------------------------- |
| Variables        | `text`, `shift`, `result`    |
| Strings          | Message                      |
| Lists            | Alphabet                     |
| Indexing         | Access letters               |
| `for` loop       | Process each character       |
| `if/else`        | Encode/decode                |
| Functions        | `caesar()`                   |
| Function inputs  | `text`, `shift`, `direction` |
| `return`         | Return final result          |
| `%`              | Alphabet wrap-around         |
| `input()`        | Get user input               |
| `int()`          | Convert shift to number      |

---

# 📝 Practice

## Practice 1 — Function Input

Create:

```python
def greet(name):
    print("Hello " + name)
```

Call it with your name.

---

## Practice 2 — Multiple Inputs

Create:

```python
def add_numbers(a, b):
    return a + b
```

Test it with different numbers.

---

## Practice 3 — Keyword Arguments

Create:

```python
def introduce(name, city):
    print(name)
    print(city)
```

Call it using keyword arguments in a different order.

---

## Practice 4 — `.index()`

Predict the result before running:

```python
print(alphabet.index("a"))
print(alphabet.index("m"))
print(alphabet.index("z"))
```

---

## Practice 5 — Modulo

Predict:

```python
print(28 % 26)
print(30 % 26)
print(52 % 26)
```

---

## Practice 6 — Caesar Cipher

Encrypt:

```text
hello
```

using:

```text
shift = 5
```

Try to predict the answer before running the program.

---

# 🚀 Day 8 Goal

By the end of Day 8, I should be able to:

* Create functions with inputs.
* Explain parameter vs argument.
* Use multiple parameters.
* Use positional and keyword arguments.
* Use `return` with function inputs.
* Explain the basic idea of encryption.
* Explain how a Caesar Cipher works.
* Use `.index()` to find a letter's position.
* Use `% 26` to wrap around the alphabet.
* Build and understand a complete Caesar Cipher program.

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

**What did I learn about parameters and arguments?**

*

**What did I learn about `%`?**

*

**What part of the Caesar Cipher was hardest?**

*

**Self-score:** ___ / 10
