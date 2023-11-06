'''
Crea una clase abstracta llamada "Figura" que tenga un método abstracto llamado "area".
Luego, crea dos clases concretas llamadas "Rectangulo" y "Circulo" que hereden de la clase "Figura" 
y que implementen el método "area" de manera adecuada para calcular el área de un rectángulo y un círculo respectivamente.
Luego, crea instancias de ambas clases y muestra el área de cada figura.
'''
from abc import abstractmethod
from abc import ABC

class Figura(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangulo(Figura):
    def area(self,base,altura):
        return base*altura


class Circulo(Figura):
    def area(self,radio):
        pi = 3.14
        return pi * radio*radio
    

rectangulo = Rectangulo()
circulo = Circulo()

print(rectangulo.area(10,25))
print(circulo.area(4))


