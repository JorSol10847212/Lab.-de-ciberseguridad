
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Parte 1

# Importamos librerias necesarias
import sys
from socket import *

# Parte 2
# Modo de ejecución del script
# port_scan.py <host> <start_port>-<end_port>
# Primer argumento se guarda en variable host
# Segundo argumento se guarda en variable portstrs
host = sys.argv[1]
portstrs = sys.argv[2].split('-')

# Parte 3
# portstrs contiene dos valores que asignamos
# en start_port el valor de inicio
# en end_port el valor fin
start_port = int(portstrs[0])
end_port = int(portstrs[1])

# Parte 4
# Para usar en el socket asignados lo de la 
# variable host a target_ip
# Definimos una lista de puertos opened_ports
target_ip = gethostbyname(host)
opened_ports = []

# Parte 5
# Iniciamos bucle for para probar puertos
for port in range(start_port, end_port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((target_ip, port))
	if result == 0:
		opened_ports.append(port)

# Parte 6
# Se imprime salida
print("Opened ports:")
for i in opened_ports:
	print(i)
