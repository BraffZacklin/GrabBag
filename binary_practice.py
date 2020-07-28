from random import randint

message = "Welcome to a binary practice study tool\n"
message += "You'll be given random numbers in the range of 0-255 to convert\t"
message += "You'll be asked to convert them to hex, decimal, or binary from any other form\n"
message += "(Enter 'Q' to quit)"
print(message)

def random_numbers():
	numbers = []
	decimal = randint(0,255)
	binary = bin(decimal)
	hexadecimal = hex(decimal)

	binary = list(binary)[2:]
	hexadecimal = list(hexadecimal)[2:]

	while len(binary) < 8:
		binary.insert(0, '0')
	while len(hexadecimal) < 2:
		hexadecimal.insert(0, '0')

	binary = ''.join(binary)
	hexadecimal = ''.join(hexadecimal)
	decimal = str(decimal)

	numbers.append(binary)
	numbers.append(hexadecimal)
	numbers.append(decimal)

	return numbers

def question_flags():
	conversion = []

	convert_from = randint(0,1)
	if convert_from == 0:
		conversion.append('binary')
		convert_to = randint(0,1)
		if convert_to == 0:
			conversion.append('decimal')
		else:
			conversion.append('hexadecimal')
	else:
		convert = randint(0,1)
		if convert == 0:
			conversion.append('decimal')
			conversion.append('binary')
		else:
			conversion.append('hexadecimal')
			conversion.append('binary')

	return conversion

def question(given, conversion, given_type, conversion_type):
	tries = 3
	while True:
		answer = input("What is the " + given_type + " value " + given + " in " + conversion_type + "?\n" )
		if answer == conversion:
			print("Correct!")
			return True
		elif tries != 0:
			print(str(tries) + " attempts left\n")
			tries -= 1
			continue
		elif tries == 0:
			print("Incorrect, the answer is " + str(conversion))
			return False
		else:
		 	quit()

score = 0	
while True:
	print("\nCurrent Score: " + str(score) + "\n")

	rand_numbers = random_numbers()
	binary = rand_numbers[0]
	hexadecimal = rand_numbers[1]
	decimal = rand_numbers[2]

	q_flags = question_flags()
	exec("answer = question(" + q_flags[0] + ", " + q_flags[1] + ", str(q_flags[0]), str(q_flags[1]))")	

	if answer == True:
		score += 1