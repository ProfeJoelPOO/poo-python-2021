class Persona:
    contador_persona = 0

    # @classmethod
    # def generar_siguiente_valor(cls):
    #     cls.contador_persona += 1
    #     return cls.contador_persona

    @staticmethod
    def generar_siguiente_id():
        Persona.contador_persona += 1
        return Persona.contador_persona

    # Desde el método constructor llamamos al método generar_siguiente_valor
    # para obtener un id unico auto incrementado, es decir,
    # es contexto dinámico llama al contexto estático a través de la clase Persona
    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_id()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [ID Persona: {self.id_persona}, Nombre: {self.nombre}, Edad: {self.edad}]'


per1 = Persona('Juan', 30)
print(per1)
per2 = Persona('Camila', 23)
print(per2)
Persona.generar_siguiente_id()
per3 = Persona('Pablo', 89)
print(per3)
