from random import randint
from random import shuffle
from random import choice
import string
from time import sleep
from sys import argv
import os

beta_mode = False

cli = argv[:]
cli_pos_list = list(range(0,len(cli)))
for cli_pos in cli_pos_list:
	if '-b' in cli[cli_pos]:
		beta_mode = True
		beta_function = cli[cli_pos+1]



## The actual programs and a lot of stuff for neatness ##
class Labs():
	def __init__(self):
		self.labs_list = [{
		'lab2': ['Greeting_Program', 'Personalised_Greeting', 'Calculate_Circle', 'Print_Three_Items', 'Sum_Range_1_10', 'Ten_Factorial', 'ASCII_face', 'Print_Lab_2_QnAs']
		},{
		'lab3' : ['Get_Initials', 'Six_Pack_Soda', 'Two_Integers', 'Metres_in_Imperial', 'Print_Filepath', 'Print_Lab_3_QnAs']
		},{
		'lab4' : ['Read_File','Road_Trip','Water_Temp','Read_Int', 'esreveR', 'Vending_Machine', 'Lab4dotTXT', 'String_Analysis', 'Minimum_Value', 'Same_Diff_Neither', 'Print_Lab_4_QnAs']
		},{
		'lab5' : ['Max_Min_List', 'Ten_Number_Shuffle', 'Quicksort', 'Quicksort_With_Alphabet']
		}]

	def what_lab(self):
		print("Enter Q to quit")
		while True:
			lab_num = input("\nWhat Lab # would you like to look at? ")
			if lab_num == 'Q' or lab_num == 'q':
				quit() 

			try:
				lab_pos = int(lab_num) - 1
			except ValueError:
				print("ERROR: Please input only a number\n")
				continue

			if int(lab_num) > len(self.labs_list) or int(lab_num) == 0:
				print("ERROR: Please only input a number within a valid range\n")
				continue

			break


		while True:
			function_num = input("What function would you like to test? ")
			if function_num == 'Q' or function_num == 'q':
				quit() 

			try:
				function_pos = int(function_num) - 1
			except ValueError:
				print("ERROR: Please input only a number\n")
				continue

			function_list = list(self.labs_list[lab_pos].values())[0]
			if int(function_num) > len(function_list) or int(function_num) == 0:
				print("ERROR: Please only input a number within a valid range\n")
				continue

			break

		response = [lab_pos, function_pos]
		return response

