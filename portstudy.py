import random
import time

##SETTING UP THE PORTS CLASS##
class port():
	def __init__(self, number, datagram, protocols, special_answer=None, bonus_q=None):
		self.number = number
		self.datagram = datagram
		self.protocols = protocols
		self.bonus_q = bonus_q
		self.special_answer = special_answer
		##THIS IS FOR BONUS QUESTIONS SPECIFIC TO THE PORT##
		dynamic_bonus_subject = ['7', '20']
		if bonus_q != None:
			if self.number in dynamic_bonus_subject:
				self.bonus_q_subject = exec(bonus_q[0])
			else:
				self.bonus_q_subject = bonus_q[0]
			self.bonus_q_subject = bonus_q[0]
			self.bonus_q_answer = bonus_q[1]
			self.bonus_q_question = bonus_q[2]
			self.bonus_q_fail_msg = bonus_q[3]
			self.bonus_q_type_flag = bonus_q[4]

	def get_rand_portorprotocol(self):
		coin_flip = random.randint(0,1)
		if coin_flip == 1:
			return self.number
		else:
			rand_protocol = random.choice(self.protocols)
			return rand_protocol
	def strip_response_to_numbers(self, response):
		numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
		stripped_res = []
		for items in response:
			if items in numbers:
				stripped_res.append(items)
		return ''.join(stripped_res)
	def make_all_letters_lower(self, protocol):
		blank_list = []
		protocol_list = list(protocol)
		for character in protocol_list:
			stripped_char = character.strip()
			if stripped_char.isupper() == True:
				patchedchar = stripped_char.lower()
			else:
				patchedchar = stripped_char
			blank_list.append(patchedchar)
		fixedprotocol = ''.join(blank_list)
		return fixedprotocol

	def question(self, subject, answer, question, fail_msg, q_type_flag):
		tries = 0
		while tries < 4:
			response = input(question)
			if q_type_flag == 'port_q':
				response = list(response)
				response = self.strip_response_to_numbers(response)
			elif q_type_flag == 'protocol_q':
				temp_list = []
				response = self.make_all_letters_lower(response)
				for items in answer:
					loweritem = self.make_all_letters_lower(items)
					temp_list.append(loweritem)
				if response in temp_list:
					response = answer
				else:
					response = None
			elif q_type_flag == 'datagram_q':
				tries += 1
			if response == answer:
				print("Correct!")
				if self.bonus_q != None:
					coin_flip = random.randint(0,2)
					if coin_flip == 1:
						print("\nBonus Question:", end=None)
						self.bonus_question()
				return "correct"
			elif response != answer:
				tries += 1
				attempts_left = 3 - tries
				if attempts_left > 0:
					print("\nIncorrect, you have " + str(attempts_left) + " attempts left")
				else:
					print(fail_msg)
					return "incorrect"

	def what_port(self):
		subject = random.choice(self.protocols)
		if self.special_answer == None:
			answer = self.number
		else:
			answer = self.special_answer
		question = "\nWhat port does protocol " + subject + " operate on?\n"
		fail_msg = "Incorrect, protocol " + subject + " operates on port " + answer
		q_type_flag = 'port_q'
		passorfail = self.question(subject, answer, question, fail_msg, q_type_flag)
		return passorfail

	def what_protocol(self):
		rand_protocol_name = random.choice(self.protocols)

		subject = self.number
		answer = self.protocols
		question = "\nWhat protocol operates on port " + subject + "?\n"
		fail_msg = "Incorrect, port " + subject + " operates the protocol " + rand_protocol_name
		q_type_flag = 'protocol_q'
		passorfail = self.question(subject, answer, question, fail_msg, q_type_flag)
		return passorfail

	def tcp_or_udp(self):
		subject = self.get_rand_portorprotocol()
		answer = self.datagram
		if subject == self.number:
			question = "\nWhat datagram type does port " + subject + " use?\n[UDP/TCP/Both/Neither] "
			fail_msg_part_1 = "Incorrect, port " + subject
		else:
			question = "\nWhat datagram type does protocol " + subject + " use?\n[UDP/TCP/Both/Neither] "
			fail_msg_part_1 = "Incorrect, protocol " + subject
		if answer == 'Both':
			fail_msg_part_2 = " uses both datagram types"
		elif answer == 'Neither':
			fail_msg_part_2 = " uses neither datagram type"
		else:
			fail_msg_part_2 = " uses datagram type " + answer
		fail_msg = fail_msg_part_1 + fail_msg_part_2
		q_type_flag = 'datagram_q'
		passorfail = self.question(subject, answer, question, fail_msg, q_type_flag)
		return passorfail

	def bonus_question(self):
		subject = self.bonus_q_subject
		answer = self.bonus_q_answer
		question = self.bonus_q_question
		fail_msg = self.bonus_q_fail_msg
		q_type_flag = self.bonus_q_type_flag
		passorfail = self.question(subject, answer, question, fail_msg, q_type_flag)
		return passorfail

