from modelos.post import Posts
from servicio.servicio_post import obtener_api_post


def procesar_datos_post():
    publicacion = obtener_api_post
    post = [Posts()]

    for publi in publicacion():
        
        nueva_publicacion = Posts()
        nueva_publicacion.userId = publi['userId']
        nueva_publicacion.id = publi['id']
        nueva_publicacion.title = publi['title']
        nueva_publicacion.body = publi['body']
        post.append(nueva_publicacion)

    print(post)