##BEGINNING OF LAB2##
	def Greeting_Program(self):
		print("\nParameters: 'When the program is run, output a greeting message to the user'")
		print("Hello, world! You look very beautiful tonight")

	def Personalised_Greeting(self):
		print("\nParameters: 'When the program is run take the name of a user and display a greeting message with their name included.'")
		name = input("What name would you like to be greeted as? ")
		message = "Hello, " + name
		print(message)

	def Calculate_Circle(self):
		print("\nParameters: 'When the program is run take input from the user of a numerical value and use it to calculate the area of a circle.'")
		while True:
			try:
				radius = input("\nWhat is the radius of the circle you would like to calculate? ")
				radius = float(radius)
				break
			except ValueError:
				print("ERROR: Please only enter a number")
		area = 3.14159 * radius * radius
		print("Calculating 3.141 * " + str(radius) + "^2")
		print(area)

	def Print_Three_Items(self):
		print("\nParameters: 'Write a program that prints three items, such as the names of your three best friends or favourite movies, on three separate lines.'")
		str_count = 0
		for random_string in list(range(0,3)):
			str_len = random.randint(3,8)
			random_str = ''
			for items in list(range(0,str_len + 1)):
				random_letter = random.randint(0,25)
				if random_str == '':
					random_str += list(string.ascii_uppercase)[random_letter]
				else:
					random_str += list(string.ascii_lowercase)[random_letter]
				if str_count == 0:
					first_item = random_str + "\n"
				elif str_count == 1:
					second_item = random_str + "\n"
				else:
					third_item = random_str + "\n"
			str_count += 1
		print(first_item + second_item + third_item)

	def Sum_Range_1_10(self):
		print("\nParameters: 'Write a program that prints the sum of the first ten positive integers, 1 + 2 + … + 10.'")
		count = 0
		summation = 0
		while count <= 10:
			summation = summation + count
			if count != 10:
				print(str(count) + " +")
			else:
				print(str(count))
			count += 1
		print("--")
		print(str(summation))
		print("--")

	def Ten_Factorial(self):
		print("\nParameters: 'Write a program that prints the product of the first ten positive integers, 1 × 2 × … × 10.'")
		answer = 1
		answer_string = '1 x '
		for numbers in list(range(2,11)):
			answer = answer * numbers
			if numbers != 10:
				answer_string += str(numbers) + ' x '
			else:
				answer_string += str(numbers) + ' = '
		answer_string += str(answer)
		print(answer_string)

	def ASCII_face(self):
		print("\nParameters: 'Write a program that prints a face similar to the following:")
		face_string = '  '
		for items in list(range(0,5)):
			face_string += "/"
		face_string += '\n +'
		for items in list(range(0,5)):
			face_string += '"'
		face_string += "+\n(| o o |)\n |  ^  |\n | '_' |\n |"
		for items in list(range(0,5)):
			face_string += ' '
		face_string += '|\n +'
		for items in list(range(0,5)):
			face_string += '-'
		face_string += '+'
		print(face_string)
		input("\nDone! Would you like to see it? ")
		input("Are you sure? ")
		input("REALLY SURE? ")
		print("\n" + face_string)
		print("\nIt was so hard not to put ascii goatse here")
		print(" - Ori")

	def Print_Lab_2_QnAs(self):
		print("Press enter to see answer\n")
		input("'1. How do you modify the hello.py program to greet you instead?'")
		print("\tGet user input, point to a file with your name in it, or hardcore your name in\n")
		input("'2. How would you modify the hello.py program to print the word “Hello” vertically?'")
		print("\tBreak into a list, then use a for loop to go through each letter and print it\n")
		input("'3. Would the program continue to work if you replaced line 5 of hello.py with" + '"print(Hello)"' + "?'")
		print("\tNo, it would treat 'Hello' as a variable and not as a string\n")
		input("'4. What does the following statement print?'")
		print("\tIt prints 'My lucky numbers are 17 29'")
		input("'5. What do the following statements print?'")
		print("\tIt prints 'Hello', a blank space, and 'World'")
