#!/usr/bin/env python
## Comment this out or change it for your own linux distro
import sys
sys.path.append('/home/wyvern/.local/lib/python3.7/site-packages')

##Logic
from scapy.all import *

header = "Port_scanner.py"
header += "\n"
header += "\tPort_scanner.py [-h,help] [-v,verbose] [-a,address | -l,list] [-t,timeout] [-r,retry]"
header += "\n"
header += "DESCRIPTION"
header += "\n"
header += "\tWhen run with the arguments address and a domain, \n\tor list and a file containing a list of domains,\n\twill scan common ports for their status and output results"
header += "\n"
header += "EXAMPLES"
header += "\n"
header += "\tPort_scanner.py -h\n\tPort_scanner.py -a 192.168.1.0\n\tPort_scanner.py verbose -a 10.0.0.0/30 -t 3 -r 2\n\tPort_scanner.py -a -v www.google.com\n\tPort_scanner.py -l remote_hosts.txt"
header += "\n"
header += "AUTHOR"
header += "\n"
header += "\tShay <p460471@tafe.wa.edu.au>"
header += "\n"
header += "LICENSE"
header += "\n"
header += "\tThis script is the exclusive and proprietary property of\n"
header += "\tTiO2 Minerals Consultants Pty Ltd. It is only for use and\n"
header += "\tdistribution within the stated organisation and its\n"
header += "\tundertakings.\n"
header += "\n"
header += "VERSION"
header += "\n"
header += "\t1.0"

timeout = 1.5
retry = 1
verbose_flag = False
list_file = None
address_list = []
dports_list = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 1434, 8080]

## Reading CLI, if there are no args, print help
CLI = sys.argv[:]
if len(CLI) == 1:
	print(header)
	quit()

## Reading CLI, finding arguments and passing them to script functionality
for x in range(1,len(CLI)):
	if CLI[x] in ['-h', 'help']:
		print(header)
		quit()
	elif CLI[x] in ['-v', 'verbose']:
		verbose_flag = True
	elif CLI[x] in ['-a', 'address']:
		if '/' in CLI[x + 1]:
			address_list += Net(CLI[x + 1])
		else:
			address_list.append(CLI[x + 1])
	elif CLI[x] in ['-l', 'list']:
		list_file = CLI[x + 1]
## If these two are set incorrectly, the user won't want to use the script and the script won't run, so we make sure they're correct for it to run
	elif CLI[x] in ['-t', 'timeout']:
		try:
			timeout = float(CLI[x + 1])
		except ValueError as e:
			print(e)
			quit()
	elif CLI[x] in ['-r', 'retry']:
		try:
			retry = int(CLI[x + 1])
		except ValueError as e:
			print(e)
			quit()

## If verbose is true, then this function outputs status updates when used; otherwise it does nothing when used
if verbose_flag == True:
	def verbose_output(status, message):
		if status == 0:
			output = '[ ] '
		elif status == 1:
			output = '[*] '
		output += message
		print(output)
else:
	def verbose_output(status, message):
		None

## Defining our scan function
def port_scan(packet, host_port, timeout, retry):
	verbose_output(1, f'Sending TCP packet to {host_port}')
	response = sr1(packet, timeout=timeout, retry=retry, verbose=0)
	if response == None:
		verbose_output(1, f'Received no response from {host_port}')
		return 'Filtered'
	else:
		response = response.getlayer(TCP)
		if 'SA' in str(response.flags):
			verbose_output(1, f'Received SYN/ACK response from {host_port}')
			return 'Open'
		elif 'R' in str(response.flags):
			verbose_output(1, f'Received RST or RST/ACK from {host_port}')
			return 'Closed'

## Checks if list file is in current directory or if list file is a directory
if list_file != None:
	verbose_output(0, f'Opening list file {list_file}')
	if list_file in os.listdir(os.getcwd()):
		list_file = os.getcwd() + '/' + list_file
	try:
		with open(list_file, 'r') as file:
			address_list += file.readlines()
		verbose_output(1, f'{list_file} successfully opened and read')
	except Exception as e:
		quit(e)
## This part strips all items, and if it's a CIDR notated range, will use Net() to convert it to a list and add onto our working one
	else:
		temp_list = []
		for items in address_list:
			if '/' in items.strip():
				temp_list += Net(items.strip())
			else:
				temp_list.append(items.strip())
		address_list = temp_list[:]
		del temp_list

## This performs the scan by constructing a packet and using 'port_scan(packet)' to check status of ports and add it to dictionary
verbose_output(0, 'Initiating scanning on all hosts and ports')
responses_dict = {'Open':[], 'Filtered':[],'Closed':[]}
for remote_host in address_list:
	for port in dports_list:
		host_port = remote_host + ':' + str(port)
		source = RandShort()
		packet = IP(dst=remote_host)/TCP(sport=source, dport=port)
		responses_dict[port_scan(packet, host_port, timeout, retry)].append(host_port) 

verbose_output(1, 'Finished scanning all hosts and ports')

## This sorts and then prints responses
print("Results: ")
print("\tOpen Ports: ")
for items in responses_dict['Open']:
	print("\t\t" + items)
print("\n\tFiltered Ports: ")
for items in responses_dict['Filtered']:
	print("\t\t" + items)
print("\n\tClosed Ports: ")
for items in responses_dict['Closed']:
	print("\t\t" + items)