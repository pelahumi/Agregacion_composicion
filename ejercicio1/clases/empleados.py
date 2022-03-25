class Empleados():
    def __init__(self, nombre):
        self.nombre = nombre
        self.jefe = "YooHoo"

    def __del__(self):
        print("El empleado {} ha muerto".format(self.nombre))
