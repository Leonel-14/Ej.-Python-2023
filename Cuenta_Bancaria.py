from abc import ABC, abstractmethod
from datetime import datetime

class CuentaBancaria(ABC):
    def __init__(self,nro_cuenta:str,cbu:str,alias:str,saldo:float):
        self.__nro_cuenta = nro_cuenta
        self.__cbu = cbu
        self.__alias = alias
        self.__saldo = saldo
        self.__movimiento = []

    @property
    def nro_cuenta(self):
        return self.__nro_cuenta
    
    @nro_cuenta.setter
    def nro_cuenta(self,valor):
        self.__nro_cuenta = valor

    @property
    def cbu(self):
        return self.__cbu
    
    @cbu.setter
    def cbu(self,valor):
        self.__cbu = valor

    @property
    def alias(self):
        return self.__alias
    
    @alias.setter
    def alias(self,valor):
        self.__alias = valor

    @property
    def consultar_saldo(self):
        return self.__saldo
    
    @consultar_saldo.setter
    def consultar_saldo(self,valor):
        self.__saldo = valor
    
    @property
    def movimiento(self):
        return self.__movimiento
    
    @movimiento.setter
    def movimiento(self,valor):
        self.__movimiento = valor
    
    def depositar(self,monto_a_depositar:float):
        retorno = False
        if monto_a_depositar > 0:
            self.__saldo += monto_a_depositar
            retorno = True
            fecha = self.fecha()
            tupla = (f"Fecha de deposito:{fecha} 'Deposito' Monto:{monto_a_depositar} Saldo:{self.__saldo}")
            self.__movimiento.append(tupla)

        return retorno
    
    @abstractmethod
    def extraer(self,monto_a_extraer:float):
        retorno = False
        if monto_a_extraer <= self.__saldo:
            self.__saldo -= monto_a_extraer
            tupla = (f"Fecha: {self.fecha()} 'Extraccion' Monto: {monto_a_extraer} Saldo: {self.consultar_saldo}")
            self.movimiento.append(tupla)
            retorno = True
        return retorno
    
    @abstractmethod
    def transferir(self,monto_a_transferir:float,cuenta_destino:"CuentaBancaria"):
        retorno = False
        if monto_a_transferir <= self.__saldo:
            self.__saldo -= monto_a_transferir
            tupla = (f"Fecha: {self.fecha()} 'Transferencia' Monto: {monto_a_transferir} Saldo: {self.consultar_saldo}")
            self.movimiento.append(tupla)
            retorno = True

        return retorno

    @staticmethod
    #agregue un metodo estatico para que me de la fecha actual, asi la llamo y no la tengo que codear cada vez que tenga que mostrar una fecha
    def fecha():
        formato_fecha = "%Y-%m-%d %H:%M:%S" 
        fecha = datetime.now()
        fecha_actual = fecha.strftime(formato_fecha)
        return fecha_actual
         
