from datetime import date

class CuentaBancaria:
    def __init__(self, nro_cuenta, cbu, alias, saldo):
        self.nro_cuenta = nro_cuenta
        self.cbu = cbu
        self.alias = alias
        self.saldo = saldo
        self.movimientos = []

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, monto_a_depositar):
        if monto_a_depositar > 0:
            self.saldo += monto_a_depositar
            self.movimientos.append((date.today(), "depósito", monto_a_depositar, self.saldo))
            return True
        return False

    def extraer(self, monto_a_extraer):
        pass  # Este método será implementado en las clases hijas

    def transferir(self, monto_a_transferir, cuenta_destino):
        pass  # Este método será implementado en las clases hijas

class CajaDeAhorro(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles, cant_transferencias_disponibles):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.monto_limite_extracciones = monto_limite_extracciones
        self.monto_limite_transferencias = monto_limite_transferencias
        self.cant_extracciones_disponibles = cant_extracciones_disponibles
        self.cant_transferencias_disponibles = cant_transferencias_disponibles

    def extraer(self, monto_a_extraer):
        if monto_a_extraer > 0 and monto_a_extraer <= self.saldo and monto_a_extraer <= self.monto_limite_extracciones and self.cant_extracciones_disponibles > 0:
            self.saldo -= monto_a_extraer
            self.cant_extracciones_disponibles -= 1
            self.movimientos.append((date.today(), "extracción", monto_a_extraer, self.saldo))
            return True
        return False

    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= self.saldo and monto_a_transferir <= self.monto_limite_transferencias and self.cant_transferencias_disponibles > 0:
            self.saldo -= monto_a_transferir
            self.cant_transferencias_disponibles -= 1
            self.movimientos.append((date.today(), "transferencia", monto_a_transferir, self.saldo))
            cuenta_destino.depositar(monto_a_transferir)
            return True
        return False

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nro_cuenta, cbu, alias, saldo, monto_maximo_descubierto):
        super().__init__(nro_cuenta, cbu, alias, saldo)
        self.monto_maximo_descubierto = monto_maximo_descubierto

    def extraer(self, monto_a_extraer):
        if monto_a_extraer > 0 and monto_a_extraer <= (self.saldo + self.monto_maximo_descubierto):
            self.saldo -= monto_a_extraer
            self.movimientos.append((date.today(), "extracción", monto_a_extraer, self.saldo))
            return True
        return False

    def transferir(self, monto_a_transferir, cuenta_destino):
        if monto_a_transferir > 0 and monto_a_transferir <= (self.saldo + self.monto_maximo_descubierto):
            self.saldo -= monto_a_transferir
            self.movimientos.append((date.today(), "transferencia", monto_a_transferir, self.saldo))
            cuenta_destino.depositar(monto_a_transferir)
            return True
        return False

class Cliente:
    def __init__(self, razon_social, cuit, tipo_persona, domicilio):
        self.razon_social = razon_social
        self.cuit = cuit
        self.tipo_persona = tipo_persona
        self.domicilio = domicilio
        self.cuentas_bancarias = []

    def crear_nueva_cuenta_bancaria(self, tipo_cuenta, nro_cuenta, alias, cbu, saldo, *args):
        nueva_cuenta = tipo_cuenta(nro_cuenta, cbu, alias, saldo, *args)
        self.cuentas_bancarias.append(nueva_cuenta)
        return True

class Banco:
    def __init__(self, nombre, domicilio):
        self.nombre = nombre
        self.domicilio = domicilio
        self.clientes = []

    def crear_nuevo_cliente(self, razon_social, cuit, tipo_persona, domicilio):
        nuevo_cliente = Cliente(razon_social, cuit, tipo_persona, domicilio)
        self.clientes.append(nuevo_cliente)
        return True


banco = Banco("Mi Banco", "Calle Principal 123")

cliente1 = banco.crear_nuevo_cliente("Cliente 1", "12345678901", "física", "Calle A 1")
cliente2 = banco.crear_nuevo_cliente("Cliente 2", "23456789012", "física", "Calle B 2")
cliente3 = banco.crear_nuevo_cliente("Cliente 3", "34567890123", "jurídica", "Calle C 3")

cuenta1_cliente1 = cliente1.crear_nueva_cuenta_bancaria(CajaDeAhorro, "001", "Caja1", "CBU001", 1000, 500, 5000, 3, 5)
cuenta2_cliente1 = cliente1.crear_nueva_cuenta_bancaria(CuentaCorriente, "002", "Corriente1", "CBU002", 2000, 1000)
cuenta1_cliente2 = cliente2.crear_nueva_cuenta_bancaria(CajaDeAhorro, "003", "Caja2", "CBU003", 1500, 600, 6000, 4, 4)
cuenta1_cliente3 = cliente3.crear_nueva_cuenta_bancaria(CajaDeAhorro, "004", "Caja3", "CBU004", 3000, 700, 7000, 5, 3)

    # Realizar operaciones
cuenta1_cliente1.depositar(500)
cuenta1_cliente1.extraer(300)
cuenta1_cliente1.transferir(200, cuenta1_cliente2)
cuenta2_cliente1.extraer(300)

print(cuenta1_cliente1.__dict__)