'''
Escribir un programa en Python que pida al usuario que ingrese las medidas de la base y la altura de un rectángulo y muestre:

1.El perímetro del rectángulo
2.El área del rectángulo
'''

base = int(input("Ingrese base: "))
altura = int(input("Ingrese altura: "))

perimetro = 2*(base+altura)
area = base*altura

print(f"Perimetro: {perimetro}\nArea: {area}")