##END OF LAB2##
##BEGINNING OF LAB3##
	def Get_Initials(self):
		print("\nParameters: 'Write a program which obtains your first name and last name, then prints a pair of initials'")
		first_initial = list(input("What is your first name? "))[0]
		last_initial = list(input("What is your "))[0]
		print(str(first_initial) + str(last_initial))

	def Six_Pack_Soda(self):
		print("\nParameters: 'Write a program which calculates the volume (in liters) of a six-pack of soda if each can is 350ml.'")
		soda_vol = 0.35
		six_sodas = soda_vol * 6
		print(str(six_sodas) + 'L in a six pack of sodas of such a volume')

	def Two_Integers(self):
		print("\nParameters: 'Write a program that prompts the user for two integers and then prints all of the following together:\n\tThe sum\n\tThe difference\n\tThe product\n\tThe average\n\tThe distance\n\tThe maximum'")
		while True:
			integers = input("Enter two integers, separated by a comma: ")
			integers = integers.split(",")
			integers[0] = integers[0].strip()
			integers[1] = integers[1].strip()
			try:
				integers[0] = int(integers[0])
				integers[1] = int(integers[1])
			except ValueError:
				print("The question says 'integers', bro.\n")
				continue
			if len(integers) > 2:
				print("The question says 'two' integers, bro\n")
				continue
			break

		message = '\nTwo numbers = ' + str(integers[0]) + ', ' + str(integers[1])
		message += "\nSum:\t\t" + str(integers[0] + integers[1])
		message += "\nDifference:\t" + str(integers[0] - integers[1])
		message += "\nProduct:\t" + str(integers[1] * integers[0])
		message += "\nAverage:\t" + str((integers[1] + integers[0]) / 2)
		message += "\nDistance:\t" + str(max(integers) - min(integers))
		message += "\nMaximum:\t" + str(max(integers))
		print(message)

	def Metres_in_Imperial(self):
		print("\nParameters: 'Write a program that prompts the user for a measurement in meters and then converts it to miles, feet, and inches.'")
		while True:
			try:
				metres = float(input("Input an amount of metres to get the length in miles, feet, and inches: "))
			except ValueError:
				print("ERROR: Please input a number")
				continue
			break
		inch_ratio = 39.3701
		foot_ratio = 3.28084
		mile_ratio = 0.000621371
		message = "Metres: " + str(metres)
		message += "\n\tin miles:\t" + str(metres * mile_ratio)
		message += "\n\tin feet:\t" + str(metres * foot_ratio)
		message += "\n\tin miles:\t" + str(metres * inch_ratio)
		print(message)

	def Print_Filepath(self):
		print("\nParameters: 'Write a program that prompts for the user drive letter, the path, the filename, and the extension, then prints complete file name.'")
		drive = str(input("Please enter drive letter: "))
		path = str(input("Please enter the filepath: "))
		filename = str(input("Please enter the filename: "))
		fileext = str(input("Please enter the file extension: "))
		filepath = drive + path + filename + fileext
		print("Your filepath is: " + filepath)

	def Print_Lab_3_QnAs(self):
		print("Press enter to see answer\n")
		input("'" + '1. What is problematic about the following statement sequence?\nuserInput = input("Please enter the unit price: ")\nunitPrice = int(userInput)' + "'")
		print("\tThe program will error in the likely event userInput is not an integer\n")
		input("'2. How do you get the first character of a string? The last character? The middle character (if the length is odd)? The middle two characters (if the length is even?)'")
		print("\tTurn it into a list, e.g.")
		print("string = 'foobar'")
		print("list = list(string)")
		print("first_char = list[0]")
		print("last_char = list[-1]")
		print("def Is_Even(num):")
		print("\tremainder = num % 2")
		print("\tif remainder == 0")
		print("\t\treturn True")
		print("\telse:")
		print("\t\treturn False")
		print("mid_char = []")
		print("length = len(list)")
		print("if Odd_Or_Even(length) == True")
		print("\tlower = length / 2")
		print("\tupper = lower + 1")
		print("\tmid_char.append(list[upper])")
		print("\tmid_char.append(list[lower])")
		print("else:")
		print("\tmid_point = length / 2 + 0.5")
		print("\tmid_char.append(list[mid_point])\n")
