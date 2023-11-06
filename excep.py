'''
class mio(Exception):
    def __init__(self) -> None:
        self.mensaje = "No cero"

    def __str__(self) -> str:
        return self.mensaje
    
def divison(a,b):
    if b != 0:
        return a / b
    else:
        raise mio()

try:
    print(divison(10,0))
except mio as e:
    print(e)

'''

from datetime import datetime

#agregue un metodo estatico para que me de la fecha actual, asi la llamo y no la tengo que codear cada vez que tenga que mostrar una fecha
def fecha():
    formato_fecha = "%Y-%m-%d %H:%M:%S" 
    fecha = datetime.now()
    fecha_actual = fecha.strftime(formato_fecha)
    return fecha_actual


def mostrar():
    hora = fecha()
    return hora

print(mostrar())