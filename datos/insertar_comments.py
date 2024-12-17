from modelos.comments import Comments
from negocio.procesar_comments import procesar_datos_comments
from datos.insertar_multiples_datos import insertar_multiples_datos

def insertar_comment():
    
    comments_data = procesar_datos_comments()

    insertar_comment = f"""
    INSERT INTO comentarios(postId, id, name, email, body) 
    VALUES (%s, %s, %s, %s, %s)
    """

    data_comment = []
    
    for coment in comments_data:
        data_comment.append((coment.postId, coment.id, coment.name, coment.email, coment.body))
        
    print("Datos insertados:", data_comment)

    insertar_multiples_datos(insertar_comment, data_comment)

    return insertar_multiples_datos 