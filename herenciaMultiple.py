class Animal():
    def __init__(self,tipo):
        self.tipo = tipo

class Cuadrupedo():
    def __init__(self,nombre):
        self.nombre = nombre

class Gato(Animal,Cuadrupedo):
    def __init__(self, tipo):
        super().__init__(tipo)