import math 

class clase():

    __pi = 3.14

    @classmethod
    def funcion(cls,radio):
        cls.__pi = cls.__pi * math.pow(radio,2)
        return cls.__pi
        


obj = clase()
print(obj.funcion(3))

