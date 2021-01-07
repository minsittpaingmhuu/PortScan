#!/bin/python3

import socket
import sys
from datetime import datetime as dt
import termcolor

s = socket.socket()

def scan(target,ports):
	print("\n[*] Started at "+str(dt.now()))
	print("[*] Start ports scanning for " + str(target))
	for port in range(1,ports):
		port_scan(target,port)


def port_scan(ipaddress,port):

	try:
		s.connect((ipaddress,port))
		print("[+] Port No ({}) is open .".format(port))
		s.close()
	except:
		pass


	# except KeyboardInterrupt:
	# 	print("\n[*] Exiting the Program.....!")

#Banner
print("\n"+"-" * 50)
print("-" * 50)
print("""   [*] Port Scanner By Rh4P50Dy! [*] """)
print("""       [*] Version ::: 1.0 [*] """)
print("-" * 50)
print("-" * 50+ "\n")

def ask():
	targets =  input("[*] Enter the IP Address/es (split them by , ) : ")
	ports = int(input("[*] How many Ports you want to scan : "))
	if "," in targets:
		# target = targets.split(",")
		print("[*] Scanning multiple targets [*]")
		for target in targets.split(","):
			scan(target.strip(" "),ports)
	else:
		scan(targets,ports)

if len(sys.argv) == 2:
	if sys.argv[1] == "-h" or "--help":
		print(termcolor.colored("Usage >>> Python3 portscan.py <ipaddress> <port>"), 'green')
	else:
		print("Use >>> Python3 portscan.py -h (or) --help for usage.")
elif len(sys.argv) == 3:
		target = sys.argv[1]
		ports = int(sys.argv[2])
		scan(target,ports)

else:
	ask()
