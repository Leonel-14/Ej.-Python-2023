import sqlite3
#este modulo si puede crear la base de datos desde el codigo
def coneccionBD():
    bd = sqlite3.connect("base_de_datos.db")
    return bd

def crearTabla():
    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    nro_legajo INTEGER NOT NULL UNIQUE,
                    dni INTEGER NOT NULL UNIQUE,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    area TEXT NOT NULL)''')
    bd.commit() #guarda los cambios

def insertarRegistro(nro_legajo,dni,nombre,apellido,area):
    sentencia = "INSERT INTO empleados (nro_legajo,dni,nombre,apellido,area) VALUES (?,?,?,?,?);"
    cursor.execute(sentencia,[nro_legajo,dni,nombre,apellido,area])
    bd.commit()

def seleccionarRegistro(dni):
    sentencia = "SELECT * FROM empleados WHERE dni = ?;"
    for row in cursor.execute(sentencia,[dni]):
        print(row)

def seleccionarTodosEmpleado():
     for row in cursor.execute("SELECT * FROM empleados;"):
         print(row)

def modificarRegistro(area,nro_legajo):
    sentecia = "UPDATE empleados SET area = ? WHERE nro_legajo = ?;"
    cursor.execute(sentecia,[area,nro_legajo])
    bd.commit()

def eliminarRegistro(nro_legajo):
    sentencia = "DELETE FROM empleados WHERE nro_legajo = ?;"
    cursor.execute(sentencia,[nro_legajo])
    bd.commit()


def menu():
    print("Opcion 1 Insertar un registro de empleado.")
    print("Opcion 2 Selecionar un registro de empleado a partir de su numero DNI.")
    print("Opcion 3 Selecionar todos los empleados o los registros de la tabla.")
    print("Opcion 4 Modificar el area de un empleado en función de su numero de legajo.")
    print("Opcion 5 Eliminar un empleado a partir del numero de legajo.")
    print("Opcion 6 Finalizar.")
    try:
        opcion = int(input("Opcion: "))
    except ValueError as e:
        print("Error",e)
    else:
        return opcion


bd = coneccionBD()
cursor = bd.cursor()
print("Base de datos Abierta")
crearTabla()

while True:
    match menu():
        case 1:
            nro_legajo = int(input("Numero de Legajo: "))
            dni = int(input("DNI: "))
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            area = input("Area: ")
            insertarRegistro(nro_legajo,dni,nombre,apellido,area)
        case 2:
            dni = int(input("DNI: "))
            seleccionarRegistro(dni)
        case 3:
            seleccionarTodosEmpleado()
        case 4:
            area = input("Area: ")
            nro_legajo = int(input("Numero de Legajo: "))
            modificarRegistro(area,nro_legajo)
        case 5:
            nro_legajo = int(input("Numero de Legajo: "))
            eliminarRegistro(nro_legajo)
        case 6:
            bd.close()
            print("Base de datos Cerrada")
            break
    

