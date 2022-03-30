from clases.dia_mañana import * 
from clases.yinyang import *
from clases.alternativa import *

if __name__ == "__main__":
    print("¿Qué ejercicio quieres ver?:", "\n","1)Dia del mañana", "\n","2)Inmortal", "\n","3)Alternativa herencia multiple")
    n =int(input("Número del ejercicio: "))

    if n == 1:
        destrucion = str(input("¿Qué ciudad quieres destruir, Los Ángeles o Nueva York?"))

        if destrucion == "Los Ángeles":
            la = LosAngeles()
            del la
        elif destrucion == "Nueva York":
            ny = NuevaYork()
            del ny
        else:
            print("La ciudad no es válida")
    
    if n == 2:
        yin = Yin()
        yang = Yang() 
        del(yang) 

    if n == 3:
        pared_norte = Pared("NORTE") 
        pared_oeste = Pared("OESTE") 
        pared_sur = Pared("SUR") 
        pared_este = Pared("ESTE") 
        ventana_norte = InterfazCristal(pared_norte, 0.5) 
        ventana_oeste = InterfazCristal(pared_oeste, 1) 
        ventana_sur = InterfazCristal(pared_sur, 2) 
        ventana_este = InterfazCristal(pared_este, 1) 
        casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
        print(casa.superficie_acristalada()) 