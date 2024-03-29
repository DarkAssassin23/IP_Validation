#!python3
######################################################################
#                                                                    #
# This script prompts the user for an ip address and for a network   #
# and validates if the ip address is in the network and lets the     #
# user know if the address and network are valid when inputed        #
#                                                                    #  
# Author: Will Jones                                                 #
#                                                                    #
######################################################################

import ipaddress, os

os.system('cls' if os.name == 'nt' else 'clear')

#tests if the ip given is in the given network
#if so it returns true otherwise it returns false
def testAddress(ip, net):
	return ipaddress.ip_address(ip) in ipaddress.ip_network(net)

#checks to make sure the ip address is a valid and
#correctly formatted ip address
def validIP(ip):
	bits = ip.split('.')
	if(len(bits)>4 or len(bits)<4):
		return False
	for x in bits:
		if(x.isdigit()):
			if(int(x)>255):
				return False
		elif(not x.isdigit()):
			return False
	return True

#checks to make sure the network given is valid by using
#a try except statement to catch the exceptions should it
#not valid
def validNetwork(net):
	try:
		ip = ipaddress.ip_network(net)
		return True
	except ValueError:
		return False
	except:
	 	return False

#the script will run indefinitaly untill the user quits
try:
	running = True
	while(running):

		#prompts for a ip address and checks the validity of it
		#if valid, it then prompts for the network. Otherwise
		#it tells the user the address is invalid and prompts for
		#the address again
		ip = input("Enter an IP address: ")
		if(validIP(ip)):

			#prompts for the network and checks the validity of it
			#if valid, it checks to see if the ip address is in the
			#network. Otherwise it prompts for the network again
			netValid = False
			while(not netValid):
				net = input("Enter the network: ")
				if(validNetwork(net)):
					netValid = True
				else:
					print("Invalid Network")

			#checks to see if the ip address is in the network
			if(testAddress(ip, net)==True):
				print("That IP is in the network")
			else:
				print("That IP is not in the network")
		
			#while the user's input is neither y or n, it prompts
			#the user whether they would like to test another ip
			#address and network.
			#
			#if they respond with n the program quits, if they
			#respond with y it goes though the process again
			valid = False
			while(not valid):
				go = input("\nWould you like to check another (y/n)? ")
				if(go.lower()=='n'):
					running = False
					print("Goodbye")
					valid = True
				elif(go.lower()=='y'):
					valid = True
				else:			 
 					print("Invlaid choice")

		#if the ip wasn't valid all the code above gets skipped 
		#and tells the user the ip is invalid and prompts again
		else:
	   		print("Invalid IP Address")
except KeyboardInterrupt:
	print("\nQuitting...")
