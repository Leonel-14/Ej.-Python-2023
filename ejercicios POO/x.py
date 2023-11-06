'''
lista = [10,20,30]
x = 33
if x in lista:
    print("si esta")
else:
    print("No esta")
'''
'''
class algo:
    algos = "d"


c1 = algo()

print(c1.algos)
print(algo.algos)

'''
'''
import random
class algo():
    vocales = "aeiou"
    def __init__(self,longitud):
        self.long = longitud

    def generadorContra(self):
        self.contra = ""
        for x in range(self.long):
            self.contra += random.choice(algo.vocales)

        print(self.contra)

c1 = algo(4)
c1.generadorContra()
'''


class temperatura():
    def __init__(self,value = 0) -> None:
        self.celsius = value

    @property
    def celsius(self):
        print("Obteniendo valor...")    
        return self.__value
    
    @celsius.setter
    def celsius(self,value):
        if value > 0:
            print("Asignando valor...")
            self.__value = value
        else:
            print("No es posible")

obj = temperatura(50)
print(obj.celsius)
    