class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta: str, cbu: str, alias: str, saldo: float,monto_limite_extracciones:float,monto_limite_transferencias:float,cant_extracciones_disponibles:int,cant_transferencias_disponibles:int):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.__monto_limite_extracciones = monto_limite_extracciones
        self.__monto_limite_transferencias = monto_limite_transferencias
        self.__cant_extracciones_disponibles = cant_extracciones_disponibles
        self.__cant_transferencias_disponibles = cant_transferencias_disponibles
        
    @property
    def monto_limite_extracciones(self):
        return self.__monto_limite_extracciones
    
    @monto_limite_extracciones.setter
    def monto_limie_extracciones(self,valor):
        self.__monto_limite_extracciones = valor

    @property
    def monto_limite_trasferencias(self):
        return self.__monto_limite_transferencias
    
    @monto_limite_trasferencias.setter
    def monto_limie_transferencias(self,valor):
        self.__monto_limite_transferencias = valor

    @property
    def cant_extracciones_disponibles(self):
        return self.__cant_extracciones_disponibles
    
    @cant_extracciones_disponibles.setter
    def cant_extracciones_disponibles(self,valor):
        self.__cant_extracciones_disponibles = valor

    @property
    def cant_transferencias_disponibles(self):
        return self.__cant_transferencias_disponibles
    
    @cant_transferencias_disponibles.setter
    def cant_transferencias_disponibles(self,valor):
        self.cant_transferencias_disponibles = valor

    def extraer(self, monto_a_extraer: float):
        retorno = False
        if monto_a_extraer > 0 and monto_a_extraer <= self.consultar_saldo and monto_a_extraer < self.__monto_limite_extracciones and self.__cant_extracciones_disponibles > 0:
            self.consultar_saldo -= monto_a_extraer
            self.__cant_extracciones_disponibles -= 1
            tupla = (f"Fecha: {self.fecha()} 'Extraccion' Monto: {monto_a_extraer} Saldo: {self.consultar_saldo}")
            self.movimiento.append(tupla)
            retorno = True

        return retorno
    
    def transferir(self,monto_a_transferir:float,cuenta_destino:"CuentaBancaria"):
        retorno = False
        if monto_a_transferir > 0 and monto_a_transferir <= self.consultar_saldo and monto_a_transferir <= self.__monto_limite_transferencias and self.__cant_transferencias_disponibles > 0:
            self.consultar_saldo -= monto_a_transferir
            cuenta_destino.consultar_saldo += monto_a_transferir
            self.__cant_transferencias_disponibles -= 1
            tupla = (f"Fecha: {self.fecha()} 'Transferencia' Monto: {monto_a_transferir} Saldo: {self.consultar_saldo}")
            self.movimiento.append(tupla)
            retorno = True
        return retorno
    
    def mostrar(self):
        print("Numero de Cuenta: ",self.nro_cuenta)
        print("CBU: ",self.cbu)
        print("Alias: ",self.alias)
        print("Saldo: ",self.consultar_saldo)
        print("Movimiento: ",self.movimiento)
        print("Monto Limite Extracciones: ",self.monto_limie_extracciones)
        print("Monto Limite Transferencias: ",self.monto_limie_transferencias)
        


        

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta: str, cbu: str, alias: str, saldo: float,monto_maximo_descubierto:float):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.__monto_maximo_descubierto = monto_maximo_descubierto

    @property
    def monto_maximo_descubierto(self):
        return self.__monto_maximo_descubierto
    
    @monto_maximo_descubierto.setter
    def monto_maximo_descubierto(self,valor):
        self.__monto_maximo_descubierto = valor
    
    def extraer(self, monto_a_extraer: float):
        retorno = False
        if monto_a_extraer > 0 and monto_a_extraer <= (self.consultar_saldo + self.__monto_maximo_descubierto):
            self.consultar_saldo -= monto_a_extraer
            tupla = (f"Fecha: {self.fecha()} 'Extraccion' Monto: {monto_a_extraer} Saldo: {self.consultar_saldo}")
            self.movimiento.append(tupla)
            retorno = True

        return retorno
    
    def transferir(self,monto_a_transferir:float,cuenta_destino:"CuentaBancaria"):
        retorno = False
        if monto_a_transferir > 0 and monto_a_transferir <= (self.consultar_saldo + self.monto_maximo_descubierto):
            self.consultar_saldo -= monto_a_transferir
            cuenta_destino.consultar_saldo += monto_a_transferir
            tupla = (f"Fecha: {self.fecha()} 'Transferencia' Monto: {monto_a_transferir} Saldo: {self.consultar_saldo}")
            self.movimiento.append(tupla)
            retorno = True
        return retorno
    
    def mostrar(self):
        print("Numero de Cuenta: ",self.nro_cuenta)
        print("CBU: ",self.cbu)
        print("Alias: ",self.alias)
        print("Saldo: ",self.consultar_saldo)
        print("Movimiento: ",self.movimiento)
        print("Monto Maximo Descubierto: ",self.monto_maximo_descubierto)

    


class Cliente():
    def __init__(self,razon_social:str,cuit:str,tipo_persona:str,domicilio:str):
        self.__razon_social = razon_social
        self.__cuit = cuit
        self.__tipo_persona = tipo_persona
        self.__domicilio = domicilio
        self.__cuentas_bancaria = []

    @property
    def razon_social(self):
        return self.__razon_social
    
    @razon_social.setter
    def razon_social(self,valor):
        self.__razon_social = valor

    @property
    def cuit(self):
        return self.__cuit
    
    @cuit.setter
    def razon_social(self,valor):
        self.__cuit = valor

    @property
    def tipo_persona(self):
        return self.__tipo_persona
    
    @tipo_persona.setter
    def tipo_persona(self,valor):
        self.__tipo_persona = valor

    @property
    def domicilio(self):
        return self.__domicilio
    
    @domicilio.setter
    def domicilio(self,valor):
        self.__domicilio = valor

    @property
    def cuentas_bancarias(self):
        return self.__cuentas_bancaria
    
    @cuentas_bancarias.setter
    def cuentas_bancarias(self,valor):
        self.__cuentas_bancaria = valor

    def crear_nueva_cuenta_bancaria(self,nro_cuenta:str,cbu:str,alias:str,saldo:float, monto_limite_extracciones: float,monto_limite_transferencias: float,cant_extracciones_disponibles: int,cant_transferencias_disponibles: int,maximo_descubierto:float,tipo_de_cuenta:"CuentaBancaria"):
        retorno = False
        if tipo_de_cuenta == "CajaDeAhorro":
            nueva_cuenta = CajaDeAhorro(nro_cuenta,cbu,alias,saldo,monto_limite_extracciones,monto_limite_transferencias,cant_extracciones_disponibles,cant_transferencias_disponibles)
            self.cuentas_bancarias.append(nueva_cuenta)
            retorno = True
        elif tipo_de_cuenta == "CuentaCorriente":
            nueva_cuenta = CuentaCorriente(nro_cuenta,cbu,alias,saldo,maximo_descubierto)
            self.cuentas_bancarias.append(nueva_cuenta)
            retorno = True

        return retorno

