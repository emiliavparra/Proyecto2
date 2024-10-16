import os

# Importamos las clases Película y Catálogo Película
from ClasePelicula import Pelicula
from ClaseCatalogoPelicula import CatalogoPelicula


# Definición del menú principal
def mostrar_menu():
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar película")
    print("4. Buscar película")
    print("5. Eliminar catálogo")
    print("6. Salir")

# Función para agregar una película al catálogo


def agregar_pelicula(catalogo):
    nombre = input("Ingresa el nombre de la película: ")
    genero = input("Ingresa el género de la película: ")
    clasificacion = input("Ingresa la clasificación de la película: ")
    pelicula = Pelicula(nombre, genero, clasificacion)
    catalogo.agregarPelicula(pelicula)

# Función para listar las películas del catálogo


def listar_peliculas(catalogo):
    catalogo.listarPeliculas()

# Función para eliminar una película del catálogo


def eliminar_pelicula(catalogo):
    indice = int(
        input("Ingresa el índice de la película que quieres eliminar: ")) - 1
    catalogo.eliminarPelicula(indice)

# Función para buscar una película en el catálogo


def buscar_pelicula(catalogo):
    busqueda = input(
        "Ingresa el nombre o parte del nombre de la película que buscas: ")
    catalogo.buscarPelicula(busqueda)

# Función para eliminar todo el catálogo


def eliminar_catalogo(catalogo):
    catalogo.eliminarCatalogo()

# Función para salir del programa


def salir():
    print("Gracias por usar el catálogo de películas. ¡Hasta luego!")
    exit()


# Código principal: punto de entrada donde se ejecutan todas las acciones y donde el usuario interactúa con el programa.
catalogo = CatalogoPelicula("Mi Catálogo")
print("\nBienvenido a tu catálogo de películas!")
while True:
    print('\n------------------------------------')
    mostrar_menu()
    print('------------------------------------\n')
    opcion = input("Por favor ingresa una opción: ")

    if opcion == '1':
        agregar_pelicula(catalogo)
    elif opcion == '2':
        listar_peliculas(catalogo)
    elif opcion == '3':
        eliminar_pelicula(catalogo)
    elif opcion == '4':
        buscar_pelicula(catalogo)
    elif opcion == '5':
        eliminar_catalogo(catalogo)
    elif opcion == '6':
        salir()
    else:
        print("No entendí qué es lo que quieres hacer, inténtalo nuevamente.")
