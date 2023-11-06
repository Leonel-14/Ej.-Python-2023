'''
import matplotlib.pyplot as plt
from numpy import arange,sin,pi



x = arange(0.0,10*pi,0.1)
y = sin(x)

plt.plot(x, y, color='black',linewidth = 2)
plt.xlabel("Longitud")
plt.ylabel("Amplitud")
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)


plt.show()

'''
#agregue un metodo estatico para que me de la fecha actual, asi la llamo y no la tengo que codear cada vez que tenga que mostrar una fecha
from datetime import datetime

def fecha():
        formato_fecha = "%H:%M:%S %d-%m-%Y" 
        fecha = datetime.now()
        fecha_actual = fecha.strftime(formato_fecha)
        return fecha_actual

print(fecha())