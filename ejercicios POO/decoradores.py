def nuevo_decorador(a_func):
    def envuelveLaFuncion():
        print("Algo1") #nueva funcionalidad
        a_func() #llamada a la la funcion que quiero decorar
        print("Algo3") #nueva funcionalidad
    return envuelveLaFuncion  #retorna estas nuevas modificaciones
  
@nuevo_decorador  #declarar arriba de la funcion que quiero darle la decoracion
def funcion_a_decorar():
    print("algo2")
  
funcion_a_decorar() #llamar a la funcion normal

