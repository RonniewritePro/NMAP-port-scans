import os

# Prompt user for domain name
domain = input("Enter domain name: ")

# Perform NSLOOKUP to get IP address
stream = os.popen(f"nslookup {domain}")
output = stream.read()
ip = output.split("Address: ")[-1].strip()

# Perform NMAP scans
scans = ["-sV", "-sS", "-sU", "-sT", "-sN"]
for scan in scans:
    cmd = f"nmap {scan} {ip}"
    stream = os.popen(cmd)
    output = stream.read()
    print(output)
