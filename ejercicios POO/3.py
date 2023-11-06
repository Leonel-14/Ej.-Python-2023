'''
Escribe un programa en Python que solicite al usuario que ingrese 5 números enteros. Luego imprimir el máximo y el mínimo
de los valores ingresados. El programa deberá permitir el ingreso de valores iguales.
'''

lista = []
for i in range(5):
    lista.append(int(input("Ingrese numero: ")))


print(f"Numero maximo: {max(lista)}\nNumero minimo: {min(lista)}")


