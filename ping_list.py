import os
import json
from colorama import init, Fore

init(autoreset=True)


try:
	f = open("ip_list.json", "r")
	ips = json.loads(f.read())
except: 
	print("Erro ao ler arquivo de lista")
	raise



for name, ip in ips.items():
	
	response = os.popen(f"ping {ip}").read()
	
	if "Recebidos = 4" in response:
		print(f"{name} - {ip}  {Fore.LIGHTGREEN_EX } \t\t[UP]")
	else:
		print(f"{name} - {ip}  {Fore.RED } \t\t[DOWN]")