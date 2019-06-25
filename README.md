IP Validation Version 1.0 06/25/2019

GENERAL USAGE NOTES
--------------------

- There are two versions of the program, which function exactly the same. 
  The first is a basic one for normal users. The second is for slightly
  more advanced users and utilizes comand line arguments

- This program requires python version 3 to run

--------------------------------------------------------------------------

Utilizing ip_Validation.py
----------------------------

Run this program by:
```bash
python ip_Validation.py 
```
If python version 3 is not your default version of then use
```bash
python3 ip_Validation.py
```

Once launched, the program will ask you for an ip address and network
If your ip address is invalid, it will tell you and keep prompting you
until you enter a valid one.

Once a valid ip address is entered it will then ask you for the network.
Like the ip address, if your network is invalid it will tell you and keep
prompting you until you enter a valid network.

Once a valid ip address and network have been entered it will check to see
if the ip address is indeed in the network.

Finally, it will prompt you if you want to check a new ip and network or not
if you do not check again the program will exit otherwise the process 
repeats

Example Output:
```bash
python ip_Validation.py
Enter an IP address: 23.8.203.6
Enter the network: 128.167.192.0/18
That IP is not in the network

Would you like to check another (y/n)? y
Enter an IP address: 45.62.44.130
Enter the network: 45.62.0.0/16 
That IP is in the network

Would you like to check another (y/n)? n
Goodbye
```

---------------------------------------------------------------------------


Utilizing ip_Validation_CL.py
-----------------------------

Run this program by
```bash
python ip_Validation_CL.py [ip_address] [network] 
```
If python version 3 is not your default version of then use
```bash
python3 ip_Validation_CL.py [ip_address] [network]
```
Examples:
```bash
python ip_Validation_CL.py 192.168.1.13 192.168.1.0/24
python ip_Validation_CL.py 43.170.89.3 250.224.128.16/30
python3 ip_Validation_CL.py 13.132.97.10 13.253.128.0/17
python3 ip_Validation_CL.py 8.79.202.78 8.0.0.0/9
```


Since this is the command line version that takes arguments, you must pass it 
an ip address first, followed by the network otherwise it won't work.

After passing the ip address and network it will check to make sure that they
are valid, and tells you if the ip address is in the network or not then the
program exits

Example Output:
```bash
python ip_Validation_CL.py 43.170.89.3 250.224.128.16/30
That IP is not in the network
```

-----------------------------------------------------------------------------
