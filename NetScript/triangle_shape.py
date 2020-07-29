#!/usr/bin/env python
"""
SYNOPSIS

    python3 triangle_shape.py
    echo "" | python3 triangle_shape.py

DESCRIPTION

    This script takes 3 inputs and sets them to a list named sides
    It checks what sides are different and outputs the right guess

EXAMPLES

    python3 triangle_shape.py
    	Please enter length of side 1: 1
    	Please enter length of side 2: 2
    	Please enter length of side 3: 3

    	Triangle is scalene

AUTHOR

   Shaylan 

VERSION

    1
"""

## Making a list of three inputs for each side
sides = [input("Please enter length of side 1: "), input("Please enter length of side 2: "), input("Please enter length of side 3: ")]
print("")

## Logic for next part
equalateral = False
scalene = False
isoceles = False

## Checking what matches for what type of triangle
if sides[0] == sides[1]:
	if sides[1] == sides[2]:
		equalateral = True
	else:
		isoceles = True
elif sides[1] == sides[2]:
	isoceles = True
else:
	scalene = True

## Outputting the appropriate response
if isoceles == True:
	print("Triangle is isoceles")
if scalene == True:
	print("Triangle is scalene")
if equalateral == True:
	print("Triangle is equalateral")
