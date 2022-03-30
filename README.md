# Agregacion_composicion
La dirección del repositorio es la siguiente: [GitHub](https://github.com/pelahumi/Agregacion_composicion)

## Día del mañana
´´´python3
class NuevaYork():

    def __init__(self):
        self.edificios = [Edificios(nombre) for nombre in ["A", "B"]]
        self.edificios = [Empleados(nombre) for nombre in ["Martin", "Salin"]]

    def __del__(self):
        print("Nueva York fue destruido")

class LosAngeles():

    def __init__(self):
        self.edificios = [Edificios(nombre) for nombre in ["C"]]
        self.edificios = [Empleados(nombre) for nombre in [["Xing"]]]

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
        print("Los edificios {} fueron destruidos".format(self.nombre))

class Empleados():

    def __init__(self, nombre):
        self.nombre = nombre
    
    def __del__(self):
        print("{} ha muerto".format(self.nombre))


## YinYang
´´´python3



## Alternativa
´´´python3

