NSLOOKUP and NMAP Scanner
This Python script prompts the user to enter a domain name, performs an NSLOOKUP to find the IP address, and then performs various NMAP scans on the identified IP address.

Prerequisites
This script requires the following software to be installed on your system:

Python 3.x
NMAP
nslookup (should be installed by default on most systems)
How to use
Clone or download the repository to your local machine.
Open a terminal or command prompt in the project directory. 
Run the script using the following command:
bash python3 nmap_scanner.py
When prompted, enter the domain name for which you want to perform the scans.

The script will perform an NSLOOKUP to find the IP address of the domain and then run the following NMAP scans on that IP address:

-sV: Version detection scan
-sS: Stealth scan
-sU: UDP scan
-sT: TCP connect scan
-sN: TCP null scan
The results of each scan will be printed to the console.

Notes
Performing network scans without proper authorization may be illegal and/or unethical. Use this script only for educational or testing purposes on networks that you are authorized to access.
This script assumes that the nslookup and nmap commands are available in the command line environment.
The script has been tested on macOS and Linux systems, but should also work on Windows systems.
