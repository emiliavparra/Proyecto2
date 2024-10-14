# Iniciamos construyendo la Clase Película:

class Pelicula:
    def __init__(self,nombre,genero,clasificacion):
        self.__nombre = nombre  # Definimos que el Atributo "Nombre" es privado.
        self.genero = genero
        self.__clasificacion = clasificacion  # Definimos que el Atributo "Clasificación" es privado.
    
    # Definir el método getter para acceder al nombre de la película.
    def get_nomnbre(self):
        return self.__nombre
        