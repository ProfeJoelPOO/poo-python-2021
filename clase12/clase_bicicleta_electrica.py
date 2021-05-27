from clase_vehiculo import Vehiculo
from clase_vehiculo_electrico import VElectrico

# Usamos el nombre de la clase y no el super ya que es mas facil de darnos
# cuenta a la hora de leer el codigo a qué clase nos estamos refiriendo
# a la hora de aplicar un metodo o utilizar un atributo de una de las clases padre
# de las cuales estamos heredando
# Ya que, con Super, se hace referencia sólo a la primera de las clases de las listadas en las clases padres
# de las multiclases de herencia
# Con este método de hacer llamado a funciones y atributos es necesario pasar el self como parametro (es un must!!)
class BicicletaElectrica(VElectrico, Vehiculo):
    def __init__(self, autonomia, marca, modelo, color):
        VElectrico.__init__(self, autonomia)
        Vehiculo.__init__(self, marca, modelo)
        self.__color = color

    def __str__(self):
        return Vehiculo.__str__(self) + ' , ' + VElectrico.__str__(self) + ' , ' + 'Color: ' + self.__color


miBici = BicicletaElectrica(200, 'Mommo', '2021', 'Verde')
print(miBici)
