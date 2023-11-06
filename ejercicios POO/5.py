'''
Crear una clase llamada persona
Con los siguientes atributos privados
nombre
edad
dni
y los siguientes metodos:
mostrar_edad(): retorna la edad de la persona
es_mayor_edad(): retorna True si edad es mayor o igual a 18, o False si es menor a 18
'''

class Persona():
    def __init__(self,nombre,edad,dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    def mostrar_edad(self):
        return self.__edad

    def es_mayor_edad(self):
        if self.__edad > 17:
            retorno = True
        else:
            retorno = False

        #return self.__edad >= 18 -> retornara true o flase

        return retorno
    
persona = Persona("Leo",18,43527099)
print(persona.mostrar_edad())
print(persona.es_mayor_edad())
#print(persona.__dict__) imprime en forma de diccionario la clase
persona.nuevo = "algo"
print(persona.__dict__)
print(persona.nuevo)

'''
def main():
    codigo

if __name__ == "__main.py":
    main()

esto se usa como limitador de codigo
'''
