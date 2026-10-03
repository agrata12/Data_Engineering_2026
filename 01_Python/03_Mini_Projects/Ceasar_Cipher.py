print('''
           ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
          a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
          8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
          "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
           `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"Y8bbdP"' `"8bbdP"Y8 88          
                                                                                                            
''')

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]
def caesar_cipher(text, shift, direction):
    result=""
    for letter in text:
        if letter in alphabet:
            position=alphabet.index(letter)
            if direction == "e":
                new_position=(position+shift)%26
            else:
                new_position=(position-shift)%26
            result+=alphabet[new_position]
        else:
            result+=letter
    return result

# def encrypt(text,shift):
#     result=""
#     for letter in text: 
#         if letter in alphabet:
#             position=alphabet.index(letter)
#             new_position=(position+shift)%26
#             result+=alphabet[new_position]
#         else:
#             result+=letter
#     return result
# def decrypt(text,shift):
#     result=""
#     for letter in text: 
#         if letter in alphabet:
#             position=alphabet.index(letter)
#             new_position=(position-shift)%26
#             result+=alphabet[new_position]
#         else:
#             result+=letter
#     return result

direction=input("Encode or decode:Press E for encode and D for Decode:").lower()
text=input("Enter the text to wish to use:")
shift=int(input("Enter the shift value:"))
output=caesar_cipher(text,shift,direction)
print(f"{text} now becomes {output}")