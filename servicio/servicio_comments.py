import requests
import negocio.procesar_url as negocio_url
from negocio.procesar_url import url_tipo


def obtener_api_comments():
    url = negocio_url.url_tipo("comments")

    respuesta = requests.get(url)
    print(respuesta)
    if respuesta.status_code == 200:
        return respuesta.json()


def buscar_comment_id():
    id = input("intrudece el id del comment a buscar: ")

    url = url_tipo(f"comments/{id}")
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        print("Comment encontrado")
        print(respuesta.json())  

    else:
        print(f"Error al encontrar el comment: {respuesta.status_code}")



def enviar_dato_comment():
    Id = input("Introduce el id de comment: ")
    name = input("Introduce el nombre del comment: ")
    email = input("Introduce el email: ")
    body = input("Introduce el cuerpo del comment: ")

    nuevo_comment = {
        'Id': Id,  
        'name': name,
        'email': email,
        'body': body 
    }

    url = url_tipo("comments")
    respuesta = requests.post(url, data=nuevo_comment)
    if respuesta.status_code == 201: 
        print("Comment creado exitosamente.")
        print("Respuesta del servidor:", respuesta.json()) 
    else:
        print(f"Error al crear el comment: {respuesta.status_code}")



def actualizar_comment():
    id = input("intrudece el id  para actualizar el commten: ")
    name = input("Introduce el nuevo nombre del comment: ")
    email = input("Introcuce el nuevo email del comment: ")
    body = input("Introcuce el nuevo cuerpo del comment: ")

    comment_actualizado = {
        'id':id,
        'name':name,
        'email': email,
        'body':body,
    }

    url = url_tipo(f"comments/{id}")
    respuesta = requests.put(url, data=comment_actualizado)
    if respuesta.status_code == 200:
        print("Comment actualizado")
        print(respuesta.json())  
    else:
        print(f"Error al actualizar el comment: {respuesta.status_code}")




def eliminar_comment():
    id = input("intrudece el id del commment a eliminar: ")

    url = url_tipo(f"comments/{id}")
    respuesta = requests.delete(url)

    if respuesta.status_code == 200:
        print("Comment eliminado")
        print(respuesta.json())  

    else:
        print(f"Error al eliminar el comment: {respuesta.status_code}")