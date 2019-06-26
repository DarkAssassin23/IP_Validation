######################################################################
#                                                                    #
# This script takes in two arguments from the comand line, the first #
# is the ip address and the second is the network. Then it checks if #
# both are valid, and if so it tells the user if the ip address is   #
# in the network                                                     #
#																	 #
# Author: Will Jones                                                 #
#                                                                    #
######################################################################


import ipaddress
import sys

#tests if the ip given is in the given network
#if so it returns true otherwise it returns false
def testAddress(ip, net):
	return ipaddress.ip_address(ip) in ipaddress.ip_network(net)

#checks to make sure the ip address is a valid and
#correctly formatted ip address
def validIP(ip):
	bits = ip.split('.')
	if(len(bits)>4):
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

if(len(sys.argv)>1):
	#checks for a valid IP
	if(validIP(sys.argv[1])):
		#checks for a valid network
		if(validNetwork(sys.argv[2])):
			#checks if the ip address given in in the network
			if(testAddress(sys.argv[1], sys.argv[2])==True):
				print("That IP is in the network")
			else:
				print("That IP is not in the network")
		else:
	  		print("Invalid Network")
	else:
		print("Invalid IP Address")
else:
	print("Error: No arguments given")
