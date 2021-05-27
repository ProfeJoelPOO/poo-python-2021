class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._enmarcha = False
        self._acelera = False
        self._frena = False

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def enmarcha(self):
        return self._enmarcha

    @property
    def acelera(self):
        return self._acelera

    @property
    def frena(self):
        return self._frena

    def arrancar(self):
        self._enmarcha = True

    def apagar(self):
        self._enmarcha = False

    def acelerar(self):
        self._acelera = True
        self._frena = False

    def frenar(self):
        self._frena = True
        self._acelera = False

    def __str__(self):
        return 'Marca: ' + self._marca + ' , Modelo: ' + self._modelo + ' , En Marcha: ' + str(self._enmarcha) + ' , Acelera: ' + str(self._acelera) + ' , Frena: ' + str(self._frena)


v1 = Vehiculo('Honda', 'CBR')
v1.arrancar()
v1.acelerar()
v1.frenar()
print(v1)
