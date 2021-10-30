"""
#######################################################
caesar cipher part 3: reorganize code
combining both functions into a single function
#######################################################
"""


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 1 Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(start_text, shift_amount, msg_direction):
    cipher_text = ''

    for letter in start_text:
        position = alphabet.index(letter)
        if msg_direction == 'encode':
            new_position = position + shift_amount
        elif msg_direction == 'decode':
            new_position = position - shift_amount

        cipher_text += alphabet[new_position]

    print(f"The encoded text is {cipher_text}")


caesar(start_text=text, shift_amount=shift, msg_direction=direction)
