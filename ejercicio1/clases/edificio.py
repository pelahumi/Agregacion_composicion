class Edificio():
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.propietario = "YooHoo"

    def __del__(self):
        print("Se ha destruido el edificio {}".format(self.nombre))

