import os
import time


with open('hosts.txt') as file:
	dump = file.read()
	dump = dump.splitlines()
	for ip in dump:
		print(ip)
		print(f'Verificando o ip: {ip}')
		print('-'*60)
		os.system(f'ping -c 2 {ip}')
		print('-'*60)
		time.sleep(5)
