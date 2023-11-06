class personaje():
    
    def __init__(self,nombre,vida,tipo):
        self.nombre = nombre
        self.vida = int(vida)
        self.tipo = tipo

p1 = personaje("Arturo",100,"Caballero")

print(p1.nombre,p1.vida,p1.tipo)

