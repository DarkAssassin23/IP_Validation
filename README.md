IP Validation 
Version 1.0 
06/25/2019

GENERAL USAGE NOTES
--------------------

- There are two versions of the program, which function exactly the same. 
  The first is a basic one for normal users. The second is for slightly
  more advanced users and utilizes comand line arguments

- This program requires python version 3 to run

--------------------------------------------------------------------------

Utilizing ip_Validation.py
----------------------------

Run this program by: python ip_Validation.py (if python version 3 is not 
your default version of then use python3 ip_Validation.py)

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

---------------------------------------------------------------------------


Utilizing ip_Validation_CL.py
-----------------------------

Run this program by: python ip_Validation_CL.py (if python version 3 is not 
your default version of then use python3 ip_Validation_CL.py)

Since this is the command line version that takes arguments, you must pass it 
an ip address first, followed by the network otherwise it won't work.

After passing the ip address and network it will check to make sure that they
are valid, and tells you if the ip address is in the network or not then the
program exits

-----------------------------------------------------------------------------
