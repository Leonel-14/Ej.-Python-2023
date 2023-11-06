class Padre():
    def __init__(self,saldo,valor) -> None:
        self.__saldo = saldo
        self.__otro = valor
        self.__mov = []

    @property
    def consultar_saldo(self):
        return self.__saldo
    
    @consultar_saldo.setter
    def consultar_saldo(self,valor):
        self.__saldo = valor

    @property
    def otro(self):
        return self.__otro
    
    @otro.setter
    def otro(self,valor):
        self.__otro = valor

    @property
    def movimiento(self):
        return self.__mov
    
    
class Hijo(Padre):
    def __init__(self, saldo,valor) -> None:
        super().__init__(saldo,valor)
        self.__kaka = 100

    def extraer(self,monto):
        if monto <= self.consultar_saldo:
            self.consultar_saldo -= monto
            self.movimiento.append("hola")
    
    @property
    def kaka(self):
        return self.__kaka

    def mostrar(self):
        print(f"Saldo {self.consultar_saldo}")
        print(f"Otro: {self.otro}")
        print(f"Movimiento :{self.movimiento}")
        print(f"kaka :{self.kaka}")
    
hj = Hijo(100,4)
hj.extraer(10)
hj.mostrar()



    