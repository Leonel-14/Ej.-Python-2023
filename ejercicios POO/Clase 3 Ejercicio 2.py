#Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos 
#expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

def funcion(hora,minutos,segundos):
    segundos_totales = (hora*3600) + (minutos*60) + segundos
    return segundos_totales

def conversor(total_segundos,Hora_Min_Seg):
     Hora_Min_Seg.append(int(total_segundos / 60) // 60)
     Hora_Min_Seg.append(int(total_segundos / 60) % 60)
     Hora_Min_Seg.append(int(total_segundos % 60)) 

total_segundos = 0

for x in range(1,3):
    hora = int(input(f"{x}° Ingreso horas: "))
    minutos = int(input(f"{x}° Ingreso minutos: "))
    segundos = int(input(f"{x}° Ingreso segundos: "))

    total_segundos += funcion(hora,minutos,segundos)

Hora_Min_Seg = []
conversor(total_segundos,Hora_Min_Seg)

print(f"{Hora_Min_Seg[0]} Horas - {Hora_Min_Seg[1]} Minutos - {Hora_Min_Seg[2]} Segundos")