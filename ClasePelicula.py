# Iniciamos construyendo la Clase Película:

class Pelicula:
    def __init__(self, nombre, genero, clasificacion):
        # Definimos que el Atributo "Nombre" es privado.
        self.__nombre = nombre
        self.genero = genero
        # Definimos que el Atributo "Clasificación" es privado.
        self.__clasificacion = clasificacion

    # Definir el método getter para acceder al nombre de la película.
    def get_nombre(self):
        return self.__nombre

    # Definir el método getter para acceder la clasificacion.
    def get_clasificacion(self):
        return self.__clasificacion

    # Uso el metodo __str__ para convertir el objeto en una string y poder utilizarlo en la clase CatalogoPelicula
    def __str__(self):
        return (f'{self.__nombre}, {self.genero}, {self.__clasificacion} \n')
