import mysql.connector
from mysql.connector import errorcode
from auxiliares.config_db import user, password, host, database

def crear_conexion():
    config = {
        'user': user,
        'password': password,
        'host': host,
        'database': database
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            return conexion
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error en las credenciales.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")
        else:
            print(err)
    return None