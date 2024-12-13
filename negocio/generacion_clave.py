import os
from cryptography.fernet import Fernet

def generacion_clave():
    key = Fernet.generate_key()
    clave_guardar = f"clave_guardada = {key}"
    
    
    file = 'clave.py'
    ubicacion = os.path.join('auxiliares', file)
    ubicacion = os.path.abspath(ubicacion)
    ubicacion = os.path.realpath(ubicacion)    
    archivo = open(f"{ubicacion}", "w+")
    archivo.write(clave_guardar)
    archivo.close()