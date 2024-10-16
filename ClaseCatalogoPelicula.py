import os

from ClasePelicula import Pelicula


class CatalogoPelicula():  # Defino la clase Catalogo pelicula
    # Inicio el constructor y le doy los dos atributos pedidos
    def __init__(self, nombre):
        self.nombre = nombre  # Para que el nombre se guarde en el parametro nombre
        # Para que la ruta del archivo se guarde en ruta_archivo
        self.ruta_archivo = f"Archivos/{self.nombre}.txt"

        # Aca capturo una excepcion para que si el catalogo ya existe
        # cuando se lo intenta crear, siga trabajando sobre el prepre existente
        try:
            with open(self.ruta_archivo, 'x') as file:
                print(f'El catalogo {self.nombre} ha sido creado exitosamente')
        except FileExistsError:
            pass

    # Creo el metodo para agregrar peliculas al catalogo: Uso la clase Pelicula.
    def agregarPelicula(self, pelicula):
        # Lo abro con 'a' para agregar a algo ya existente
        with open(self.ruta_archivo, 'a') as file:
            # Uso 'str' para convertir la clase pelicula en un string
            # y que pueda usarse con el metodo __str__ de la clase Pelicula
            file.write(str(pelicula))
        # Imprimo un mensaje si fue agregado exitosamente para que el usuario lo sepa
        print(f"La pelicula {pelicula} ha sido agregada con exito al catalogo {self.ruta_archivo}")

    #
    def listarPeliculas(self):  # Metodo para mostrar las peliculas del catalogo
        # Abro en modo lectura el txt donde se guardan las peliculas
        # Atrapo una excepcion para el caso de que intente listar un catalogo vacio
        try:
            with open(self.ruta_archivo, 'r') as file:
                # Uso el metodo readlines para leer todas las lineas del archivo a la vez
                lines = file.readlines()
                print(f'La lista de peliculas del {self.nombre} es: ')
                # Recorro cada linea para mostrarlas
                # Uso el metodo enumerate para obtener un indice para cada pelicula
                for indice, line in enumerate(lines):
                    # agrego +1 a indice para que arranque en el indice nro 1 y no en el nro 0 lo que ve el usuario
                    print(f'{indice+1}. {line}', end='')
        except:
            pass

    # Para crear este metodo pensamos que utilizar indices seria la forma mas sencilla y visualmente comoda (igual que listarPeliculas)
    def eliminarPelicula(self, indicePelicula):
        # Atrapo una excepcion donde primero leo el archivo con readlines()
        try:
            with open(self.ruta_archivo, 'r') as file:
                lines = file.readlines()
        # Reescribo el archivo sin la pelicula que se elimina
            with open(self.ruta_archivo, 'w') as file:
                for indice, line in enumerate(lines):
                    # Aqui le pido que si es diferente, reescriba lo que es diferente. Es decir, la elimina reescribiendo las que no elimina
                    if indice != indicePelicula:
                        file.write(line)
        # Este except es para que no rompa el codigo si la pelicula a eliminar no existe
        except:
            pass

    # Defino un metodo para eliminar el catalogo completo
    def eliminarCatalogo(self):
        if os.path.exists(self.ruta_archivo):
            # Le pido la confirmacion al usuario.
            confirmacion = input(
                'Estas seguro que queres eliminar el catalogo? [Y/n] :').lower()
            # Si ingresa algo diferente a n se borrara. Si ingresa incluso n mayuscula, no se borrara
            if confirmacion != 'n':
                os.remove(self.ruta_archivo)

    # Defino un metodo para buscar una pelicula por cualquier texto
    def buscarPelicula(self, busqueda):
        try:
            with open(self.ruta_archivo, 'r') as file:
                # Uso el metodo readlines para leer todas las lineas del archivo a la vez
                lines = file.readlines()
                # Recorro cada linea para mostrarlas
                # Uso el metodo enumerate para obtener un indice para cada pelicula
                for indice, line in enumerate(lines):
                    # Uso if para que se muestren todos los resultados que tengan el texto buscado
                    if busqueda in line:
                        print(f'{indice+1}. {line}', end='')
        # Atrapo una excepcion por si la pelicula que busco no existe
        except:
            pass


# # Pruebas del codigo
#Catalogo1 = CatalogoPelicula("Catalogo 1")
#Catalogo1.agregarPelicula(Pelicula("Star Wars", "Ciencia ficcion", "Juvenil"))
#Catalogo1.agregarPelicula(Pelicula("Peter Pan", "Infantil", "Juvenil"))
#Catalogo1.agregarPelicula(Pelicula("El Padrino", "Drama", "Adulto"))

#Catalogo1.listarPeliculas()

#Catalogo1.eliminarPelicula(0)
#Catalogo1.listarPeliculas()

#Catalogo1.buscarPelicula("Juvenil")

#Catalogo1.eliminarCatalogo()
#Catalogo1.listarPeliculas()
