import negocio.encriptacion

ingrese_contrasena = input("Ingrese Contraseña: ")
contrasena_encriptada = negocio.encriptacion.encriptar_contrasena(ingrese_contrasena)

ingrese_contrasena = input("Ingrese contraseña: ")
contrasena_anterior = negocio.encriptacion.desencriptar_contrasena(contrasena_encriptada)

if contrasena_anterior == ingrese_contrasena:
    print("Permiso concedido")
else:
    print("Permiso denegado")



