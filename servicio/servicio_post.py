import requests
import negocio.procesar_url as negocio_url


def obtener_api_post():
    url = negocio_url.url_tipo("post")

    respuesta = requests.get(url)
    print(respuesta)
    if respuesta.status_code == 200:
        return respuesta.json()