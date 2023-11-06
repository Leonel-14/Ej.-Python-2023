import mariadb

try:
    conexion = mariadb.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="proyecto_mac",
        port=3307
        )
    print("Conexion exitosa")
except:
    print("Conexion erronea")

base_de_datos = conexion.cursor()

def menu():
    print("--Menu--")
    print("1)Ver todos los dispositivos")
    print("2)Ver conectados")
    print("3)Ver desconectados")
    print("4)Agregar dipositivo")
    print("5)Conectar Dispositivo")
    print("6)Desconectar Dispositivo")
    print("7)Cambiar nombre de dispositivo")
    print("8)Salir")
    opcion = int(input("Opcion: "))
    while(opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 and opcion != 7 and opcion != 8):
        print("Opcion Incorrecta, elija de nuevo")
        opcion = int(input("Opcion: "))
    return opcion


entrada = 'n'
while(entrada == 'n'):

    opcion = menu()

    if(opcion == 1):
        base_de_datos.execute("SELECT dispositivos.id_dispositivo,dispositivos.nombre,dispositivos.mac,estados.nombre FROM dispositivos INNER JOIN estados ON dispositivos.id_estado = estados.id_estado")
        for i in base_de_datos:
            print("|",i)
    elif(opcion == 2):
        base_de_datos.execute("SELECT dispositivos.id_dispositivo,dispositivos.nombre,dispositivos.mac,estados.nombre FROM dispositivos INNER JOIN estados ON dispositivos.id_estado = estados.id_estado WHERE estados.id_estado = 1")
        for i in base_de_datos:
            print("|",i)
    elif(opcion == 3):
        base_de_datos.execute("SELECT dispositivos.id_dispositivo,dispositivos.nombre,dispositivos.mac,estados.nombre FROM dispositivos INNER JOIN estados ON dispositivos.id_estado = estados.id_estado WHERE estados.id_estado = 2")
        for i in base_de_datos:
            print("|",i)
    elif(opcion == 4):
        nombre = input("Ingrese nombre: ")
        mac = input("Ingrese mac: ")
        base_de_datos.execute(f"INSERT INTO dispositivos (nombre,mac,id_estado) VALUES ('{nombre}','{mac}',2)")
        conexion.commit()
        print("Carga Exitosa")
    elif(opcion == 5):
        base_de_datos.execute("SELECT dispositivos.id_dispositivo,dispositivos.nombre,dispositivos.mac,estados.nombre FROM dispositivos INNER JOIN estados ON dispositivos.id_estado = estados.id_estado WHERE estados.id_estado = 2")
        for i in base_de_datos:
            print("|",i)
        id = int(input("Que dispositivo quiere conectar: "))
        base_de_datos.execute(f"UPDATE dispositivos SET id_estado = 1 WHERE id_dispositivo = '{id}'")
        conexion.commit()
        print("☑ Dispositivo Conectado ☑")
    elif(opcion == 6):
        base_de_datos.execute("SELECT dispositivos.id_dispositivo,dispositivos.nombre,dispositivos.mac,estados.nombre FROM dispositivos INNER JOIN estados ON dispositivos.id_estado = estados.id_estado WHERE estados.id_estado = 1")
        for i in base_de_datos:
            print("|",i)
        id = int(input("Que dispositivo quiere desconectar: "))
        base_de_datos.execute(f"UPDATE dispositivos SET id_estado = 2 WHERE id_dispositivo = '{id}'")
        conexion.commit()
        print("☒ Dispositivo Desconectado ☒")
    elif(opcion == 7):
        id = int(input("Ingrese el ID del nombre a cambiar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        for x in base_de_datos.execute(f"SELECT id_dispositivo FROM dispositivos"):
            print(x)
        base_de_datos.execute(f"UPDATE dispositivos SET nombre = '{nuevo_nombre}' WHERE id_dispositivo = '{id}'")
        conexion.commit()
        print("Nombre Actualizado con Exito")
        
    elif(opcion == 8):
        entrada = input("Desea salir?: s | n : ")
    

print("♣ Programa Finalizado ♣")


