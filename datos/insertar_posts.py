from modelos.post import Posts
from negocio.procesar_post import procesar_datos_post
from datos.insertar_multiples_datos import insertar_multiples_datos


def insertar_post():
    
    posts_data = procesar_datos_post()

    insertar_post = f"""
    INSERT INTO publicaciones(userId, id, title, body) 
    VALUES (%s, %s, %s, %s)
    """

    data_post = []
    contador = 0
    for publi in posts_data:
        contador += 1
        data_post.append((publi.userId, publi.id, publi.title, publi.body))
        
    print("Datos a insertar:", data_post)

    insertar_multiples_datos(insertar_post, data_post)

    return insertar_multiples_datos