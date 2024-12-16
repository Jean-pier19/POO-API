from datos.conexion import crear_conexion

def insertar_multiples_datos(consulta, data):      
    conexion = crear_conexion()
    cursor = conexion.cursor()
    if cursor != None:
        cursor.executemany(consulta, data)
        conexion.commit()
        id = cursor.lastrowid
        cursor.close()        
        return id
    else:
        print("No fue posible insertar datos")
    conexion.close()