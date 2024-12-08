from modelos.comments import Comments
from servicio.servicio_comments import obtener_api_comments

def procesar_comments():
    comentario = obtener_api_comments
    comments = [Comments()]

    for coment in comentario():
        
        nuevo_comentario = Comments()
        nuevo_comentario.postId = coment['postId']
        nuevo_comentario.id = coment['id']
        nuevo_comentario.email = coment['email']
        nuevo_comentario.body = coment['body']

        crear_dict = {
            'postId': nuevo_comentario.postId,
            'id': nuevo_comentario.id,
            'email': nuevo_comentario.email,
            'body': nuevo_comentario.body
        }
        comments.append(crear_dict)
    print(comments)
