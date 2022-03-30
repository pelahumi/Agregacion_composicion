class Yin: 
    pass 

class Yang:
 
    def __del__(self): 
        print("?") #Metemos el print dentro de la función en la linea anterior de Yang destruido
        print("Yang destruido") 
 



