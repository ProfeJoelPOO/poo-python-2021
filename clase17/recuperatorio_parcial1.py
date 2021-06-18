class Cuenta:

    def __init__(self, nombre, numero_cuenta, tipos_interes, saldo):
        self._nombre = nombre
        self._numero_cuenta = numero_cuenta
        self._tipos_interes = tipos_interes
        self._saldo = saldo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def numero_cuenta(self):
        return self._numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, numero_cuenta):
        self._numero_cuenta = numero_cuenta

    @property
    def tipos_interes(self):
        return self._tipos_interes

    @tipos_interes.setter
    def tipos_interes(self, tipos_interes):
        self._tipos_interes = tipos_interes

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def ingreso(self, saldo):
        if saldo > 0:
            self._saldo = self._saldo + saldo
            return True
        else:
            return False

    def reintegro(self, saldo):
        if saldo > 0:
            if (self._saldo - saldo) >= 0:
                self._saldo = self._saldo - saldo
                return True
        else:
            return False

    def tranferir(self, cuenta_destino, saldo):
        correcto = True
        if saldo < 0:
            # Saldo que transfiero negativo
            correcto = False
        elif self._saldo >= saldo:
            self.reintegro(saldo)
            cuenta_destino.ingreso(saldo)
        else:
            # Saldo de la cuenta menor al saldo que transfiero
            correcto = False

        return correcto

    def __str__(self):
        return f"Nombre: {self._nombre}\nNumero_cuenta: {self._numero_cuenta}\nTipos_interes: {self._tipos_interes}\n" \
               f"Saldo: {self._saldo}"
