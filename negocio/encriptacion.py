import os
from cryptography.fernet import Fernet
from auxiliares.clave import clave_guardada


def encriptar_contrasena(contrasena):
    clave = Fernet(clave_guardada)  
    token = clave.encrypt(contrasena.encode('utf-8')) 
    print(f"Contraseña encriptada: {token}") 
    return token

def desencriptar_contrasena(token):
    clave = Fernet(clave_guardada)  
    contrasena_desencriptada = clave.decrypt(token).decode('utf-8') 
    print(f"Contraseña desencriptada: {contrasena_desencriptada}")  
    return contrasena_desencriptada
