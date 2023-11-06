from abc import ABC
from abc import abstracmethod
from datetime import datetime

class CuentaBancaria(ABC):
    def __init__(self,nro_cuenta:str,cbu:str,alias:str,saldo:float,movimientos:list):
        self.nro_cuenta = nro_cuenta
        self.cbu = cbu
        self.alias = alias
        self.saldo = saldo
        self.movimientos = movimientos

    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self,monto_a_depositar:float):
        retorno = False
        self.monto_a_depositar = monto_a_depositar
        if monto_a_depositar > 0:
            self.saldo += self.monto_a_depositar
            fecha = fecha()
            tupla = (f"Hora registrada:{fecha} Monto Depositado:{self.monto_a_depositar} Saldo Actual{self.saldo}") 
            self.movimientos.append(tupla)
            retorno = True
        return retorno
    
    @abstracmethod
    def extraer(self,monto_a_extraer:float):
        self.monto_a_extraer = monto_a_extraer
        retorno = False
        if self.saldo - self.monto_a_extraer >= 0:
            retorno = True
            self.saldo -= self.monto_a_extraer
            fecha = fecha()
            tupla = (f"Hora registrada:{fecha} Monto Depositado:{self.monto_a_depositar} Saldo Actual{self.saldo}")
            self.movimientos.append(tupla)

        return retorno
    
    @abstracmethod
    def transferir(self,monto_a_transferir:float,cuenta_destino:"CuentaBancaria"):
        self.saldo = monto_a_transferir
        retorno = False
        if self.saldo> 0:
            retorno = True
            self.saldo -= self.monto_a_extraer
            fecha = fecha()
            tupla = (f"Hora registrada:{fecha} Monto Depositado:{self.monto_a_depositar} Saldo Actual{self.saldo}")
            self.movimientos.append(tupla)

        return retorno

    #agregue un metodo estatico para que me de la fecha actual, asi la llamo y no la tengo que codear cada vez que tenga que mostrar una fecha
    @staticmethod
    def fecha():
        formato_fecha = "%Y-%m-%d %H:%M:%S" 
        fecha = datetime.now()
        fecha_actual = fecha.strftime(formato_fecha)
        return fecha_actual
        

    
            


class CajaDeAhorro(CuentaBancaria):
    pass

class CuentaCorriente(CuentaBancaria):
    pass

class Cliente():
    def __init__(self):
        self.lista_cuenta_bancaria
        
class Banco():
    def __init__(self):
        self.lista_cliente

obj = CuentaBancaria("1408","hxe087d1","leonel.loz",100)

print(obj.monto_a_depositar(250))