#Las listas se utilizan para almacenar varios elementos en una sola variable.

#--------------------------------lista = ["algo1","algo2","algo3"]
#--------------------------------print(lista)

#Se puede almacenar diferentes tipos de datos en una lista

#--------------------------------lista2 = ["algo1",3,False]
#--------------------------------print(lista2)

'''
-Los elementos de la lista están ordenados, se pueden cambiar y permiten valores duplicados.
-Los elementos de la lista están indexados, el primer elemento tiene índice [0], el segundo elemento tiene índice, [1]etc.
-Cuando decimos que las listas están ordenadas, significa que los elementos tienen un orden definido y ese orden no cambiará.
-Si agrega nuevos elementos a una lista, los nuevos elementos se colocarán al final de la lista.
-La lista se puede cambiar, lo que significa que podemos cambiar, agregar y eliminar elementos en una lista después de que se haya creado.
'''

#Para saber cuántos elementos tiene una lista, use la len()función:

#--------------------------------print(len(lista2))

#tipo

#--------------------------------print(type(lista2))

#usando el constructor list()
#lista = ["algo1","algo2","algo3"]  == lista = list(("algo1","algo2","algo3"))

#Acceso de listas
#--------------------------------print(lista[0])
#La indexación negativa significa comenzar desde el final.
#-1se refiere al último elemento, -2se refiere al penúltimo elemento, etc.
#--------------------------------print(lista[-3])

#Gama de índices
#Puede especificar un rango de índices especificando dónde comenzar y dónde terminar el rango.
#Al especificar un rango, el valor devuelto será una nueva lista con los elementos especificados.

#--------------------------------lista = [1,2,3,4,5,6,7,8,"algo"]
#muestra desde el indice 1 hasta 6-1 osea el 6 y no el 7
#lista[1] = 2
#lista[2] = 3
#lista[3] = 4
#lista[4] = 5
#lista[5] = 6
#--------------------------------print(lista[1:6])

#Al omitir el valor inicial, el rango comenzará en el primer elemento:
#--------------------------------print(lista[:6])

#Rango de índices negativos
#Especifique índices negativos si desea iniciar la búsqueda desde el final de la lista:
#--------------------------------print(lista[-8:-3])

#Comprobar si el elemento existe
#Para determinar si un elemento específico está presente en una lista, use la 'in' palabra clave:

#--------------------------------lista = [1,2,3,4,5,6,7,8,"algo"]

#--------------------------------if "algo" in lista:
#-----------------------------------print("Si esta")

#-Cambiar el valor del artículo
#-Para cambiar el valor de un elemento específico, consulte el número de índice:

#--------------------------------lista = [1,2,3,4,5]
#--------------------------------lista[1] = 10
#--------------------------------print(lista)

#Para cambiar el valor de los elementos dentro de un rango específico,
#defina una lista con los nuevos valores y consulte el rango de números de índice donde desea insertar los nuevos valores:

#--------------------------------lista[1:4] = ["hola","hola2","hola3"]
#--------------------------------print(lista)

#Insertar elementos
#-Para insertar un nuevo elemento de lista, sin reemplazar ninguno de los valores existentes, podemos usar el insert()método.
#-El insert()método inserta un elemento en el índice especificado:

#--------------------------------lista = [1,2,3,4,5,6]
#--------------------------------lista.insert(2,"algo")
#--------------------------------print(lista)

#-Para agregar un elemento al final de la lista, use el método append() :
#--------------------------------lista.append("algofinal")
#--------------------------------print(lista)

#Ampliar lista
#-Para agregar elementos de otra lista a la lista actual, use el extend()método.
#--------------------------------lista2 = ["ama","tera","su"]
#--------------------------------lista.extend(lista2)
#--------------------------------print(lista)

#-tambien se puede agregar cualquier objeto iterable (tuplas, conjuntos, diccionarios, etc.)
#--------------------------------tupla = ("t1","t2","t3")
#--------------------------------.extend(tupla)
#--------------------------------print(lista2)

#Eliminar elemento especificado
#-El remove()método elimina el elemento especificado.

#--------------------------------lista = [1,2,3,4,5]
#--------------------------------.remove(2)
#--------------------------------print(lista)

#Eliminar índice especificado
#-El pop()método elimina el índice especificado.
#--------------------------------lista.pop(2)
#--------------------------------print(lista)

#-Si no especifica el índice, el pop()método elimina el último elemento.
#--------------------------------.pop()
#--------------------------------print(lista)

