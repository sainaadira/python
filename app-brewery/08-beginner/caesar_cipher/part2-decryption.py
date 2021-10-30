
"""
#######################################################
caesar cipher part 2
decrypting the message
#######################################################
"""

# adding alphabet twice to this list for letter that are close to the end, shift can loop back to beginning
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# encypting message


def encrypt(plain_text, shift_amount):
    encrypt_message = ''
    # looping through letters in plain text(alphabet)
    for letter in plain_text:
        # grabbing the index of the letter from alphabet
        position = alphabet.index(letter)
        # setting new postion to be postion + shift amount
        new_position = position + shift_amount
        # adding new position of aphabet to encrypt message

        encrypt_message += alphabet[new_position]
    print(f"The encoded text is {encrypt_message}")

# decrypting message


def decrypt(cipher_text, shift_amount):
    decrpt_message = ''
    for letter in cipher_text:
        position = alphabet.index(letter)
        # to move the postion backwards
        new_position = position - shift_amount
        decrpt_message += alphabet[new_position]
    print(f'your decoded message is: {decrpt_message}')

    # 2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"


# 3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
