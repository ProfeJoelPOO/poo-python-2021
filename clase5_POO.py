# Clase y objeto
# Clase: Es una plantilla o estructura c
# Objeto: Es una instancia de una clase
#         - Atributos (Estado interno) y Métodos (Comportamiento)
#         - Son únicos (Poseen un nombre)

# Sintaxis clase
# pass - Estamos "pasando" la clase
class Persona:

    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Métodos
    def saludar(self):
        print('Hola soy '+ self.nombre +' y tengo '+ str(self.edad) +' años! :)')


# Clase - ya es un objeto dentro de Python por si misma
Persona.nombre = 'Juan'
Persona.edad = 28
print(Persona.nombre)
print(Persona.edad)

# Creación de un objeto
persona1 = Persona('Karla', 30)
print(persona1.nombre)
print(persona1.edad)

persona1.saludar()
