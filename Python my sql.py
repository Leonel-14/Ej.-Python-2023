import pymysql
#este modulo no puede crear la base de datos desde codigo

#misma consigna que el ejercicio SQLite
try:
    db = pymysql.connect(host='localhost',
        port=8080,
        user='root',
        password='',
        db = "empleados"
    )
    cursor = db.cursor()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrio un error al concectar: ",e)
else:
    print("Conecto")
    

