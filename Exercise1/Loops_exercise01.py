scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")

 #Above program prints all service ips running on a port that are present in the list
 """If you use only the dict name (here it is scan) and loop, it will throw error as it cannot unpack a dict value for looping. 
    We need to .items() after dict name to loop through each key value pairs in a dictionary
 """