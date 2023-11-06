from abc import ABC, abstractclassmethod
import math

class FiguraGeometrica(ABC):
   
    def __init__(self,color_fondo:str,color_borde:str):
        self.__color_fondo = color_fondo
        self.__color_borde = color_borde

    @property
    def color_fondo(self):
        return self.__color_fondo
    
    @color_fondo.setter
    def color_fondo(self,valor:str):

        while not isinstance(valor,str):
            valor = input("Error. Ingrese un valor valido: ")
        
        self.__color_fondo = valor

    @property
    def color_borde(self):
        return self.__color_borde
    
    @color_borde.setter
    def color_borde(self,valor:str):

        while not isinstance(valor,str):
            valor = input("Error. Ingrese un valor valido: ")
        
        self.__color_borde = valor

    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):
     
    def __init__(self,color_fondo:str,color_borde:str,base:float,altura:float):
        super().__init__(color_fondo,color_borde)
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self,valor:float):
        while not isinstance(valor,int):
            valor = input("Error. Ingrese un valor valido: ")
        
        self.__base = valor

    @property
    def altura(self):
        return self.__base
    
    @altura.setter
    def altura(self,valor:float):
        while not isinstance(valor,float):
            valor = input("Error. Ingrese un valor valido: ")
        
        self.__altura = valor

    def area(self):
        return self.__altura * self.__base

    def perimetro(self):
        return math.pow(self.__altura,2) + math.pow(self.__base,2)

class Circulo(FiguraGeometrica):
    def __init__(self, color_fondo:str, color_borde:str,radio:float):
        super().__init__(color_fondo, color_borde)
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self,valor:float):
        while not isinstance(valor,float):
            valor = input("Error. Ingrese un valor valido: ")
        self.__radio = valor
    
    def area(self):
        return 2*3.14*pow(self.__radio,2)
    
    def perimetro(self):
        return 2*3.14*self.__radio

class Triangulo(FiguraGeometrica):
    def __init__(self, color_fondo:str, color_borde:str,base:float,altura:float):
        super().__init__(color_fondo, color_borde)
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self,valor):
        while not isinstance(valor,float):
            valor = input("Error. Ingrese un valor valido: ")
        
        self.__base = valor

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self,valor):
        while not isinstance(valor,float):
            valor = input("Error. Ingrese un valor valido: ")
        
        self.__altura = valor

    def area(self):
        return self.__base*self.__altura

    def perimetro(self):
        return 3*self.__base

    
if __name__ == "__main__":
    r_1 = Rectangulo("Verde","Negro",10,15)
    r_2 = Rectangulo("Rojo","Negro",17,12)
    c_1 = Circulo("Amarillo","Celeste",5)
    c_2 = Circulo("Amarillo","Celeste",9)
    t_1 = Triangulo("Violeta","Naranja",10,50)
    t_2 = Triangulo("Azul","Marron",11,40)

    lista = [r_1,r_2,c_1,c_2,t_1,t_2]

    for x in lista:
        print(f"De la clase: {type(x)} | Su area es: {x.area()} | Su perimetro: {x.perimetro()}")

        