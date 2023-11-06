'''
Escribe un programa en Python que solicite 5 números enteros al usuario. El mismo debe indicar si
entre dichos valores hay números duplicados o no, imprimiendo por pantalla “HAY DUPLICADOS” o “SON TODOS DISTINTOS”.
'''

lista = []
for i in range(5):
    lista.append(int(input("Ingrese numero: ")))

flag = 0

for x in range(len(lista)-1):
    for j in range(x+1,len(lista)):
        if(lista[x] == lista[j]):
            flag = 1
            break

if flag == 1:
    print("Hay duplicados")

else:
    print("Son todos distintos")
