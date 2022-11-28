# Jorge Andrés Solís Sánchez - 1850014
# 28/10/2022

# Escaneo UDP
# Escaneo completo
# Detección de sistema operativo
# Escaneo de red con ping

import sys
from socket import *
import nmap

print("Opciones de escaneo:")
print()
print("1. Escaneo UDP")
print("2. Escaneo completo")
print("3. Detección de sistema operativo")
print("4. Escaneo de red con ping")
print("5. Exit")
print()

menu = int(input("Opción: "))

while menu < 1 and menu > 5:
	menu = int(input("Opción incorrecta: "))

while menu != 5:
	if menu == 1:
		
		host = input("Escriba la ip host: ")
		
		nm = nmap.PortScanner()
		nm.scan(host, arguments='-sU')

		up = nm.all_hosts()
		print(up)

		menu = int(input("Opción: "))

		while menu < 1 and menu > 5:
			menu = int(input("Opción incorrecta: "))

	elif menu == 2:
		host = input("Escriba la ip host: ")
		start_port = 1
		end_port = 65535
		target_ip = gethostbyname(host)
		opened_ports = []

		for port in range(start_port, end_port):
			sock = socket(AF_INET, SOCK_STREAM)
			sock.settimeout(10)
			result = sock.connect_ex((target_ip, port))
			if result == 0:
				opened_ports.append(port)

		print("Opened ports:")
		for i in opened_ports:
			print(i)

		menu = int(input("Opción: "))

		while menu < 1 and menu > 5:
			menu = int(input("Opción incorrecta: "))

	elif menu == 3:
		nm = nmap.PortScanner()
		
		host = input("Escriba la ip host: ")
		
		nm.scan(host, arguments='-O')

		print(nm.command_line())

		menu = int(input("Opción: "))

		while menu < 1 and menu > 5:
			menu = int(input("Opción incorrecta: "))

	else:
		host = input("Escriba la ip host: ")
		
		nm = nmap.PortScanner()
		nm.scan(host, arguments='-sP')

		up = nm.all_hosts()
		print(up)

		menu = int(input("Opción: "))

		while menu < 1 and menu > 5:
			menu = int(input("Opción incorrecta: "))

print("Good bye")