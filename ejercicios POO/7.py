import random

class Password:
    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    #se declaran dos atributos de clase privados
    #__LONGITUD sera usado como valor por defecto
    #__CARACTERES_VALIDOS sera usado como posibilidades para una constraseña
    
    def __init__(self,longitud):

        self.__longitud = Password.__LONGITUD
        if longitud > 5 and longitud < 16:
            self.__longitud = longitud 
        self.__contraseña = self.generadorPassword()
    #metodo constructor que recibira la longitud que quiera el usuario
    #por defecto sera de 8, pero en caso de que quiera mas o menos se lo habilitara
    #declaraciones de dos atributos de instancia privados
    #self.__contraseña 

    @property
    def get_longitud(self):
        return self.__longitud
    
    @get_longitud.setter
    def setter_longitud(self,longitud):
        self.__longitud = longitud

    @property
    def get_contraseña(self):
        return self.__contraseña
    
    @get_contraseña.setter
    def setter_contraseña(self,contraseña):
        self.__contraseña = contraseña

    def esFuerte(self):
        mayus = 0
        minus = 0
        numero = 0
        carac_esp = 0
        retorno = False
        for x in range(len(self.__contraseña)):
            if self.__contraseña[x].isupper():
                mayus += 1
            elif self.__contraseña[x].islower():
                minus += 1
            elif self.__contraseña[x].isdigit():
                numero += 1
            elif self.__contraseña[x] == '<' or self.__contraseña[x] == '=' or self.__contraseña[x] == '>' or self.__contraseña[x] == '@' or self.__contraseña[x] == '#' or self.__contraseña[x] == '%' or self.__contraseña[x] == '&' or self.__contraseña[x] == '+':
                carac_esp += 1
        
        if mayus > 1 and minus > 1 and numero > 1 and carac_esp > 1:
            retorno = True

        return retorno
        

    def generadorPassword(self):
        contra = ""
        for x in range(self.__longitud):
            contra += random.choice(Password.__CARACTERES_VALIDOS)

        return contra

    def __str__(self):
        retorno = self.__contraseña +" "+ str(self.esFuerte())
        return retorno
    

if __name__ == '__main__':

    lista_contraseña = []

    for x in range(5):
        valor = int(input("Ingrese longitud: "))
        objeto = Password(valor)
        lista_contraseña.append(objeto)


    print("##########CONTRASEÑAS##########")

    for x in range(5):
        print(lista_contraseña[x].__str__())

