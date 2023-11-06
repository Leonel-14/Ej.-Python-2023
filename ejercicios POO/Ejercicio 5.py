'''
Crear una clase llamada ListaDeTareas con los siguientes atributos y métodos:
• Atributo de instancia privado “lista_tareas” de tipo list.
• Método de instancia público “agregarTarea(tarea)”, que recibe como argumento
una tarea que debe ser agregada a la lista de tareas (atributo “lista_tareas”) y
retorna el string “Tarea agregada correctamente a la lista” ó “La tarea no fue
agregada a la lista” en caso que la tarea se haya agregado o no a la lista
respectivamente.
• Método de instancia público “quitarTarea(tarea)”, que recibe como argumento una
tarea que debe ser eliminada de la lista de tareas (atributo “lista_tareas”) y retorna
el string “Tarea eliminada correctamente de la lista” ó “La tarea no fue eliminada de
la lista” en caso que la tarea se haya eliminado o no de la lista respectivamente.
• Método de instancia público “mostrarTareas()”, que no recibe ningún argumento y
retorna la lista de tareas (atributo “lista_tareas”) .
Luego, se debe crear una instancia de ListaDeTareas, agregar tareas a la lista, eliminar
tareas de la lista y finalmente imprimir la lista completa de tareas.
Nota: el método “quitarTarea(tarea)” debe validar si la tarea a eliminar existe en la lista
antes de ser eliminada.
'''

class ListaDeTareas():
    def __init__(self,lista_tareas):
        self.__lista_tareas = lista_tareas

    def agregarTarea(self,tarea):
        if tarea.isalpha():
            self.__lista_tareas.append(tarea)
            retorno = "Se agrego la tarea"
        else:
            retorno = "No se agrego tarea"
        return retorno

    def quitarTarea(self,tarea):
        
        for x in range(0,len(self.__lista_tareas)):
            if(self.__lista_tareas[x] == tarea):
                retorno = "Tarea eliminada correctamente de la lista"
                break
            else:
                retorno = "La tarea no fue eliminada de la lista"
        return retorno
    
    def mostrarTareas(self):
        print(self.__lista_tareas)
                    

lista = []
A1 = ListaDeTareas(lista)
i = int(input("Cuantas tareas ingresara: "))
for x in range(0,i):
    print(A1.agregarTarea(input("Ingrese tarea: ")))

A1.mostrarTareas()
print(A1.quitarTarea(input("Que tarea desea eliminar: ")))

'''
lista = [10,20,30]
x = 33
if x in lista:
    print("si esta")
else:
    print("No esta")

La x busca dentro de la lista con 'in'
'''







