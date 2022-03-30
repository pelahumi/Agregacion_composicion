from clases.dia_mañana import * 

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