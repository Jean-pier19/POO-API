import mysql.connector
from mysql.connector import errorcode
import requests

url_base_jsonplaceholder = "https://jsonplaceholder.typicode.com/"

class Geo:
    def __init__(self, id_geo = 0, lat = '', lng = ''):
        self.id_geo = id_geo
        self.lat = lat
        self.lng = lng

class Address(Geo):
    def __init__(self, id_geo = 0, id_address = 0, street = '', suite = '', city = '', zipcode = ''):
        super().__init__(id_geo)
        self.id_address = id_address
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode

class Company:
    def __init__(self, id_company = 0, company_name = '', catchPhrase = '', bs = ''):
        self.id_company = id_company
        self.company_name = company_name
        self.catchPhrase = catchPhrase
        self.bs = bs

class User(Address, Company):
    def __init__(self, id_address = 0, id_company = 0, id_user = 0, name = '', username = '', email = '', phone = '', website = ''):
        super().__init__(id_address)
        super().__init__(id_company)
        self.id_user = id_user
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website

def url_servicio(origen):
    #direccion = f"{url_base}{origen}"
    #direccion = f"{url_base_jsonplaceholder}{origen}"
    direccion = f"https://jsonplaceholder.typicode.com/{origen}"
    return direccion

def obtener_usuarios_api():
    #direccion = url_base("users")
    direccion = url_servicio("users")

    try:
        respuesta = requests.get(direccion)
        print(respuesta)
        respuesta.raise_for_status()

        if respuesta.status_code == 200:
            return respuesta.json()

    except requests.exceptions.Timeout:
        print("Se sobrepasó el timepo de espera para la respuesta.")

    except requests.exceptions.ConnectionError:
        print("Hay un problema de comunicación con le servidor.")
    
    except requests.exceptions.RequestException as error: 
        print(f"Error en la solicitud: {error}")

def procesar_datos_usuarios():
    usuarios_api = obtener_usuarios_api()
    #usuarios_api = obtener_usuarios_api()
    #data_usuarios = json.loads(json.dumps(usuarios_api))
    usuarios = [User()]

    for usr in usuarios_api:
        nuevo_usuario = User()
        nuevo_usuario.id_user = usr['id']
        nuevo_usuario.name = usr['name']
        nuevo_usuario.username = usr['username']
        nuevo_usuario.email = usr['email']
        nuevo_usuario.phone = usr['phone']
        nuevo_usuario.website = usr['website']
        
        nuevo_usuario.street = usr['address']['street']
        nuevo_usuario.suite = usr['address']['suite']
        nuevo_usuario.city = usr['address']['city']
        nuevo_usuario.zipcode = usr['address']['zipcode']

        nuevo_usuario.lat = usr['address']['geo']['lat']
        nuevo_usuario.lng = usr['address']['geo']['lng']
        
        nuevo_usuario.company_name = usr['company']['name']
        nuevo_usuario.catchPhrase = usr['company']['catchPhrase']
        nuevo_usuario.bs = usr['company']['bs']

        usuarios.append(nuevo_usuario)

    #return usuarios
    #def insertar_varios_usuarios(usuarios = [usuario()]):
    insertar_geolocalizaciones = f"""
        INSERT INTO geos(lat,lng) VALUES
        (%S, %S);
        """
    insertar_direcciones = f"""
        INSERT INTO addresses(street,suite,city,zipcode,id_geo) VALUES
        (%S, %S, %S, %S, %S);
        """
    insertar_companias = f"""
        INSERT INTO companies(company_name,catchPhrase,bs) VALUES
        (%S, %S, %S);
        """
    insertar_usuarios = f"""
        INSERT INTO users(id_user,name,username,email,id_address,phone,website,id_company) VALUES
        (%S, %S, %S, %S, %S, %S, %S, %S);
        """
    data_geolocalizaciones = []
    data_direcciones = []
    data_companias = []
    data_usuarios = []
    contador = 0
    
    for usr in usuarios:
        contador += 1
        data_geolocalizaciones.append(f"{usr.lat},{usr.lng}")
        data_direcciones.append(f"{usr.street},{usr.suite},{usr.city},{usr.zipcode},{contador}")
        data_companias.append(f"{usr.company_name},{usr.catchPhrase},{usr.bs}")
        data_usuarios.append(f"{usr.id_user},{usr.name},{usr.username},{usr.email},{contador},{usr.phone},{usr.website},{contador}")
        
    #id = acceso_db.insertar_multiples_datos(consulta, data_usuarios)
    id = insertar_multiples_datos(insertar_geolocalizaciones, data_geolocalizaciones)
    id = insertar_multiples_datos(insertar_direcciones, data_direcciones)
    id = insertar_multiples_datos(insertar_companias, data_companias)
    id = insertar_multiples_datos(insertar_usuarios, data_usuarios)

def generar_conexion():
    config={
        # 'host': host,
        # 'user': user,
        # 'password': password,
        # 'database': database
        'host': "localhost",
        'user': "evaluacion",
        'password': "a1b2c3d4e5",
        'database': "evaluacion_3"
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion and conexion.is_connected():
            return conexion
        else:
            print("No fue posible conectarse a la base de datos.")
    
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado, usuario o contraseña incorrectos.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe")
        else:
            print(error)
    else:
        conexion.close()
        
def insertar_multiples_datos(consulta, data):      
    conexion = generar_conexion()
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

procesar_datos_usuarios()