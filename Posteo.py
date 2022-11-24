import requests
import json

if __name__ == "__main__":
    url = "http://httpbin.org/post"
    argumentos = {"Nombre":"Jorge", "Matricula":"1850014", "Curso":"Programación para Ciberseguridad"}
    
    response = requests.post(url, params=argumentos)
    
    if response.status_code == 200:
        print(response.content)