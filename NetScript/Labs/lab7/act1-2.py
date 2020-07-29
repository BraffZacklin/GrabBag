def DigitCount(n):
	digits = 0
	for _ in list(str(n)):
		digits += 1
	return digits

def Main():
	while True:
		try:
			n = int(input("Please enter an integer: "))
			break
		except ValueError as e:
			print(e)
			continue
	print(DigitCount(n))