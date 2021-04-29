# Herencia
# Clase Padre: Persona
# Clase Hija: Empleado
# La clase Empleado va a heredar las características de la clase Persona

# Python permite heredar atributos privados, pero debemos colocar como protegidos
# aquellos atributos que queremos que se herenden a clase hijas

class Persona(object):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def _metodo_clase(self):
        print('Soy la clase Persona')

    def __str__(self):
        return 'Nombre: ' + self._nombre + ' Edad: ' + str(self._edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) # Super refiere a la clase padre
        self._sueldo = sueldo

    def _metodo_clase(self):
        print('Soy la clase Empleado')

    def llamo_al_metodo(self):
        super()._metodo_clase()

    def __str__(self):
        return super().__str__() + ' Sueldo: ' + str(self._sueldo)


e1 = Empleado('Carlos', 35, 10000.0)
e1.llamo_al_metodo()
print(e1.__str__())

p1 = Persona('Jorge', 34)
print(p1.__str__())
