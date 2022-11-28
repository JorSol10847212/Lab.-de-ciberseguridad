# Jorge Andrés Solís Sánchez - 1850014
# 27/10/2022

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Parte 1
#
# Importamos librerias necesarias
import sys
import threading
from socket import *

# Parte 2
# Creamos una función tcp_test la cual permite probar mediante socket
# los puertos abiertos, se le agrega lock.release()
def tcp_test(port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((target_ip, port))
	if result == 0:
		print("Opened port:", port)

# Parte 3
# Establecemos el main del script y guardamos en variables host y portstrs
if __name__=='__main__':
	
	# portscan.py <host> <start_port>-<end_port>
	host = sys.argv[1]
	portstrs = sys.argv[2].split('-')

	# Parte 4
	# portstrs se convierte en lista al momento de hacer split
	# y de ahí obtiene 2 valores
	start_port = int(portstrs[0])
	end_port = int(portstrs[1])

	# Parte 5
	# Usando la función gethostbyname se obtiene la dirección ip
	target_ip = gethostbyname(host)

	# Parte 6
	# Se inicia bucle para probar puertos usando la función tcp_test
	# y generando un hilo por cada puerto a probar
	hilos = []
	for port in range(start_port, end_port):
		hilo = threading.Thread(target=tcp_test, args=(port,))
		hilos.append(hilo)
		hilo.start()