##END OF LAB3##
##BEGINNING OF LAB4##
	def Read_File(self):
		print("\nParameters: 'Write a program to prompt for a file name, and then read through the file line-by-line'")
		working_dir = os.getcwd()
		print("\nYou are in " + str(working_dir) + "; What file would you like to read?\n")
		print("Press enter to read file line-by-line")
		while True:
			dir_to_read = input()
			try:
				with open(dir_to_read, 'r') as file:
					for lines in file:
						input()
						print(file.readlines())
						break
			except:
				print("\nERROR: Please input a valid file path and name\n")
				continue

	def Road_Trip(self):
		print("\nParameters: 'Write a program which will calculate the cost of petrol based on a road trip in kilometers'\n")
		while True:
			try:
				fuel_efficiency = float(input("Enter fuel efficiency of car in km/L: "))
				break
			except:
				print("ERROR: Input is not a number")
				continue
		
		while True:
			try:
				distance = float(input("Enter distance in km: "))
				break
			except:
				print("ERROR: Input is not a number")
				continue

		while True:
			try:
				fuel_cost = float(input("Enter fuel cost in cents: "))
				break
			except:
				print("ERROR: Input is not a number")
				
		total_cost = (distance/fuel_efficiency) * fuel_cost / 100
		print("TOTAL COST OF ROAD TRIP: ${:.2f}".format(total_cost))

	def Water_Temp(self):
		print("\nParameters: 'Write a program based off the following flow chart:")
		print("1. Read Temp\n2. Temp < 0? --> 2True: Print 'Ice'\n3: Temp > 100? --> 3True: Print 'Steam'\n4. Print 'Liquid'")
		while True:
			try:
				water_temp = float(input("Enter a random celcius value: "))
				break
			except:
				print("ERROR: Input is not a number")
		if water_temp < 0:
			state = 'ice'
		elif water_temp > 100:
			state = 'steam'
		else:
			state = 'liquid'
		print("At the temperature " + str(water_temp) + "C, water would be in the form of " + state)

	def Read_Int(self):
		print("\nParameters: 'Write a program that reads an integer and prints whether it is negative, zero, or positive'")
		while True:
			try:
				checking_int = int(input("Enter a random positive, negative, or zero-value integer: "))
				break
			except:
				print("ERROR: Input is not an integer")
		if checking_int == 0:
			print("Integer is equal to 0")
		elif checking_int < 0: 
			print("Integer is a positive value")
		else:
			print("Integer is a negative value")

	def esreveR(self):
		print("\nParameters: 'Write a program that reads a word and prints the word in reverse.'")
		string_to_reverse = input("Enter a string to reverse: ")
		reversing_list = list(string_to_reverse)
		reversed_string = []
		for characters in range(-1, -1-len(reversing_list), -1):
			reversed_string.append(reversing_list[characters])
		print("Your string reversed is: " + ''.join(reversed_string))

	def Vending_Machine(self):
		print("\nParameters: 'Write a program which simulates a basic vending machine and provides change based on the users monetary input and item price. Your change total must be represented in dollars and cents.'")
		cents = [5, 10, 20, 50]
		dollars = [1, 2, 5, 10, 20, 50, 100]
		values = [0.05, 0.10, 0.20, 0.50, 1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00]
		count = 1
		money_inserted = 0.0
		for items in cents:
			print(str(count) + ") " + str(items) + "c")
			count += 1
		for items in dollars:
			print(str(count) + ") $" + str(items))
			count += 1
		print("\nPress 'E' after inserting money to select your items\n")
		while True:
			try:
				user_in = None
				user_in = input("Insert Money: ")
				if user_in == 'E' or user_in == 'e':
					break
				else:
					pos = int(user_in) - 1
					money_inserted += values[pos]
					print("$" + str(money_inserted) + " inserted total\n")
			except:
				print("ERROR: Please input an integer")
		vending_machine = ['Plain Chips', 'Snickers', 'Mars Bar', 'Bounty Bar', 'Giant Cookie', 'Barbecue Chips', 'Salt and Vinegar Chips', 'Gummy Bears']
		shuffle(vending_machine)
		price_dict = {}
		items_bought = []
		count = 1
		cost = 0
		for snacks in vending_machine:
			iterations = randint(1,5)
			for items in list(range(0,iterations)):
				cost += choice(values)
			price_dict[snacks] = cost
			print(str(count) + ") " + snacks + ": " + str(cost))
			count += 1
		print("\nPress enter after you are done purchasing snacks")
		while money_inserted > 0:
			try:
				user_in = None
				user_in = input("$" + str(money_inserted) + " remaining: ")
				pos = int(user_in) - 1
				money_inserted -= price_dict[vending_machine[pos]]
				if money_inserted < 0:
					print("ERROR: Insufficient Funds, Goodbye")
					break
				else:
					print("You have bought " + vending_machine[pos])
			except:
				if user_in != None:
					print("ERROR: Please input an integer")
				else:
					print("Thank you for shopping!")
					break

	def Lab4dotTXT(self):
		print("\nParameters: 'Create a file called Lab4.txt. First add a new line to the file: " + '"This is Lab 4, Activity 2, Question 3"' + " and finally print the content of Lab4.txt.'")
		with open('Lab4.txt', 'a') as file:
			file.write("This is Lab4, Activity 2, Question 3\n")
		with open('Lab4.txt', 'r') as file:
			print(file.read())

	def String_Analysis(self):
		print("\nParameters: 'Write a program that reads in a string and prints whether it:\n\tContains only letters\n\tContains only uppercase letters\n\tContains only lowercase letters\n\tContains only digits\n\tContains only letters and digits\n\tStarts with an uppercase letter\n\tEnds with a period")
		string_analysis = input("Enter a string to receive information on it: ")
		
		contains_letters = False
		contains_uppercase = False
		contains_lowercase = False
		contains_digits = False
		starts_upper = False
		ends_period = False

		string_analysis = list(string_analysis)
		for items in string_analysis:
			if items.isdigit():
				contains_digits = True
			elif items.isupper():
				contains_letters = True
				contains_uppercase = True
			elif items.islower():
				contains_letters = True
				contains_lowercase = True

		if string_analysis[0].isupper():
			starts_upper = True
		if string_analysis[-1] == '.':
			ends_period = True

		if contains_letters == True:
			if contains_digits == True:
				print("Your string contains only letters and digits")
			else:
				print("Your string contains only letters")
				if contains_uppercase == True:
					if contains_lowercase == False:
						print("Your string contains only uppercase letters")
				else:
					if contains_lowercase == True:
						print("Your string contains only lowercase letters")
		else:
			print("Your string contains only digits")
		if starts_upper == True:
			print("Your string starts with an uppercase")
		if ends_period == True:
			print("Your string ends with a period")

	def Minimum_Value(self):
		print("\nParameters: 'Translate the following pseudocode for finding the minimum value from a set of inputs into a Python program'")
		minimum = 0
		first = True
		while True:
			num_value = float(input("Enter a number: "))
			if first == True:
				minimum = num_value
				first == False
			elif num_value < minimum:
				minimum = num_value
			else:
				break
		print("The lowest number entered was " + str(minimum))

	def Same_Diff_Neither(self):
		print("\nParameters: 'Write a program that reads three numbers and prints “all the same” if they are all the same, “all different” if they are all different, and “neither” otherwise.'")
		nums_picked = False
		num_list = []
		count = 1
		while nums_picked == False:
			try:
				num = float(input("Enter number " + str(count) + "/3: "))
				num_list.append(num)
				count += 1
				if count == 4:
					nums_picked = True
			except:
				print("ERROR: Input must be a number")
		all_same = True
		all_different = False

		if num_list[0] != num_list[1]:
			all_same = False
			if num_list[0] != num_list[2]:
				all_different = True
		else:
			if num_list[0] != num_list[2]:
				all_same = False

		if all_same == True:
			print("Numbers are all the same")
		elif all_different == True:
			print("Numbers are all different")
		else:
			print("Numbers are neither all the same or all different")

	def Print_Lab_4_QnAs(self):
		print("Press enter to see answer\n")
		input("1. What are nested loops? Give an example of where a nested loop is typically used")
		print("\tNested loops are when there is a loop within a loop; used for arrays\n")
		input("2. How do you generate random values")
		print("\tThe random module\n")
		input("3. What do these loops print?")
		print("\tA) prints 1-9 on newline, B) prints 1, 3, 5, 7, 9 all on newlines, C) Prints 10 descending down to 2 on newlines, D) Prints 1-9 on newlines, E) prints even numbers from 1-10 on newlines\n")
		input("4. Explain difference between an if/elif/else sequence and nested if statements")
		print("\tif/elif/else will only execute a maximum of one instruction from three, nested if statements will execute one statement per layer\n")
		input("5. If you are asking a user to input a number, how would you structure this and why?")
		print("\tI would set up a while loop that only breaks if they input ONLY a number, so the program can assume they always entered a number\n")
		input("6. Provide a description of the following file modes in python: r, w, x, a, t, b, +")
		print("\tr == read, w == write, x == exclusive, only do file operation if this file, a == append, t == text mode, b = binary mode, + = extension\n")

