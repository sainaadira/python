
"""
#######################################################
caesar cipher part 1

encrypting the message
#######################################################
"""

# adding alphabet twice to this list for letter that are close to the end, shift can loop back to beginning
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amount):
    # -2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    # e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"
    encrypt_message = ''

    for letter in plain_text:
        # find the index of the letter that i'm looping through in alphabet
        position = alphabet.index(letter)
       # calculate new postion by adding shift amount to index postion
        new_postion = position + shift_amount
    # setting the new letter based on shift amount
        new_letter = alphabet[new_postion]

        encrypt_message += new_letter

    print(f'the encoded message is {encrypt_message}')


# 3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amount=shift)
