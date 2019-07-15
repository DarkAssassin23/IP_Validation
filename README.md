# IP Validation
**Version:** 1.2 <br />
**Published Date:** 07/15/2019

GENERAL USAGE NOTES
--------------------

- There are two versions of the program, which function exactly the same. 
  The first is a basic one for normal users. The second is for slightly
  more advanced users and utilizes command line arguments

- This program requires python version 3 to run

--------------------------------------------------------------------------

Utilizing IP Validation
----------------------------

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
./ip_Validation
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


Utilizing IP Validation (Command Line Arguments Version)
-----------------------------

Since this is the command line version that takes arguments, you must pass it 
an ip address first, followed by the network otherwise it won't work.

After passing the ip address and network it will check to make sure that they
are valid, and tells you if the ip address is in the network or not then the
program exits

Example Output:
```bash
./ip_Validation_CL.py 43.170.89.3 250.224.128.16/30
That IP is not in the network

./ip_Validation_CL.py 8.79.202.78 8.0.0.0/9
That IP is in the network
```

-----------------------------------------------------------------------------

Linux/MacOS
-----------

This program can be run in either of the following ways, using the respective
MacOS and Linux Versions:
```bash
python ip_Validation 
```
```bash
python3 ip_Validation
```
```bash
./ip_Validation
```
```bash
python ip_Validation_CL [ip_address] [network]
```
```bash
python3 ip_Validation_CL [ip_address] [network]
```
```bash
./ip_Validation_CL [ip_address] [network]
```
If you chose instead to run the source code, use the following:
```bash
python ip_Validation.py
```
```bash
python3 ip_Validation.py
```
```bash
python ip_Validation_CL.py [ip_address] [network]
```
```bash
python3 ip_Validation_CL.py [ip_address] [network]
```
An optional step you can do is, edit your .bash_profile file so you only have to type the name of the file to run it. To do so add the following line to your .bash_profile file:
```bash
alias ipvalidation='python3 /path/to/your/file/ip_Validation' 
```
And you can call 'ipvalidation' whatever you like and you would do the same for the ip_Validation_CL file as well. **Note:** in order for this to take effect you must restart the terminal.

Once you do this all you will need to do is:
```bash
ipvalidation
```
Or
```bash
ipvalidationCL [ip address] [network]
```
And unlike the other methods where you had to be in the same directory as the file, this allows you to run the program from any directory while using the terminal


--------------------------------------

Windows
----------------

Windows takes a little more effort. First in each respective .bat file, make
sure you replace the
```bash
C:/path/to/the/file/ip_Validation.py
```
Portion, with the actual path to the file, but leave everything else the
same, including the %*. All you have to do now is press click on the batch file and it will run the program. However, the command line arguments one, will not work this way. You have to manually type that on the command prompt in the directory where your .bat file is saved 

Additionally, if you want to utilize the Windows Run feature, you can add 
the batch files as path variables. To do this, go to Control Panel --> 
System --> Advanced System Settings, then click the Advanced tab and select 
Environment Variables. Here, locate the PATH variable under System Variables 
and select edit.

Next add the path to the folder where the .bat files, you should just be able to click 'new' and add the path to the folder and press ok on all the windows and exit out of Control Panel.

Then you can just do Win + R then either:
```bash
ip_Validation 
```
or
```bash
ip_Validation_CL [ip address] [network]
```

