def find(string, match):
	string_list = list(string)

	for index in range(0,len(string_list)):
		temp_list = []

		for pos in range(index,index+len(match)):
			temp_list.append(string_list[pos])

		if match == ''.join(temp_list):
			return True
	return False

def Main():
	b = find(input("What string would you like to search? "), input("What string would you like to search for inside? "))
	print(b)

Main()