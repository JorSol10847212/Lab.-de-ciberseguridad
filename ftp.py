
# Script para transferencia de FTP
# Objetivo: conectarse a servidor ftp y hacer un upload de un archivo
# 27/10/2022 - v1 Jorge Andrés Solís Sánchez
#
# Importando modulo ftp
from ftplib import FTP

# Conectandonos a la ip host
ftp = FTP('000.000.000.000')

# Ingresando al cuenta
ftp.login('xxxxx','xxxxxxx')

# Cambiando de directorio
ftp.cwd('upload')

# Teniendo el documento, se envía
filename = 'file.txt'
ftp.storbinary('STOR ' + filename, open(filename, 'rb'))

# Se cierra
ftp.quit()