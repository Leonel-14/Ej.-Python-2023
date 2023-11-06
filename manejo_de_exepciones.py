'''
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except: #except simple error tipo de dato
        print("Debe ser un valor numerico")


if edad >= 18:
    print("Es mayor de edad")
else:
    print("Aun no es mayor")
'''

'''
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except Exception as x:
        print("Debe ser un valor numerico")
        print("Error -> ",type(x))
        
        #Ingrese su edad: d
        #Debe ser un valor numerico    
        #Error ->  <class 'ValueError'> 
        #Ingrese su edad: 323
        #Es mayor de edad


if edad >= 18:
    print("Es mayor de edad")
else:
    print("Aun no es mayor")
'''

def mayor_edad(value):
    if value >= 18:
        print("Es mayor de edad")
    else:
        print("Aun no es mayor de edad")
    
while True:
    try:
        edad = int(input("Ingrese edad:"))
        #break
    except ValueError as e: #ya que que el error se llama ValueError | si no se identifica bien el tipo de exception no se ejecuta bien el codigo
        print("Debe ingresar in valor numerico. Error -> ",e)

    else:
        mayor_edad(edad)
        break