## DAS WO BEGINNEN LAB5
	def Min_Max_List(self):
		print("\nParameters: Write Python code for a loop that simultaneously computes both the max and min of a list, during each loop ask the user to enter a new number")
		print("Enter Q to quit")
		num_list = []
		while True:
			new_number = input("Please enter a number: ")
			if new_number == 'Q' or new_number == 'q':
				break
			else:
				try:
					new_number = float(new_number)
				except:
					print("ERROR: Please enter a number")
			if len(num_list) == 0:
				num_list.append(new_number)
				print(str(num_list[0]) + " is the min and max value entered")
			elif new_number > num_list[-1]:
				num_list.append(new_number)
				print(str(num_list[0] + " is the minimum\n" + str(num_list[-1] + " is the maximum")))

	def Ten_Number_Shuffle(self):
		print("\nParameters: Write a loop that reads 10 numbers and a second loop that displays them in the opposite order from which they were entered")
		num_list = []
		numbers_input = 1
		while numbers_input < 11:
			try:
				new_number = float(input("Please enter number " + str(numbers_input) + "/10: "))
				numbers_input += 1
				num_list.append(new_number)
			except:
				print("ERROR: Please enter a number")
		reverse_list = num_list[:]
		reverse_list.reverse()
		print("Your input: ")
		for items in num_list:
			print("\t" + str(items))
		print("\nYour input reversed: ")
		for items in reverse_list:
			print("\t" + str(items))

	def Quicksort_Body(self):
		example_list = ['foo', 'bar', '1', '2', 'five', 'sixtynine', 'a', 'ca', 'hcde', 'afb', 'aaa', 'aba', 'aac', 'bac']
		user_list = []
		print("Example List: " + str(example_list))
		while True:
			build = input("\nWould you like to make your own list [Y], or use the example list above [N]? ")
			if list(build)[0].upper() == 'Y':
				build = True
				break
			elif list(build)[0].upper() == 'N':
				build = False
				break
			else:
				print("ERROR: Unrecognised Input")

		count = 1
		if build == True:
			print("Enter QQ to stop")
			while True:
				user_element = input("Enter element " + str(count) + ": ")
				if user_element != 'QQ':
					user_list.append(user_element)
					count += 1
				else:
					break
		if build == True:
			return user_list[:]
		else:
			return example_list[:]

	def Quicksort_Impl(self, list_to_sort, lex=False):
		## python implementation of quicksort stolen from stackoverflow; I couldn't understand the recursion 'till I saw this
		## extended to use .sort() if asked and that's it
		less = []
		equal = []
		greater = []

		if len(list_to_sort) > 1:
			pivot = list_to_sort[0]
			for items in list_to_sort:
				if len(items) < len(pivot):
					less.append(items)
				elif len(items) == len(pivot):
					equal.append(items)
				else:
					greater.append(items)
			if lex == True:
				equal.sort()
			return self.Quicksort_Impl(less) + equal + self.Quicksort_Impl(greater)
		else:
			return list_to_sort

	def Quicksort(self):
		print("\nParameters: Write Python code which sorts a list of strings by increasing length")
		sorted_list = self.Quicksort_Impl(self.Quicksort_Body())
		print("Sorted List: " + str(sorted_list))
		
	def Quicksort_With_Alphabet(self):
		print("\nParameters: Write Python code which sorts a list of strings by increasing length, or by alphabetical order if two strings are of the same length")
		sorted_list = self.Quicksort_Impl(self.Quicksort_Body(), lex=True)
		print("Sorted List: " + str(sorted_list))


## This is the greeting stuff ##
program = Labs()
first_run = True

if beta_mode != True:
	if first_run != True:
		time.sleep(3)
	while True:
		print("")
		num_count = 1
		for labs_dict in program.labs_list:
			lab_name = list(labs_dict.keys())[0]
			func_list = list(labs_dict.values())[0]
			func_count = 1

			num_str = str(num_count)
			lab_line = num_str + ") " + lab_name + ":"
			print(lab_line)

			for functions in func_list:
				func_str = str(func_count)
				func_line = "\t" + func_str + ") " + functions
				print(func_line)
				func_count += 1

			num_count += 1
	
		response = program.what_lab()
		lab_pos = response[0]
		func_pos = response[1]
		lab_dict = program.labs_list[lab_pos]
		func_list = list(lab_dict.values())[0]
		func_name = func_list[func_pos]

		exec("program." + func_name + "()")
		first_run = False
else:
	exec("program." + beta_function + "()")