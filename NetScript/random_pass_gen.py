#!/usr/bin/env python
"""
SYNOPSIS

    random_pass_gen.py
    No command line arguments involved.

DESCRIPTION

    Enter a number between 8 and 16, a randomised password
    will be output.

EXAMPLES

    User enters a number of 13.
    Output should give a randomised password, such as 'iuuqfAFWQF&2;'.

AUTHOR

    Joe Blog <jblogs@TMC.org>
	fixed version by Shaylan

LICENSE

    This script is in the public domain, free from copyrights or
    restrictions.

VERSION

    0.4
"""
# Scenario 2 code
# Modules
import random

# Logic
# The character to randomly choose from.
char = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

# Welcome the user to the program.
print("Welcome to the random password generator.\n")

# Set pass_len to 0 to start WHILE loop.
pass_len = 0
# Continually ask user to enter the number until in the right range.
while pass_len < 8 or pass_len > 16:
	## Only allows a change to pass_len if it's an integer
	try:
		pass_len = int(input("Please enter a number between 8 and 16 to generate your password: "))
	except:
		print("ERROR: Input was not an integer")

# Set password to a blank string to later join values to it.
password = ""

# Loop through for as many times in the value of pass_len, adding a
# random character from char each time.
for i in range(pass_len):
	password += password.join(random.choice(char))

# Output final result.
print("Your generated password is:", password)
