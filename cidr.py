#!/bin/env python3

"""
Author : GordonWei
Date : 04/16/21
Comment : input CIDR, this python will output ip range
"""

import ipaddress

choice = input('''
Which output does you want to show?
1. Only show cidr start and end.
2. Show all cidr ip-address. 
''')
cidr = input('Enter CIDR include slash num : ')
net = ipaddress.ip_network(cidr)
if choice == '1' :
	print('Your CIDR is ' + cidr)
	print('CIDR Start From : ' + str(net[0]))
	print('CIDR End To : ' + str(net[-1]))
elif choice == '2':
	for i in net:
		print(i)
else:
	None 
