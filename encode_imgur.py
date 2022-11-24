## Jorge Andrés
## 01/10/2022
import requests # Para hacer un request a un sitio
import base64 # Para Encode/decode en base 64
#
## Para descargar la imagen del sitio
#
if __name__=='__main__':
	url = 'https://i.imgur.com/wcWk8Ao.jpeg'

	Response: Response = requests.get(url, stream=True)
	with open('stones.jpg', 'wb') as file_down:
		for chunk in Response.iter_content(): # Descargando contenido poco a poco
			file_down.write(chunk)
	Response.close()
#
## Para codificar la imagen
#
with open('stones.jpg', 'rb') as binary_file:
	binary_file_data = binary_file.read()
	base64_encoded_data = base64.b64encode(binary_file_data)
	base64_message = base64_encoded_data.decode('utf8')

	print(base64_message)