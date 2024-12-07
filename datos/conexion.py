import mysql.connector
from mysql.connector import errorcode

def crear_conexion():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'base datos api'
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