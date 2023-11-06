'''
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona():

    def __init__(self,nombre,edad,DNI) -> None:
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getDni(self):
        return self.DNI
    
    def setNombre(self,valor):
        self.nombre = valor
    
    def setEdad(self,valor):
        self.edad = valor
    
    def setDni(self,valor):
        self.DNI = valor

    def mostrar(self):
        print(self.getNombre())
        print(self.getEdad())
        print(self.getDni())
        if self.getEdad() > 17:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

obj = Persona("Leonel",15,43527099)
obj.mostrar()


