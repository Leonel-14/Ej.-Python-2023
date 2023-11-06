#Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.

def funcion(hora,minutos,segundos):
    segundos_totales = ((hora*60)*60) + (minutos*60) + segundos
    return segundos_totales

total_segundos = funcion(1,40,30)

print("Total Segundos: ",total_segundos)