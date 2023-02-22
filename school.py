class School:
    def __init__(self, nombre, direccion, numAlumnos, numProfesores, telefono, horario):
        self.nombre = nombre
        self.direccion = direccion
        self.numAlumnos = numAlumnos
        self.numProfesores = numProfesores
        self.telefono = telefono
        self.horario = horario

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_numAlumnos(self):
        return self.numAlumnos

    def set_numAlumnos(self, numAlumnos):
        self.numAlumnos = numAlumnos

    def get_numProfesores(self):
        return self.numProfesores

    def set_numProfesores(self, numProfesores):
        self.numProfesores = numProfesores

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_horario(self):
        return self.horario

    def set_horario(self, horario):
        self.horario = horario

    def info(self):
        print("Colegio", self.nombre, "ubicado en", self.direccion, "con una capacidad de", self.numAlumnos, "y de", self.numProfesores,"de profesores, el telefono de contacto es" , self.telefono, "atendido de", self.horario)