## Jorge Andrés
## 01/10/2022
# Importamos fernet desde cryptography

from cryptography.fernet import Fernet
# Definición de la función genwrite que genera una llave para cifrado

def genwrite():
	key = Fernet.generate_key()
	with open("pass.key", "wb") as key_file:
		key_file.write(key)

# Llamamos a la función para generar el archivo "pass.key" que contiene la llave

genwrite()

# Definición de la función call_key con la cual leemos el contenido del archivo "pass.key"

def call_key():
	return open("pass.key", "rb").read()

# Ahora cifraremos un mensaje almacenado y codificado previamente

key = call_key()
banner = "Bienvenido a Laboratorio de Programación en Ciberseguridad de Jorge Solís (LPC)".encode()
a = Fernet(key)
coded_banner = a.encrypt(banner)
print(coded_banner)

# Ahora desciframos el mensaje previamente cifrado

key = call_key()
b = Fernet(key)
decoded_banner = b.decrypt(coded_banner)
print(decoded_banner)

# Fin del script