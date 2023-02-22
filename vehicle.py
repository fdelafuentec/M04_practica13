class Vehicle:
    def __init__(self, marca, model, any, color, numeroPuertas, motor):
        self.marca = marca
        self.model = model
        self.any = any
        self.color = color
        self.numeroPuertas = numeroPuertas
        self.motor = motor

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_any(self):
        return self.any

    def set_any(self, any):
        self.any = any

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_numeroPuertas(self):
        return self.numeroPuertas

    def set_numeroPuertas(self, numeroPuertas):
        self.numeroPuertas = numeroPuertas

    def get_motor(self):
        return self.motor

    def set_motor(self, motor):
        self.motor = motor

    def parts(self):
        print("Vehiculo de la marca", self.marca, "modelo", self.model, "con", self.numeroPuertas,"puertas, del año", self.any, "de color ", self.color, "y motorizado con", self.motor)