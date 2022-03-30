class NuevaYork():

    def __init__(self):
        self.edificios = [Edificios(nombre) for nombre in ["Martin", "Salin"]]
        self.edificios = [Empleados(nombre) for nombre in ["A", "B"]]

    def __del__(self):
        print("Nueva York fue destruido")

class LosAngeles():

    def __init__(self):
        self.edificios = [Edificios(nombre) for nombre in ["Xing"]]
        self.edificios = [Empleados(nombre) for nombre in ["C"]]

    def __del__(self):
        print("Los Ángeles fue destruido")

class Empresa():

    def __init__(self):
        self.propietario = "YooHoo"
    
    def __del__(self):
        print("La empresa se ha destruido")
    

class Edificios():

    def __init__(self, nombre):
        self.nombre = nombre
    
    def __del__(self):
        print("Los edificios {} fueron destruidos").format(self.nombre)

class Empleados():

    def __init__(self, nombre):
        self.nombre = nombre
    
    def __del__(self):
        print("{} ha muerto").format(self.nombre)
