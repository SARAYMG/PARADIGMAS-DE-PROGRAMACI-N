class SaldoEfectivoInsuficiente(Exception):
    """Excepción lanzada cuando el cajero no tiene suficiente efectivo."""
    pass

class SaldoCuentaInsuficiente(Exception):
    """Excepción lanzada cuando la cuenta no tiene suficiente saldo para la operación."""
    pass

class Cuenta:
    def __init__(self, numero_cuenta, nombre, saldo):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoCuentaInsuficiente(f"Saldo insuficiente en la cuenta. Saldo disponible: {self.saldo}")
        self.saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")

    def transferir(self, otra_cuenta, monto):
        if monto > self.saldo:
            raise SaldoCuentaInsuficiente(f"Saldo insuficiente en la cuenta. Saldo disponible: {self.saldo}")
        self.saldo -= monto
        otra_cuenta.depositar(monto)
        print(f"Transferencia exitosa. Nuevo saldo: {self.saldo}")

    def mostrar_datos(self):
        print(f"Cuenta: {self.numero_cuenta}, Nombre: {self.nombre}, Saldo: {self.saldo}")

class CajeroAutomatico:
    def __init__(self, saldo_efectivo):
        self.saldo_efectivo = saldo_efectivo
        self.cuentas = {}

    def agregar_cuenta(self, cuenta):
        self.cuentas[cuenta.numero_cuenta] = cuenta

    def autenticar(self, numero_cuenta):
        if numero_cuenta in self.cuentas:
            return self.cuentas[numero_cuenta]
        else:
            print("Número de cuenta no encontrado.")
            return None

    def depositar(self, cuenta, monto):
        cuenta.depositar(monto)

    def depositar_otras_cuentas(self, numero_cuenta_destino, monto):
        cuenta_destino = self.cuentas.get(numero_cuenta_destino)
        if cuenta_destino:
            cuenta_destino.depositar(monto)
        else:
            print("Cuenta destino no encontrada.")

    def transferir(self, cuenta_origen, numero_cuenta_destino, monto):
        cuenta_destino = self.cuentas.get(numero_cuenta_destino)
        if cuenta_destino:
            cuenta_origen.transferir(cuenta_destino, monto)
        else:
            print("Cuenta destino no encontrada.")

    def retirar(self, cuenta, monto):
        if monto > self.saldo_efectivo:
            raise SaldoEfectivoInsuficiente(f"El cajero no tiene suficiente efectivo. Saldo disponible en cajero: {self.saldo_efectivo}")
        cuenta.retirar(monto)
        self.saldo_efectivo -= monto
        print(f"Retiro exitoso. Efectivo restante en cajero: {self.saldo_efectivo}")

# Creación de cuentas y cajero automático
cuenta1 = Cuenta("135790", "Saray Mendo", 4500)
cuenta2 = Cuenta("246801", "Lenin Paredes", 6800)
cuenta3 = Cuenta("345712", "Misael Ramirez", 3500)

cajero = CajeroAutomatico(100000)
cajero.agregar_cuenta(cuenta1)
cajero.agregar_cuenta(cuenta2)
cajero.agregar_cuenta(cuenta3)

# Simulación de operaciones
try:
    # Autenticación de cuentahabiente
    cuenta_actual = cajero.autenticar("135790")
    if cuenta_actual:
        cuenta_actual.mostrar_datos()

        # Depósito en cuenta propia
        cajero.depositar(cuenta_actual, 9000)

        # Depósito en otra cuenta
        cajero.depositar_otras_cuentas("246801", 800)

        # Transferencia a otra cuenta
        cajero.transferir(cuenta_actual, "345712", 1000)

        # Retiro de efectivo
        cajero.retirar(cuenta_actual, 2000)

except SaldoEfectivoInsuficiente as e:
    print(e)
except SaldoCuentaInsuficiente as e:
    print(e)
