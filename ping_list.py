import os
import sys
import json
from colorama import init, Fore

init(autoreset=True)


# Lendo o Arquivo de texto com os endereços Ips
try:
	f = open("ip_list.json", "r")
	ips = json.loads(f.read())
except: 
	print("Erro ao ler arquivo de lista")
	raise
finally:
	f.close()

# Saber se é Linux ou Windows
arq = sys.platform

# Comandos diferentes para cada plataforma
if arq == "win32":
	command = "ping -n 4"
	msg = "Recebidos = 4" 
else:
	command = "ping -c4"
	msg = "4 received" 


for name, ip in ips.items():
	
	response = os.popen(f"{command} {ip}").read()
	
	if msg  in response:
		print(f"{name} - {ip}  {Fore.LIGHTGREEN_EX } \t\t[UP]")
	else:
		print(f"{name} - {ip}  {Fore.RED } \t\t[DOWN]")
