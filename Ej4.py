'''
Consigna 2: Propiedades, atributos públicos y privados con métodos de clase y estáticos

Crea una clase llamada "Persona" con los siguientes atributos:

"nombre" (público)
"_edad" (privado, utilizando la convención de un guión bajo)
Agrega los siguientes métodos a la clase:

Un método @property llamado "edad" que devuelve el valor del atributo "_edad".
Un método setter para "edad" que permite actualizar "_edad" solo si el nuevo valor es un número positivo.
Un método de clase llamado "crear_persona" que toma un nombre y un año de nacimiento como argumentos y crea una instancia de "Persona" con el nombre y la edad calculada a partir del año de nacimiento.
Un método estático llamado "calcular_edad" que toma un año de nacimiento como argumento y devuelve la edad calculada como la diferencia entre el año actual (2023) y el año de nacimiento.
Luego, crea instancias de "Persona" utilizando el método de clase "crear_persona" y muestra la información de la persona, incluyendo su nombre y edad.

Estas consignas deberían permitirte practicar las características mencionadas en Python.
'''

class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def seter(self,edad):
        self.__edad = edad
        while self.__edad <= 0:
            print("No se puede")
            self.__edad = int(input("Error. Ingrese edad positiva: "))

    @classmethod
    def crear_persona(cls,nombre,nacimiento):
        cls.nombre = nombre
        cls.edad = cls.calcular_edad(nacimiento)

        print(f"Su nombre es {cls.nombre} y su edad {cls.edad}")

    @staticmethod
    def calcular_edad(nacimiento):
        return 2023-nacimiento
        

obj = Persona("leo",21)
obj.crear_persona("Leonel",2001)









    




