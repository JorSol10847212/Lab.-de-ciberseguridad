#!/bin/bash
#
# Menu de escaneos
#
    echo "---------------------------"
    echo "   Menu Principal"
    echo "---------------------------"
    echo "1. Escaneo de red"
    echo "2. Escaneo individual"
    echo "3. Escaneo udp"
    echo "4. Escaneo de script"
    echo "5. Salir"
read -p "Opción  [ 1 - 5 ] " c
case $c in
        1) read -p "Ingresa tu subred para escaneo: " subred
           nmap -sn $subred -oN Red_Scan.txt;;
        2) read -p "Ingresa tu ip: " ip
	   nmap -v -A $ip -oN Indiv_Scan.txt;;
        3) read -p "Ingresa tu ip: " ip
           nmap -sU $ip -oN UDP_Scan.txt;;
        4) read -p "Ingresa el nombre del script a escanear: " script
           read -p "Ingresa tu ip: " ip
           nmap --script $script -v -A $ip;;
        5) echo "Bye!"; exit 0;;
esac