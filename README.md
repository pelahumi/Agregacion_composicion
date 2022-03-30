# Agregacion_composicion
La dirección del repositorio es la siguiente: [GitHub](https://github.com/pelahumi/Agregacion_composicion)

El UML del primer ejercicio no se porque no se ve en el readme, pero esta en la carpeta UML en formato png y drawio con el resto.

## Día del mañana
```python3
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
```

Diagrama UML:

![UML](https://github.com/pelahumi/Agregacion_composicion/blob/main/UML/Dia%20del%20mañana.png)

## YinYang
```python3
class Yin: 
    pass 

class Yang:
 
    def __del__(self): 
        print("?") #Metemos el print dentro de la función en la linea anterior de Yang destruido
        print("Yang destruido") 
```

Diagrama UML:

![UML](https://github.com/pelahumi/Agregacion_composicion/blob/main/UML/YinYang.png)

## Alternativa
```python3
class Pared:
    #Constructor
    def __init__(self, orientacion):
        self.orientacion = orientacion


class InterfazCristal(Pared):
    #Constructor
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion) 
        self.superficie = superficie

    def get_area(self):
        return self.superficie


class Casa(InterfazCristal):
    #Constructor
    def __init__(self, paredes, orientacion, superficie):
        super().__init__(orientacion, superficie)
        self.paredes = paredes
    
    def superficie_acristalada(self):
        return sum(self.paredes.superficie)
```

Diagrama UML:
![UML](https://github.com/pelahumi/Agregacion_composicion/blob/main/UML/Alternativa.png)


