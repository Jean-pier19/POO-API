import requests
import negocio.procesar_url as negocio_url
from negocio.procesar_url import url_tipo


def obtener_api_post():
    url = negocio_url.url_tipo("posts")

    respuesta = requests.get(url)
    print(respuesta)
    if respuesta.status_code == 200:
        return respuesta.json()
    


def buscar_post_id():
    id = input("intrudece el id del post a buscar: ")

    url = url_tipo(f"posts/{id}")
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        print("Post encontrado")
        print(respuesta.json())  

    else:
        print(f"Error al encontrar el post: {respuesta.status_code}")



def enviar_dato_post():
    user_id = input("Introduce el id de usuario: ")
    title = input("Introduce el título del post: ")
    body = input("Introduce el cuerpo del post: ")

    nuevo_post = {
        'userId': user_id,
        'title': title,
        'body': body 
    }

    url = url_tipo("posts")
    respuesta = requests.post(url, data=nuevo_post)
    if respuesta.status_code == 201: 
        print("Post creado.")
        print(respuesta.json()) 
    else:
        print(f"Error al crear el post: {respuesta.status_code}")


def actualizar_post():
    id = input("intrudece el id de usuario para actualizar el post: ")
    title = input("Introduce el nuevo titulo del post: ")
    body = input("Introcuce el nuevo cuerpo del post: ")

    post_actualizado = {
        'id':id,
        'title':title,
        'body': body
    }

    url = url_tipo(f"posts/{id}")
    respuesta = requests.put(url, data=post_actualizado)

    if respuesta.status_code == 200:
        print("Post actualizado")
        print(respuesta.json())  

    else:
        print(f"Error al actualizar el post: {respuesta.status_code}")



def eliminar_post():
    id = input("intrudece el id del post a eliminar: ")

    url = url_tipo(f"posts/{id}")
    respuesta = requests.delete(url)

    if respuesta.status_code == 200:
        print("Post eliminado")
        print(respuesta.json())  

    else:
        print(f"Error al eliminar el post: {respuesta.status_code}")

