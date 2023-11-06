class clase():
    atributo_clase = 0

    def __init__(self,valor) -> None:
        self.matar = valor

    def metodo(self):
        self.matar += 10

obj = clase(20)
print(obj.atributo_clase)

