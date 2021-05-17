'''
1) Haz una clase llamada Persona que siga las siguientes condiciones:
- Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos que se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también su tipo.
- Por defecto, todos los atributos menos el DNI tendrán valores por defecto según su tipo (0 números, cadena vacía para String, etc.). Sexo será hombre por defecto.
- El método __init__ debe poder recibir parámetros y definir valores por defecto en caso de no recibirlos.
- Los métodos que se implementaran son:
* calcularIMC(): calculara si la persona esta en su peso ideal (peso en kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos), significa que esta por debajo de su peso ideal la función devuelve un 0 y si devuelve un valor mayor que 25 significa que tiene sobrepeso, la función devuelve un 1.
* esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
* comprobarSexo(sexo): comprueba que el sexo introducido es correcto. Si no es correcto, será H. No será visible al exterior. Este método es la validación que posee la clase para el ingreso del atributo sexo.
* __str__(): devuelve toda la información del objeto.
* generaDNI(): genera un número aleatorio de 8 cifras, genera a partir de este su número su letra correspondiente. Este método será invocado cuando se construya el objeto. Puedes dividir el método para que te sea más fácil. No será visible al exterior.
* Métodos set de cada parámetro, excepto de DNI.


- Ahora, para ejecutar el programa haga lo siguiente:
* Hacer un menú para la creación de objetos Persona
* Pide por teclado el valor de los atributos, en caso de no ingresar nada debe tener su valor por defecto y permitir modificarlo luego.
* Para cada objeto, deberá comprobar si esta en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
* Indicar para cada objeto si es mayor de edad.
* Por último, mostrar la información de cada objeto.
* Con 0 salir del sistema
'''

import string
import random


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Persona:

    def __init__(self, nombre='', sexo='H', edad=0, peso=0.0, altura=0.0):
        self.__nombre = nombre
        self.__sexo = self.__comprobarSexo(sexo)
        self.__edad = edad
        self.__DNI = self.__generaDNI()
        self.__altura = altura
        self.__peso = peso

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = self.__comprobarSexo(sexo)

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def dni(self):
        return self.__DNI

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    def calcularIMC(self):
        pesoIdeal = self.__peso / (self.__altura ** 2)
        if pesoIdeal < 20 :
            return -1
        elif 20 <= pesoIdeal <= 25:
            return 0
        else:
            return 1

    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return True
        else:
            return False

    def __comprobarSexo(self, sexo):
        if sexo != 'M' and sexo != 'H':
            print('Sexo incorrecto! Se coloca H por defecto!')
            return 'H'
        else:
            return sexo

    def __str__(self):
        return 'Nombre: ' + self.__nombre + ' , sexo: ' + self.__sexo + ' , edad: ' + str(self.__edad) + ' DNI: ' + self.__DNI + ' altura: ' + str(self.__altura) + ' peso: ' + str(self.__peso)

    def __generaDNI(self):
        return id_generator(8)
