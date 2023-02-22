#clase animal y su constructor
class Animal:
    def __init__(self, nombre, especie, edad, peso, color, alimentacion):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.color = color
        self.alimentacion = alimentacion

#getters y setters

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_especie(self):
        return self.especie

    def set_especie(self, especie):
        self.especie = especie

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_alimentacion(self):
        return self.alimentacion

    def set_alimentacion(self, alimentacion):
        self.alimentacion = alimentacion

    def salutacio(self):
        print("Hola, soy un", self.especie, "llamado", self.nombre, "y tengo", self.edad, "años. Peso", self.peso, "kilos y mi color es", self.color, ". Me alimento de", self.alimentacion)

