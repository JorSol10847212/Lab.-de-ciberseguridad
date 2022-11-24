# Jorge Solís - 1850014
# 12/10/2022

# Importación de modulogs
import requests
from bs4 import BeautifulSoup

# Obtención de los datos mediante petición GET
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Analizamos el contenido HTML con BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Buscar todos los elementos que el class "card-content"
job_elements = results.find_all("div", class_="card-content")

# Buscar todos los elementos que el h2 contenga en su texto la palabra "python"
python_jobs = results.find_all(
	"h2", string=lambda text: "python" in text.lower()
	)

# Buscar cada elemento que tengan referencia de python_jobs y almacenarlo en python_jobs_elements
python_jobs_elements = [
	h2_element.parent.parent.parent for h2_element in python_jobs
	]

# Mostrar información de python_jobs_elements
for job_element in python_jobs_elements:
	title_element = job_element.find("h2", class_="title")
	company_element = job_element.find("h3", class_="company")
	location_element = job_element.find("p", class_="location")
	# Buscamos elementos con la etiqueta "a"	
	link_url = job_element.find_all("a")[1]["href"]
	print(company_element.text.strip())
	print(location_element.text.strip())
	print(title_element.text.strip())
	#Formateamos el print para que incluya el link
	print(f"Apply Here: {link_url}\n")
	print()