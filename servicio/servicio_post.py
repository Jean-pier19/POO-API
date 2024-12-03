import requests
from auxiliares.URL import url_post

def consultar_api_post():
    URL = url_post 
    respuesta = requests.get(URL)

    if respuesta.status_code == 200:
        return respuesta.json()