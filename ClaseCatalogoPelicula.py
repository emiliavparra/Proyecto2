import os


class CatalogoPelicula():  # Defino la clase Catalogo pelicula
    # Inicio el constructor y le doy los dos atributos pedidos
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre  # Para que el nombre se guarde en el parametro nombre
        # Para que la ruta del archivo se guarde en ruta_archivo
        self.ruta_archivo = ruta_archivo

        # Aca capturo una excepcion para que si el catalogo ya existe
        # cuando se lo intenta crear, siga trabajando sobre el predeterminado
        try:
            with open(self.ruta_archivo, 'x') as file:
                print(f'El catalogo {self.nombre} ha sido creado exitosamente')
        except FileExistsError:
            pass

    # Creo el metodo para agregrar peliculas al catalogo:
    # o el nuevo que se haya creado en el paso anterior
    # o en el predeterminado (catalogo1)
    def agregarPelicula(self, nombre, fechaDeEstreno, director):
        with open(self.ruta_archivo, 'a') as file:
            file.write(f"'{nombre}', {fechaDeEstreno}, {director}\n")
        print(f'La pelicula {nombre} se ha agregado con exito al catalogo')

    #
    def listarPeliculas(self):
        with open(self.ruta_archivo, 'r') as file:
            print(f'La lista de peliculas del {self.nombre} es: ')
            listaPeliculas = file.read()
            print(listaPeliculas)

    def eliminarPelicula(self, nombre):
        with open(self.ruta_archivo, 'r') as file:
            line = file.readline()
            while line:
                print(line.strip())
                line = file.readline()

    def buscarPelicula(self):
        pass


Catalogo1 = CatalogoPelicula('Catalogo uno', 'Archivos/catalogo1.txt')
