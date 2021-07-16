import os
from colorama import init, Fore

init(autoreset=True)

ip_list = ["8.8.8.8", "8.8.4.4", "172.0.0.2"]

for ip in ip_list:
	
	response = os.popen(f"ping {ip}").read()
	
	if "Recebidos = 4" in response:
		print(f"{ip}  {Fore.LIGHTGREEN_EX } \t\t[UP]")
	else:
		print(f"{ip}  {Fore.RED } \t\t[DOWN]")