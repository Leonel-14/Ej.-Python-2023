class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def ingresar_saldo(self, ingreso_saldo, cuenta_destino):
        if ingreso_saldo > 0:
            self.saldo += ingreso_saldo  
        else:
            print("El monto de ingreso debe ser mayor que cero.")

class CuentaCorriente(CuentaBancaria):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase padre

    def consultar_saldo(self):
        return self.saldo

# Crear una instancia de la clase hija
cuenta = CuentaCorriente()

# Ingresar saldo en la cuenta corriente
cuenta.ingresar_saldo(200, "Cuenta Corriente")  # Ingresa 100 a la cuenta de Cuenta Corriente

# Consultar el saldo de la cuenta corriente
saldo_actual = cuenta.consultar_saldo()
print(f"El saldo actual de la cuenta corriente es: {saldo_actual}")


    

    