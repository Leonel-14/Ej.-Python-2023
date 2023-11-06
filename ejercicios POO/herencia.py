class padre():
    def idiota(valor):
        print("idiota ",valor)

class hija(padre):
    pass

obj = hija

obj.idiota("Salame")