##INFO ON ALL 30 PORTS MENTIONED##
bonus_q_subject = 'self.get_rand_portorprotocol()'
bonus_q_answer = ['ICMP', 'Internet Control Message Protocol']
bonus_q_question = 'What protocol does ping (Packet Internet Groper) use instead of TCP or UDP?\n'
bonus_q_fail_msg = 'Incorrect, ping uses the Internet Control Message Protocol (ICMP) instead of TCP or UDP'
bonus_q_type_flag = 'protocol_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]

port7 = port('7', 'Neither', ['Echo Reply', 'Ping', 'Packet Internet Groper'], bonus_q=bonus_q)

bonus_q_subject = 'random.choice(self.protocols)'
bonus_q_answer = '20'
bonus_q_question = 'FTP uses two ports: 20 and 21, Passive FTP will use a dynamic port\nWhich port would be used for active file transfer?\n(The other is used as a control port): '
bonus_q_fail_msg = 'Incorrect, FTP uses port 20 for active file transfers, and 21 as the control port'
bonus_q_type_flag = 'port_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port20 = port('20', 'TCP', ['FTP', 'File Transfer Protocol'], special_answer='2021', bonus_q=bonus_q)
port21 = port('21', 'TCP', ['FTP', 'File Transfer Protocol'], special_answer='2021', bonus_q=bonus_q)

bonus_q_answer = '26'
bonus_q_subject = '25'
bonus_q_question = 'What other port does SMTP use?\n'
bonus_q_fail_msg = 'Incorrect, SMTP uses ports 26 & 25'
bonus_q_type_flag = 'port_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port25 = port('25', 'TCP', ['SMTP', 'Simple Mail Transfer Protocol'], bonus_q=bonus_q)

bonus_q_answer = '25'
bonus_q_subject = '26'
bonus_q_question = 'What other port does SMTP use?\n'
bonus_q_fail_msg = 'Incorrect, SMTP uses ports 26 & 25'
bonus_q_type_flag = 'port_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port26 = port('26', 'TCP', ['SMTP', 'Simple Mail Transfer Protocol'], bonus_q=bonus_q)

if random.randint(0,1) == 1:
	tcp_or_udp = 'TCP'
	bonus_q_answer = 'Zone Transfer'
else:
	tcp_or_udp = 'UDP'
	bonus_q_answer = 'Name Queries'
bonus_q_subject = None
bonus_q_type_flag =  'protocol_q'
##This isn't a protocol question, but it can be read like on into the program
bonus_q_question = 'DNS uses both TCP and UDP for different purposes; what does it use ' + tcp_or_udp + ' for?\n[Zone Transfer or Name Queries?]: ' 
bonus_q_fail_msg = 'Incorrect, DNS uses ' + tcp_or_udp + ' for ' + bonus_q_answer
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port53 = port('53', 'Both', ['Domain Name System', 'DNS'], bonus_q=bonus_q)

bonus_q_subject = '67'
bonus_q_answer = '68'
bonus_q_question = 'Port ' + bonus_q_subject + ' hosts the Bootstrap Protocol\nWhat other (non-dynamic) port does this protocol use?\n'
bonus_q_fail_msg = 'Incorrect, BOOTP is hosted on ports ' + bonus_q_subject + ' and ' + bonus_q_answer
bonus_q_type_flag = 'port_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port67 = port('67', 'UDP', ['BOOTP', 'Bootstrap Protocol', 'DHCP', 'Dynamic Host Configuration Protocol'], bonus_q=bonus_q)

bonus_q_subject = '68'
bonus_q_answer = '67'
bonus_q_question = 'Port ' + bonus_q_subject + ' hosts the Bootstrap Protocol\nWhat other (non-dynamic) port does this protocol use?\n'
bonus_q_fail_msg = 'Incorrect, BOOTP is hosted on ports ' + bonus_q_subject + ' and ' + bonus_q_answer
bonus_q_type_flag = 'port_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port68 = port('68', 'UDP', ['BOOTP', 'Bootstrap Protocol', 'DHCP', 'Dynamic Host Configuration Protocol'], bonus_q=bonus_q)

