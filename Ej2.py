'''
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda
'''
class Agenda():
    def __init__(self,lista):
        self.lista = lista

    def añadir(self,nombre,numero):
        self.lista.append([nombre,numero])

    def listado(self):
        for x in self.lista:
            print(x)
    
    def buscar(self,buscado):
        retorno = "No encontrado"
        for x in self.lista:
                if x[0] == buscado:
                     retorno = "Encontrado"
                     print(x)
                     break
        return retorno
    
    def editarC(self):
         n = -1
         for x in self.lista:
            n += 1
            print(n,x)
         
         indice = int(input("Que quiere editar: "))
         nombre = input("Ingrese nuevo nombre: ")
         numero = int(input("Ingrese nuevo numero: "))

         lista[indice] = [nombre,numero]

    def fin(self):
         print("Fin del programa")

    def menu(self):
         print("### - MENU - ###")
         print("1) Añadir contacto")
         print("2) Lista de contactos")
         print("3) Buscar contacto")
         print("4) Editar contacto")
         print("5) Cerrar agenda")

         opcion = int(input("Ingrese opcion: "))
         return opcion


         
 

                
        
lista = [["Leonel",1126393433],["Mariela",1133343926]]
obj = Agenda(lista)

salida = 's'

while salida == 's':
    match obj.menu():
        case 1:
            nombre = input("Ingrese Nombre: ")
            numero = int(input("Ingrese Numero: "))
            obj.añadir(nombre,numero)
        case 2:
            obj.listado()
        case 3:
            print(obj.buscar("Leonel"))
        case 4:
            obj.editarC()
        case 5:
            obj.fin()
            salida = 'n'


'''
def algo(lista):
    print(lista[1])

lista = [["Leonel",1126393433],["Mariela",1133343926]]
algo(lista)



lista = [[10,11,12],[20,21,22],[30,31,32]]

indice = int(input("Indice: "))
nombre = input("Nombre: ")
numero = int(input("Numero: "))

lista[indice] = [nombre,numero]

print(lista)
'''



