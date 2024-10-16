import os

class Pelicula:
    # ... (código de la clase Pelicula existente)

def mostrar_menu():
    print("Bienvenido a tu catálogo de películas!")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar película")
    print("4. Buscar película")
    print("5. Eliminar catálogo")
    print("6. Salir")

def agregar_pelicula(catalogo):
    # ... (código de la función agregar_pelicula)

def listar_peliculas(catalogo):
    # ... (código de la función listar_peliculas)

# ... (funciones para las demás opciones)

if __name__ == "__main__":
    catalogo = CatalogoPelicula("Mi Catálogo")

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            agregar_pelicula(catalogo)
        elif opcion == '2':
            listar_peliculas(catalogo)
        # ... (demás opciones)
        else:
            print("Opción inválida. Intente nuevamente.")