bonus_q_subject = 'NetBIOS'
bonus_q_answer = '135-139'
bonus_q_question = 'What port range does NetBIOS (not NetBIOS over TLS) use?\n[aaa-bbb]: '
bonus_q_fail_msg = 'Incorrect, NetBIOS operates on ports 135-139'
bonus_q_type_flag = 'port_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port135 = port('135', 'UDP', ['NetBIOS', 'Net Basic Input Output System'], special_answer='135139', bonus_q=bonus_q)
port136 = port('136', 'UDP', ['NetBIOS', 'Net Basic Input Output System'], special_answer='135139', bonus_q=bonus_q)
port137 = port('137', 'UDP', ['NetBIOS', 'Net Basic Input Output System'], special_answer='135139', bonus_q=bonus_q)
port138 = port('138', 'UDP', ['NetBIOS', 'Net Basic Input Output System'], special_answer='135139', bonus_q=bonus_q)
port139 = port('139', 'UDP', ['NetBIOS', 'Net Basic Input Output System'], special_answer='135139', bonus_q=bonus_q)

bonus_q_subject = None
bonus_q_answer = '162'
bonus_q_question = 'What other port does Simple Network Management Protocol (SNMP) operate on?\n'
bonus_q_fail_msg = 'Incorrect, SNMP also uses port 162'
bonus_q_type_flag = 'port_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port161 = port('161', 'Both', ['SNMP', 'Simple Network Management Protocol'], bonus_q=bonus_q)

bonus_q_subject = None
bonus_q_answer = '161'
bonus_q_question = 'What other port does Simple Network Management Protocol (SNMP) operate on?\n'
bonus_q_fail_msg = 'Incorrect, SNMP also uses port 161'
bonus_q_type_flag = 'port_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port162 = port('162',  'Both', ['SNMP', 'Simple Network Management Protocol'], bonus_q=bonus_q)

bonus_q_subject = None
bonus_q_answer = 'UDP'
bonus_q_question = 'What datagram type does Microsoft use with LDAP?\n(Most other systems use the other datagram) '
bonus_q_fail_msg = 'Incorrect, Microsoft uses the User Datagram Protocol (UDP) type'
bonus_q_type_flag = 'datagram_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port389 = port('389', 'Both', ['LDAP', 'Lightweight Directory Access Protocol'], bonus_q=bonus_q)
port636 = port('636', 'Both', ['Secure LDAP', 'Secure Lightweight Directory Access Protocol', 'LDAP', 'Lightweight Directory Access Protocol'], bonus_q=bonus_q)

bonus_q_subject = None
bonus_q_answer = 'TCP'
bonus_q_question = 'RADIUS used to use the other datagram type, but what datagram type does DIAMETER use?\n[UDP/TCP/Both/Neither] '
bonus_q_fail_msg = 'Incorrect, DIAMETER uses the Transmission Control Protocol datagram type'
bonus_q_type_flag = 'datagram_q'
bonus_q = [bonus_q_subject, bonus_q_answer, bonus_q_question, bonus_q_fail_msg, bonus_q_type_flag]
port1812 = port('1812', 'Both', ['RADIUS', 'Remote Access Dial In User Services', 'DIAMETER'], bonus_q=bonus_q)

port22 = port('22', 'TCP', ['SSH', 'Secure Shell'])
port23 = port('23', 'UDP', ['TELNET', 'TeleType Network'])
port49 = port('49', 'TCP', ['TACACS', 'TACACS+', 'Terminal Access Controller Access Control System', 'Terminal Access Controller Access Control System Plus'])
port69 = port('69', 'UDP', ['TFTP', 'Trivial File Transfer Protocol'])
port80 = port('80', 'TCP', ['HTTP', 'Hypertext Transfer Protocol'])
port88 = port('88', 'Both', ['Kerberos'])
port145 = port('145', 'TCP', ['NetBIOS', 'Net Basic Input Output System', 'NetBIOS over TLS', 'Net Basic Input Output System over TLS', 'NetBIOS over SSL', 'Net Basic Input Output System over SSL'])
port443 = port('443', 'TCP', ['HTTPS', 'Hypertext Transfer Protocol Secure'])
port500 = port('500', 'UDP', ['ISAKMP', 'Internet Security Association Key Management Protocol'])
port1433 = port('1433', 'TCP', ['Transact SQL', 'Transact Structured Query Langauge', 'T-SQL'])
port1521 = port('1521', 'TCP', ['Oracle SQL', 'SQLpl', 'SQL Programming Language'])
port1701 = port('1701', 'UDP', ['L2TP', 'Layer 2 Tunneling Protocol', 'Layer Two Tunneling Protocol'])
port1723 = port('1723', 'TCP', ['MS PPTP', 'Microsoft Point to Point Tunneling Protocol', 'Point to Point Tunneling Protocol'])
port143 = port('143', 'TCP', ['IMAP', 'Internet Messaging Application Protocol'])
port110 = port('110', 'TCP', ['POP', 'Post Office Protocol'])
port119 = port('119', 'TCP', ['NNTP', 'RSS', 'Network News Transfer Protocol', 'Real Simple Syndication'])
port123 = port('123', 'UDP', ['NTP', 'Network Time Protocol'])
port3389 = port('3389', 'Both', ['RDP', 'Remote Desktop Protocol', 'WBT', 'Windows Based Terminal'])

