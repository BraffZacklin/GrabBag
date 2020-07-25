#!/bin/env python3

from sys import argv

filename = argv[1]

def TabReplace(file):
	replaced_tabs = []
	for lines in file.split('\n'):
		temp_line = ''
		count = 0
		for chars in list(lines):
			if chars == ' ':
				count += 1
			else:
				break
		tabs = int(count / 4)
		for _ in range(0,tabs):
			temp_line += '\t'
		temp_line += lines.strip()
		replaced_tabs.append(temp_line)
	return '\n'.join(replaced_tabs)

with open(filename, 'r') as file:
	file_text = file.read()

file_text = TabReplace(file_text)
print(file_text)

response = None
while True:
	try:
		use_file = list(input(f"\nWould you like to write this to {filename}?\n[Y/N]"))[0].upper()
		if use_file == 'Y':
			response = True
			break
		elif use_file == 'N':
			response = False
			break
		else:
			print("ERROR: Unrecognised Input")
			continue
	except:
		print("ERROR: Unrecognised Input")
		continue

if response == True:
	with open(filename, 'w') as file:
		file.write(file_text)
		print("File updated!")