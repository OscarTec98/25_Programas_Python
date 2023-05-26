#García Vázquez Oscar Daniel - 18212189

#

# Base de datos de películas
peliculas = [
    {"titulo": "El padrino", "genero": "Crimen", "año": 1972},
    {"titulo": "Pulp Fiction", "genero": "Drama", "año": 1994},
    {"titulo": "El señor de los anillos", "genero": "Fantasía", "año": 2001},
    {"titulo": "Interestelar", "genero": "Ciencia ficción", "año": 2014},
    {"titulo": "Buenos muchachos", "genero": "Crimen", "año": 1990},
    {"titulo": "El resplandor", "genero": "Terror", "año": 1980},
    {"titulo": "Erase una vez en hollywood", "genero": "Comedia", "año": 2019},
    {"titulo": "Bettlejuice, el súper fantasma", "genero": "Fantasia", "año": 1988},
    {"titulo": "Gran Turismo", "genero": "Drama deportivo", "año": 2023},
    {"titulo": "Alambradas de violencia", "genero": "Spaghetti Western", "año": 1966}
]

# Función para recomendar películas basadas en el género y año
def recomendar_peliculas(genero, año):
    recomendaciones = []
    for pelicula in peliculas:
        if pelicula["genero"] == genero and pelicula["año"] >= año:
            recomendaciones.append(pelicula["titulo"])
    return recomendaciones

# Pedir al usuario que ingrese sus gustos
genero_preferido = input("Ingrese su género de película preferido: ")
año_preferido = int(input("Ingrese el año mínimo de estreno de las películas que le gustan: "))

# Obtener recomendaciones de películas basadas en las preferencias del usuario
recomendaciones = recomendar_peliculas(genero_preferido, año_preferido)

# Mostrar las recomendaciones al usuario
if len(recomendaciones) == 0:
    print("Lo siento, no se encontraron películas que coincidan con sus preferencias.")
else:
    print("Recomendaciones de películas:")
    for pelicula in recomendaciones:
        print(pelicula)
