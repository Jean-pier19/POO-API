from servicio.servicio_post import buscar_post_id, enviar_dato_post, actualizar_post, eliminar_post
from servicio.servicio_comments import buscar_comment_id, enviar_dato_comment, actualizar_comment, eliminar_comment



def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Administrar Posts")
        print("2. Administrar Comments")
        print("3. Salir")

        opcion_principal = input("Seleccione una opción (1-3): ")

        if opcion_principal == '1':
            menu_posts()
        elif opcion_principal == '2':
            menu_comments()
        elif opcion_principal == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_posts():
    while True:
        print("\n--- Menú de Posts ---")
        print("1. Buscar Post por ID")
        print("2. Enviar un nuevo Post")
        print("3. Actualizar un Post")
        print("4. Eliminar un Post")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            buscar_post_id()
        elif opcion == '2':
            enviar_dato_post()
        elif opcion == '3':
            actualizar_post()
        elif opcion == '4':
            eliminar_post()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_comments():
    while True:
        print("\n--- Menú de Comments ---")
        print("1. Buscar Comment por ID")
        print("2. Enviar un nuevo Comment")
        print("3. Actualizar un Comment")
        print("4. Eliminar un Comment")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            buscar_comment_id()
        elif opcion == '2':
            enviar_dato_comment()
        elif opcion == '3':
            actualizar_comment()
        elif opcion == '4':
            eliminar_comment()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu_principal()