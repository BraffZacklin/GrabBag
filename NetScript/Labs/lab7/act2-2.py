def TranslateNumerals(r):
	RomanNumerals = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
	for numerals in RomanNumerals.keys():
		if r.upper() == numerals:
			return RomanNumerals[numerals]

def SolveNumberString(number_list):
	summation = 0
	group = 0

	for pos in range(0,len(number_list)):
		if pos != len(number_list) - 1:
			if number_list[pos] > number_list[pos + 1]:
				if group != 0:
					group += number_list[pos]
					summation += group
				else:
					summation += number_list[pos]
				group = 0

			elif number_list[pos] == number_list[pos + 1]:
				group += number_list[pos]

			elif number_list[pos] < number_list[pos + 1]:
				if group != 0:
					group += number_list[pos]
					summation -= group
				else:
					summation -= number_list[pos]
				group = 0

	return summation

def Main():
	numerals_list = list(input(str("Please input Roman Numerals: ")))
	number_list = []
	for numerals in numerals_list:
		number_list.append(TranslateNumerals(numerals))

	r = SolveNumberString(number_list)

	print(r)
	
Main()