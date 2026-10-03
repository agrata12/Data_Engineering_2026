# #multiple parameters
# def greet(name,age):
#     print(f"I,{name}, am {age}years old")

# greet("Agrata",34)
# #positional 
# def introduce(name,city):
#     print(name,city)
# introduce(city="mohali", name="Agrata")

# #inputs
# def add(a,b):
#     result=a+b
#     return result
# answer=add(5,6)
# print(answer)
#ceasar cipher

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]
# new_alphabet=[]
# old_alphabet=[]
# position=0
# new_position=0
# old_position=0
# shift=int(input("Enter shift value="))
# # new_position=position+shift
# for position in range(0,26):
#     new_position=position+shift
#     if new_position >25:
#         new_position=(position+shift)%26
#     new_alphabet.append(alphabet[new_position])
# print(new_alphabet)
# for new_position in range(0,26):
#     old_position=new_position-shift
#     if old_position<=0:
#         old_position=(new_position-shift)%26
#     old_alphabet.append(new_alphabet[old_position])
# print(old_alphabet)

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]
def ceasar(text,shift,direction):
    result=""
    for letter in text:
        if letter in alphabet:
            position=alphabet.index(letter)
            if direction == "e":
                new_position=position+shift
            else:
                new_position=position-shift
            new_position=new_position%26
            result=alphabet[new_position]
            return result
        else:
            result+=letter

text=input("Enter the text to wish to use:")
shift=int(input("Enter the shift value:"))
direction=input("Encode or decode:Press E for encode and D for Decode:").lower()
output=ceasar(text,shift,direction)
print(f"Result:{output}")