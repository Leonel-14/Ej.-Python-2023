'''
Las tuplas se utilizan para almacenar varios elementos en una sola variable.
Una tupla es una colección ordenada e inmutable .
Las tuplas se escriben con parentesis.
'''
#--------------------------------tupla = ("uno","dos","tres")

'''
Elementos de tupla
Los elementos de tupla están ordenados, no se pueden modificar y permiten valores duplicados.
Los elementos de tupla están indexados, el primer elemento tiene índice [0], el segundo elemento tiene índice, [1]etc.

Ordenado
Cuando decimos que las tuplas están ordenadas, significa que los elementos tienen un orden definido y ese orden no cambiará.

inmutable
Las tuplas no se pueden cambiar, lo que significa que no podemos cambiar, agregar o eliminar elementos después de que se haya creado la tupla.

Permitir duplicados
Dado que las tuplas están indexadas, pueden tener elementos con el mismo valor

Longitud de la tupla
Para determinar cuántos elementos tiene una tupla, use len()

Acceder a elementos de tupla
Puede acceder a los elementos de la tupla consultando el número de índice, entre corchetes:

print(tupla[0])

Indexación negativa -> igual que la lista
Gama de índices -> igual que la lista
Rango de índices negativos -> igual que la lista
Comprobar si el artículo existe -> igual que la lista
'''
#Cambiar valores de tupla
#-Una vez que se crea una tupla, no puede cambiar sus valores. Las tuplas son inmutables , o inmutables como también se le llama.
#-Pero hay una solución. Puede convertir la tupla en una lista, cambiar la lista y volver a convertir la lista en una tupla.

#--------------------------------tupla = (1,2,3)
#--------------------------------tupla = list(tupla)
#--------------------------------tupla.append(4)
#--------------------------------tupla = tuple(tupla)
#--------------------------------print(tupla)

#Agregar elementos
#-Dado que las tuplas son inmutables, no tienen un método integrado append(), pero existen otras formas de agregar elementos a una tupla.
#-Puede convertirla en una lista, agregar sus elementos y volver a convertirla en una tupla.

#Eliminar elementos
#-No puede eliminar elementos en una tupla.
#-Las tuplas no se pueden modificar , por lo que no puede eliminar elementos, pero puede usar la misma solución alternativa

#La palabra 'del' puede eliminar la tupla por completo

#Desempaquetando una tupla

#-Cuando creamos una tupla, normalmente le asignamos valores. Esto se llama "empaquetar" una tupla:
#fruits = ("apple", "banana", "cherry")

#Pero, en Python, también podemos volver a extraer los valores en variables. Esto se llama "desempacar":

#----------Empaquetando--------tupla = ("uno","dos","tres")
#----------Desempaquetando-----(objeto1,objeto2,objeto3) = tupla
#------------------------------print(objeto1)
#------------------------------print(objeto2)
#------------------------------print(objeto3)

#Usando asterisco*
#-Si el número de variables es menor que el número de valores, 
#-puede agregar un * al nombre de la variable y los valores se asignarán a la variable como una lista

#----------Empaquetando--------tupla = ("una","dos","tres","cuatro")
#----------Desempaquetando-----(obj1,obj2,*obj3) = tupla
#------------------------------print(obj1)
#------------------------------print(obj2)
#------------------------------print(obj3)

#-Si el asterisco se agrega a otro nombre de variable que no sea el último, 
#-Python asignará valores a la variable hasta que la cantidad de valores restantes coincida con la cantidad de variables restantes.


#----------Empaquetando--------tupla = ("una","dos","tres","cuatro")
#----------Desempaquetando-----(obj1,*obj2,obj3) = tupla
#------------------------------print(obj1)
#------------------------------print(obj2)
#------------------------------print(obj3)

# Se puede recorrer la tupla con un for o while, como en las listas

#Unir tuplas

'''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

'''

#Multiplicar tuplas

'''
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
'''




