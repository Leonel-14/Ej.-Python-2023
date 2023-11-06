class MiClase:
    
    @staticmethod
    def metodo_estatico(x, y):
        return x + y


# Llamar al método estático en la clase misma (no en la instancia)
resultado = MiClase.metodo_estatico(10, 20)
print(resultado)  # Salida: 30
'''
En este ejemplo, metodo_estatico es un método estático que no recibe automáticamente una referencia a la instancia o a la clase. 
Puedes llamar a este método en la clase misma sin crear una instancia de la clase, y simplemente realiza una operación matemática simple.
Algunos casos comunes de uso de @staticmethod incluyen la encapsulación de funciones que están relacionadas con la clase pero no necesitan acceso a atributos de instancia o de clase específicos. 
Los métodos estáticos son útiles cuando deseas organizar tu código y mantenerlo dentro de la clase por razones de diseño, aunque la funcionalidad no dependa directamente de la instancia o de la clase.
'''