#-La palabra 'del' también elimina el índice especificado:
#--------------------------------del lista[1]
#--------------------------------print(lista)

#-La palabra 'del' también puede eliminar la lista por completo.
#-------------------------------- lista = [10,20,30]
#-------------------------------- del lista2
#-------------------------------- print(lista2) #dara error porque no existe lista2

#Baciar lista
#-El método clear() vacía la lista.
#-La lista aún permanece, pero no tiene contenido.
#--------------------------------lista = [11,22,33]
#--------------------------------lista.clear()
#--------------------------------print(lista)

#Recorrer una lista
#-Puede recorrer los elementos de la lista usando un for bucle:

#--------------------------------lista = ["uno","dos","tres","cuatro"]

#--------------------------------for x in lista:
#--------------------------------    print(x)

#Bucle a través de los números de índice
#-También puede recorrer los elementos de la lista consultando su número de índice.
#-Utilice las funciones range()y len()para crear un iterable adecuado.

#--------------------------------lista = ["uno","dos","tres"]
#--------------------------------print(len(lista))

#--------------------------------for i in range(len(lista)):
#--------------------------------  print(lista[i])

#Lista de comprensión
#-La comprensión de listas ofrece una sintaxis más corta cuando desea crear una nueva lista basada en los valores de una lista existente.
#-Ejemplo:
#-Basado en una lista de frutas, desea una nueva lista que contenga solo las frutas que contengan al menos una letra "a" en el nombre.
#-Sin comprensión de lista, tendrá que escribir una fordeclaración con una prueba condicional dentro:
#--------------------------------lista_frutas = ['manzana', 'plátano', 'naranja', 'uva', 'sandía', 'piña', 'mango', 'fresa', 'kiwi', 'melón','tomate']
#--------------------------------lista_frutas_a = []
#--------------------------------for x in lista_frutas:
#--------------------------------    if "m" in x:
#--------------------------------        lista_frutas_a.append(x)

#--------------------------------print(lista_frutas_a)

#Ordenar lista alfanuméricamente
#-Los objetos de lista tienen la palabra sort() ordenará la lista de forma alfanumérica, ascendente, de forma predeterminada:

#--------------------------------lista = ["uno","dos","tres"]
#--------------------------------lista.sort()
#--------------------------------print(lista)

#--------------------------------lista2 = [100,99,2,23]
#--------------------------------lista2.sort()
#--------------------------------print(lista2)

#Orden descendiente
#-Para ordenar de forma descendente, use el argumento de palabra clave es reverse = True:

#--------------------------------lista.sort(reverse=True)
#--------------------------------print(lista)
#--------------------------------lista2.sort(reverse=True)
#--------------------------------(lista2)

#Clasificación insensible a mayúsculas y minúsculas
#-De forma predeterminada, el sort() distingue entre mayúsculas y minúsculas,
#lo que da como resultado que todas las letras mayúsculas se clasifiquen antes que las minúsculas:

#--------------------------------lista = ["minuscula","Mayuscula"]
#--------------------------------lista.sort()
#--------------------------------print(lista)

#Orden inverso
#-El reverse() invierte el orden de clasificación actual de los elementos.

#--------------------------------lista2 = ["uno","dos","tres"]
#--------------------------------lista2.reverse()
#--------------------------------print(lista2)

#Copiar una lista
#-No puede copiar una lista simplemente escribiendo list2 = list1, porque: list2 
# solo será una referencia a list1, y los cambios realizados en list1automáticamente también se realizarán en list2.
#-Hay formas de hacer una copia, una forma es usar el método List incorporado copy().

#--------------------------------lista = ["uno","dos","tres"]
#--------------------------------lista2 = lista.copy()
#--------------------------------print(lista2)


#Unirse dos listas
#-Hay varias formas de unir o concatenar dos o más listas en Python.
#-Una de las formas más fáciles es usando el + operador.

lista = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = lista + lista2
print(lista3)

'''
append() Agrega un elemento al final de la lista
clear() Elimina todos los elementos de la lista
copy() Devuelve una copia de la lista
count() Devuelve el número de elementos con el valor especificado
extend () Agrega los elementos de una lista (o cualquier iterable), al final de la lista actual
index() Devuelve el índice del primer elemento con el valor especificado
insert() Agrega un elemento en la posición especificada
pop() Elimina el elemento en la posición especificada
remove() Elimina el elemento con el valor especificado
reverse() Invierte el orden de la lista
sort() Ordena la lista
'''
