#!/usr/bin/env python
"""
SYNOPSIS

    Caesar.py
    No command line arguments involved.

DESCRIPTION

    Enter a plaintext message and then the rotation key. The
    plaintext is then converted to cypher text and saved to a file.

EXAMPLES

    User enters 'Hello!' and a key of 13.
    Output should give 'Uryyb!' and write it to a file.

AUTHOR

    Joe Blog <jblogs@TMC.org>

LICENSE

    This script is in the public domain, free from copyrights or
    restrictions.

VERSION

    0.2
"""
## Scenario 2 Code ##

# Caesar cypher function
def rot(input, key):
    # Create an empty string to add to later
    cypher_text = ''
    # Iterate through each character in the message.
    for char in input:
        # Get the ASCII decimal number of char and add the rot key onto it
        cypher_num = ord(char) + key
        # test if it's upper or lowercase, and put the correct input into the wrap_around function
        if char.islower():
        # append the new char to the cypher_text string
            cypher_text += chr(wrap_around(cypher_num, 'lower'))
        elif char.isupper():
            cypher_text += chr(wrap_around(cypher_num, 'upper'))
        # if it's neither uppercase or lowercase, it's not a letter, and shouldn't be rotated: this ensures it is still added to the string
        else:
            cypher_text += char
    # return the string when it's rotated through
    return cypher_text

# Defining another function to check if the ord number for the cypher is in the given case range in ASCII
def wrap_around(cypher_num, case):
    # Sets the lower and upper bounds of the lowercase ASCII range if the case given is lowercase
    if case == 'lower':
        floor = 97
        ceiling = 122
    # Set upper and lower bounds if ASCII range is uppercase
    elif case == 'upper':
        floor = 65
        ceiling = 90
    # Return none if used incorrectly in the program
    else:
        return None
    # if the new ord number is greater than the range's ceiling, it'll lower it by the ceiling, raise it by the floor, and take one (because otherwise it'll be an off by one error)
    if cypher_num > ceiling:
        cypher_num = cypher_num - ceiling + floor - 1
    # return the new ord number in the correct range
    return cypher_num

# Ask the user for their message
plain_input = input('Input the text you want to encode: ')
# Set up a while loop until the key entered is an int between 25 and 0
rot_key = 999
while rot_key > 25 or rot_key < 0:
    try:
        rot_key = int(input('Input the key you want to use from 0 to 25: '))
    except ValueError as e:
        rot_key = 999

# Secret message is the result of the function
secret_message = rot(plain_input, rot_key)
# Print out message for feedback
print('Writing the following cypher text to file:', secret_message)
# Write the message to file
with open('EncryptedText.txt', 'w') as file:
    file.write(secret_message)
