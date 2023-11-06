#Los conjuntos se utilizan para almacenar varios elementos en una sola variable.

#Un conjunto es una colección desordenada , inmutable * y no indexada .
#Los elementos establecidos no se pueden modificar, pero puede eliminar elementos y agregar elementos nuevos.

#--------------------------------conjunto = {"uno","dos","tres"}
#--------------------------------print(conjunto)

#Los conjuntos no están ordenados, por lo que no puede estar seguro en qué orden aparecerán los elementos.

'''
Establecer elementos
Los elementos establecidos no están ordenados, no se pueden modificar y no permiten valores duplicados.

Desordenado
Desordenado significa que los elementos de un conjunto no tienen un orden definido.

Los elementos establecidos pueden aparecer en un orden diferente cada vez que los usa y no se puede hacer referencia a ellos por índice o clave.

Inmutable
Los elementos del conjunto no se pueden cambiar, lo que significa que no podemos cambiar los elementos después de que se haya creado el conjunto.
'''

'''
No se permiten duplicados
Los conjuntos no pueden tener dos artículos con el mismo valor.

Ejemplo
Los valores duplicados serán ignorados:

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

Los valores True y 1 se consideran el mismo valor en conjuntos y se tratan como duplicados:
-
Longitud de conjunto
len(conjunto)
-
el tipo de dato de un conjunto se llama 'set'
-
Elementos de acceso
No puede acceder a los elementos de un conjunto haciendo referencia a un índice o una clave.

Pero puede recorrer los elementos del conjunto usando un for bucle, o preguntar si un valor específico está presente en un conjunto, 
usando in.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

-
Una vez que se crea un conjunto, no puede cambiar sus elementos, pero puede agregar nuevos elementos.

Para agregar un elemento a un conjunto, utilice el add() método.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
-
Agregar conjuntos
Para agregar elementos de otro conjunto al conjunto actual, utilice el update() método.

Ejemplo
Añadir elementos de tropical en thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

tambien se puede agregar una lista

-
Estas funciones aplican tambien para eliminacion
.remove()
Del
.clear()
.pop()
.discard()
-
Bucle con for
-

'''

