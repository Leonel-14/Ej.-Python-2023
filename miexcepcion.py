class MiError(ValueError):
    def __init__(self,valor):
        self.valor = valor
        self.mensaje = "Error: Imposible añadir elementos duplicados"

    def __str__(self) -> str:
        return f"{self.mensaje} => {[self.valor]}"
    
def agregar_una_vez(lista, elem):
        try:
            if elem in lista:
                raise MiError(elem)
            else:
                lista.append(elem)
                print(f"Valor: {[elem]} => agregado")
        except MiError as e:
                print(e)

if __name__ == "__main__":
    lista = [1,5,-2]
    agregar_una_vez(lista,10)
    agregar_una_vez(lista,-2)
    agregar_una_vez(lista,"Hola")

