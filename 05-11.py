class Alumno():
    def __init__(self,nombre:str,materias:list,materias_aprobadas:list) -> None:
        self.nombre = nombre
        self.materias = []
        self.materias_aprobadas = []

    def enviar_solicitud(self):
        return f"Nombre: {self.nombre} Materia Solicitada: {self.materias} Aprobadas: {self.materias_aprobadas}"

class Verificador():
    def __init__(self,alumnos_solicitantes:list) -> None:
        self.alumnos_solicitantes = alumnos_solicitantes
    
    def verificar(self):
        Al = Alumno

class Materia():
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.alumnos_inscriptos = []

class Profesor():
    pass

class Coordinador():
    pass