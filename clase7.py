# POO: Programación Orientada a Objetos
# - Encapsulamiento:
#       Visibilidad (UML): Público, privado, protegido, paquete
#       Objectos: Atributos y Métodos
#       Atributos (estado interno del objeto) no debe ser modificado ni accedido desde fuera del objeto
#       Para acceder u obtener los atributos vamos a usar GETTERS
#       Para modificar o setear los atributos vamos a usar SETTERS
# - Herencia:
#       Objectos: Atributos y Métodos
#       Es un mecanismo que permite adquirir métodos y atributos de la clase padre a la cual hace referencia
#       Los métodos y atributos que sean privados no se heredan
# - Poliformismo
# - Abstraccion

class Persona:
    def __init__(self, n, ape_paterno, ape_materno):
        self.__nombre = n
        self.apellido_paterno = ape_paterno
        self._apellido_materno = ape_materno
        # Llama de un método privado
        self.__metodo_privado()

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido_paterno(self):
        return self.apellido_paterno

    def set_apellido_paterno(self, ape_paterno):
        self.apellido_paterno = ape_paterno

    def get_apellido_materno(self):
        return self._apellido_materno

    def set_apellido_materno(self, ape_materno):
        self._apellido_materno = ape_materno

    def __metodo_privado(self):
        print('Hola, soy un metodo privado')


p1 = Persona('Juan', 'Perez', 'Gonzalez') # Objeto p1 de tipo Persona

# print(p1.__nombre) => Esto arroja ERROR
# print(p1._apellido_materno) => Python permite acceder a los protegidos pero no es una buena práctica

print(p1.get_nombre())

#p1.__nombre = 'Karla' => Esto arroja ERROR

p1.set_nombre('Karla')
print(p1.get_nombre())

# p1.__metodo_privado() => Esto arroja ERROR
