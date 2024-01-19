import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    # Realizar la solicitud HTTP
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML de la página con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # En este ejemplo, supongamos que los títulos de los artículos están dentro de etiquetas <h2>
        # Ajusta esto según la estructura real de la página que estás raspando
        titles = soup.find_all('h2')

        # Imprimir los títulos de los artículos
        for title in titles:
            print(title.text)

    else:
        print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")

# URL de la página web que deseas raspar
url_to_scrape = 'https://www.ejemplo.com'

# Llamada a la función del web scraper
web_scraper(url_to_scrape)