portslist = [
'port7', 
'port20', 
'port21', 
'port22', 
'port23', 
'port25', 
'port26', 
'port49', 
'port53', 
'port67', 
'port68', 
'port69', 
'port80', 
'port88', 
'port110', 
'port119', 
'port123', 
'port135', 
'port136', 
'port137', 
'port138', 
'port139', 
'port143', 
'port145', 
'port161', 
'port162', 
'port389', 
'port443', 
'port500', 
'port636', 
'port1433', 
'port1521', 
'port1701', 
'port1723', 
'port1812', 
'port3389', 
]

print("  #####################################################  ")
print("##                                                     ##")
print("## Welcome!                                            ##")
print("## This is a study tool made by Braff Zacklin          ##")
print("## Feel free to distribute or edit this                ##")
print("## If you need a cheat sheet, look inside the program  ##")
print("## Enjoy!                                              ##")
print("## (Please Note: Protocols that take up multiple ports ##")
print("##   should be answered as a range from the lowest to  ##")
print("##     from the lowest port to the highest port,       ##")
print("##     e.g. NetBIOS is from 135-139)                   ##")
print("##                                                     ##")
print("  #####################################################  ")
print("\n")
print("How many questions would you like to be asked this session")
print("(Bearing in mind there are only 30 different ports on this list)")
while True:
	how_many = input("")
	if how_many.isdigit():
		how_many = int(how_many)
		if how_many < 31:
			print("You have chosen 30 or less questions")
			print("You will not be asked about the same port more than once")
			repeat = False
			break
		if how_many < 61:
			print("You have chosen 60 or less questions")
			print("You may be asked the same question multiple times")
			repeat = True
			break
		else:
			print("There's a cap of 60 for your own safety, friendo")
	else:
		print("Please enter your response only in digits")

while True:
	ask_datagrams = input("\nWould you like to be asked questions about datagram types?\n[Y/N] ")
	if list(ask_datagrams.title())[0] == 'Y':
		datagram_questions = True
		break
	elif list(ask_datagrams.title())[0] == 'N':
		datagram_questions = False
		break
	else:
		print("Please enter only a yes or a no")

correct = []
incorrect = []

questions_asked = 0
while questions_asked < how_many:
	questions_asked += 1
	rand_port = random.choice(portslist)

	if repeat == False:
		portslist.remove(rand_port)
	if datagram_questions == True:
		question_range = 2
	else:
		question_range = 1

	rand_num = random.randint(0,question_range)
	if rand_num == 0:
		exec("question = " + rand_port + ".what_port()")
	elif rand_num == 1:
		exec("question = " + rand_port + ".what_protocol()")
	else:
		exec("question = " + rand_port + ".tcp_or_udp()")

	if question == "correct":
		exec("port_num = " + rand_port + ".number")
		correct_string = "Port " + port_num
		correct.append(correct_string)
	else:
		exec("port_num = " + rand_port + ".number")
		port_info = "Port "
		port_info += port_num
		port_info += "\n"

		exec("protocols_list = " + rand_port + ".protocols")
		protocols_list = ', '.join(protocols_list)
		protocol_info = "Operates Protocol(s): "
		protocol_info += protocols_list
		protocol_info += "\n"

		exec("datagram_type = " + rand_port + ".datagram")
		datagram_info = "Uses TCP or UDP: "
		datagram_info += datagram_type
		datagram_info += "\n"
		incorrect_msg = port_info + protocol_info + datagram_info
		if incorrect_msg not in incorrect[:]:
			incorrect.append(incorrect_msg)

print("\nYou got " + str(len(correct)) + " answers correct")
if len(incorrect) != 0:
	while True:
		see_summary = input("You got " + str(len(incorrect)) + " questions wrong\nWould you like to view a summary of the information of each port incorrectly answered?\n[Y/N] ")
		if list(see_summary.title())[0] == 'Y':
			print("")
			for items in incorrect:
				print(items)
			quit()
		elif list(see_summar.title())[0] == 'N':
			print("Very well!\nGoodbye!")
			quit()
		else:
			print("Sorry, please only answer with either yes or no")