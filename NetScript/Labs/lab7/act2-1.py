from random import randint

def FirstDigit(n):
	return list(str(n))[0]

def LastDigit(n):
	return list(str(n))[-1]

def Digits(n):
	return len(list(str(n)))

def EnterNum(message):
	while True:
		try:
			n = int(input(message))
			break
		except ValueError as e:
			print(e)
			continue
	return n

def Main():
	floor = EnterNum("Please enter the lowest digit to test: ")
	cap = EnterNum("Please enter to highest digit to test: ")
	print("Testing 3 random numbers")
	for _ in range(0,3):
		n = randint(floor, cap)
		print(f"\nTesting {n}")
		print(f"\tFirstDigit = {FirstDigit(n)}")
		print(f"\tLastDigit = {LastDigit(n)}")
		print(f"\tDigits = {Digits(n)}")

Main()