from modelos.post import Post
from servicio.servicio_post import obtener_api_post


def procesar_datos_post():
    publicaciones = obtener_api_post
    post = [Post()]

    for publi in publicaciones:
        
        nueva_publicacion = Post()
        nueva_publicacion.userId = publi[]