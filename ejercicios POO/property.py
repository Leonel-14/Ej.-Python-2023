'''
class clase:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    def getter(self):
        return self.__nombre
    
obj = clase("Leonel")
print(obj.getter())

#Este es el caso del getter comun y corriente
'''
'''
class clase:
    def __init__(self, nombre) -> None:
        self.__algo = nombre

    @property
    def getter(self):
        return self.__algo
    
obj = clase("Leonel")
print(obj.getter)

#este el caso property donde no hace falta poner parentesis en el getter ya que property lo usa como si fuera una propiedad
'''

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def temperature(self):
        print("Obteniendo valor...")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            print("La temperatura por debajo de -273° no es posible")
        else:
            print("Asignando valor...")
            self.__temperature = value
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

# creamos un objeto
human = Celsius(37)
print(human.temperature)
human.temperature = 42
print(human.__dict__)

print(human.to_fahrenheit())
human.temperature = 12
print(human.__dict__)