class Banco():
    def __init__(self,nombre:str,domicilio:str):
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__clientes = []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor

    @property
    def domicilio(self):
        return self.__domicilio
    
    @domicilio.setter
    def domicilio(self,valor):
        self.__domicilio = valor

    @property
    def listaclientes(self):
        return self.__clientes
    
    @listaclientes.setter
    def listaclientes(self,valor):
        self.__clientes = valor


    def crear_nuevo_cliente(self, razon_social, cuit, tipo_persona, domicilio):
        nuevo_cliente = Cliente(razon_social, cuit, tipo_persona, domicilio)
        self.__clientes.append(nuevo_cliente)
        return True
    


if __name__ == "__main__":
    mi_banco = Banco("Bancio Nacion","Av. de Mayo 1464")
    mi_banco.crear_nuevo_cliente("Sociedad Anónima","30-12345678-6","Fisica","Calle Ficticia, 1234, Ciudad Ficticia, Provincia Ficticia")
    mi_banco.crear_nuevo_cliente("Inversiones Internacionales","98-76543210-2","Jurídica","Avenida Principal, 123, Capital Metropolitana, Provincia Principal")
    mi_banco.crear_nuevo_cliente("Cliente de Prueba","11-22223333-4","Física","Calle Principal, 456, Ciudad de Ejemplo, Provincia de Prueba")
    cliente1 = mi_banco.listaclientes[0]
    cliente2 = mi_banco.listaclientes[1]
    cliente3 = mi_banco.listaclientes[2]
    cliente1.crear_nueva_cuenta_bancaria("1234567890","CBU1234567890123456789","Fisica.cuenta",5000.00,10000,10000,10,10,0,"CajaDeAhorro")
    cliente1.crear_nueva_cuenta_bancaria("9876543210","AR0009876543210987654321","juridica.cuenta",4000.00,5000,10000,0,0,5000,"CuentaCorriente")
    cliente1_caja_de_ahorro = cliente1.cuentas_bancarias[0]
    cliente1_cuenta_corriente = cliente1.cuentas_bancarias[1]

    cliente2.crear_nueva_cuenta_bancaria("5555555555","AR0005555555555555555555","CuentaJoven777",250.75,100.00,500.00,10,10,0,"CajaDeAhorro")
    cliente2.crear_nueva_cuenta_bancaria("1111222233","CBU11112222331111222233","Cuenta de Inversiones",20000.00,0,0,0,0,10000,"CuentaCorriente")
    cliente2_caja_de_ahorro = cliente2.cuentas_bancarias[0]
    cliente2_cuenta_corriente = cliente2.cuentas_bancarias[1]

    cliente3.crear_nueva_cuenta_bancaria("9876123456","CBU98761234569876123456","Cuenta Empresarial",15000.00,20000.00,20000.00,10,10,0,"CajaDeAhorro")
    cliente3.crear_nueva_cuenta_bancaria("9999999999","CBU9999999999999999999","Cuenta de Jubilación",10000.00,0,0,0,0,4000,"CuentaCorriente")
    cliente3_caja_de_ahorro = cliente3.cuentas_bancarias[0]
    cliente3_cuenta_corriente = cliente3.cuentas_bancarias[1]

    def mostrar_estado_cuentas_cliente1(): 
        print("\n- Cliente 1 -")
        print("Caja de Ahorro:")
        cliente1_caja_de_ahorro.mostrar()
        print("\nCuenta Corriente:")
        cliente1_cuenta_corriente.mostrar()

    def mostrar_estado_cuentas_cliente2():
        print("\n- Cliente 2 -")
        print("Caja de Ahorro:")
        cliente2_caja_de_ahorro.mostrar()
        print("\nCuenta Corriente:")
        cliente2_cuenta_corriente.mostrar()

    def mostrar_estado_cuentas_cliente3():
        print("\n- Cliente 3 -")
        print("Caja de Ahorro:")
        cliente3_caja_de_ahorro.mostrar()
        print("\nCuenta Corriente:")
        cliente3_cuenta_corriente.mostrar()
        
    #Estados de cuentas de los clientes
    print("💵💵💵💵💵💵💵💵💵💵💵💵💵💵💵💵💵💵")
    mostrar_estado_cuentas_cliente1()
    mostrar_estado_cuentas_cliente2()
    mostrar_estado_cuentas_cliente3()
    print("💵💵💵💵💵💵💵💵💵💵💵💵💵💵💵💵💵💵")

    #Simulaciones
    print("\nSimulacion 1")
    cliente1_caja_de_ahorro.transferir(400,cliente3_caja_de_ahorro)
    mostrar_estado_cuentas_cliente1()
    mostrar_estado_cuentas_cliente3()
    print("Fin de la simulacion 1")

    print("\nSimulacion 2")
    cliente2_caja_de_ahorro.extraer(50)
    mostrar_estado_cuentas_cliente2()
    print("Fin de la simulacion 2")

    print("\nSimulacion 3")
    cliente3_cuenta_corriente.transferir(600,cliente2_cuenta_corriente)
    mostrar_estado_cuentas_cliente2()
    mostrar_estado_cuentas_cliente3()
    print("Fin de la simulacion 3")

    print("\nSimulacion 4")
    cliente1_cuenta_corriente.depositar(6000)
    mostrar_estado_cuentas_cliente1()
    print("Fin de la simulacion 4")
