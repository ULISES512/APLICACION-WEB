import sqlite3

def conectar():
    conexion = sqlite3.connect('Quantom.db')
    cursor = conexion.cursor()
    return conexion, cursor

def crearTabla():
    conexion, cursor = conectar()
    sql = """CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(25) NOT NULL,
        apellido VARCHAR(25) NOT NULL,
        email VARCHAR(25) NOT NULL,
        password VARCHAR(20) NOT NULL,
        direccion VARCHAR(30) NOT NULL
    )"""
    try:
        cursor.execute(sql)
        print('Tabla Creada')
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.commit()  
        conexion.close()   

def insertar(datos):
    conexion, cursor = conectar()
    sql = "INSERT INTO usuarios(nombre, apellido, email, password, direccion) VALUES(?,?,?,?,?)"
    try:
        cursor.execute(sql, datos)  
        print('Datos Guardados correctamente')
    except sqlite3.Error as e:
        print(f'Error al guardar los datos: {e}')
    finally:
        conexion.commit() 
        conexion.close()   

def consultar():
    conexion, cursor = conectar()
    sql = "SELECT id, nombre, apellido, email, password, direccion FROM usuarios"
    try:
        cursor.execute(sql) 
        filas = cursor.fetchall()  
        for fila in filas:
            print(f"id = {fila[0]}")
            print(f"nombre = {fila[1]}")
            print(f"apellido = {fila[2]}")
            print(f"email = {fila[3]}")
            print(f"password = {fila[4]}")
            print(f"direccion = {fila[5]}\n")
    except sqlite3.Error as e:
        print(f"Error en la consulta: {e}")
    finally:
        conexion.close() 

if __name__ == "__main__":
    crearTabla()  
    for i in range(5):  
        nombre = input('Ingresa el nombre del usuario: ')
        apellido = input('Ingresa el apellido del usuario: ')
        email = input('Ingresa el email del usuario: ')
        contra = input("Ingresa la contraseña: ")
        direccion = input('Ingresa la dirección: ')

        datos = (nombre, apellido, email, contra, direccion)  
        insertar(datos) 

    consultar()  
