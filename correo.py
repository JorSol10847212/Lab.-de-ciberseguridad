# Primero importamos lo necesario para el envío del correo
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# Aquí abrimos el mensaje, en donde podremos juntar tanto el html como la imagen
message = MIMEMultipart()
message['Subject'] = "Prueba de envio (script Python) - 1850014"


# Escribimos el mensaje en html
html = """
<html>
	<body>

		<h2><b>Practica 12</b></h2>

		<p>Ejercicio de la practica 12 para envío de correos</p>

		<b>Alumno: </b><p>Perez Lopez</p>


		<b>Matricula: </b><p>117676</p>
	</body>
</html>

"""

# Declaramos el mensaje como html y lo añadimos a "message" de Multiparts
msg = MIMEText(html, "html")
message.attach(msg)


# Abrimos la imagen que queremos envíar, la leemos y la añadimos a "message" de Multiparts
with open('fcfm_cool.png', 'rb') as foto:
	img = MIMEImage(foto.read())
	message.attach(img)


# Pedimos el correo y la contraseña de origen
correo1 = input("Correo origen: ")
pswd = input("Contraseña: ")


# Nos conectamos al correo y enviamos el mensaje, ya unido el html (convertido a string) y la imagen
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as conn:
	conn.login(correo1,pswd)
	conn.sendmail(correo1,'soy.yo@correo.com',message.as_string())