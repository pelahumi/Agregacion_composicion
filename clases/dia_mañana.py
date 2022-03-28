class NuevaYork():

    def __init__(self):
        self.edificios = [Edificios(nombre) for nombre in ["Martin", "Salin"]]
        self.edificios = [Empleados(nombre) for nombre in ["A", "B"]]

class Empresa():

    def __init__(self):
        self.propietario = "YooHoo"

class Edificios():

    def __init__(self, nombre):
        self.nombre = nombre

class Empleados():

    def __init__(self, nombre):
        self.nombre = nombre
