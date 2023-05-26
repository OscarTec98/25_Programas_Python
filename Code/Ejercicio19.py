#García Vázquez Oscar Daniel - 18212189

#Programa que obtiene la probabilidad de sacar cierta probabiliad al tirar dados
#Se cuenta las veces que cae la combinacion deseada en un nuemro de intentos dados por default
#utilizado random

import random

# Función dados
def lanzamiento_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Función para calcular la probabilidad de obtener una combinación específica
def calcular_probabilidad(n, combinacion):
    contador = 0
    lanzamientos_totales = n

    for _ in range(n):
        dado1, dado2 = lanzamiento_dados()

        if dado1 == combinacion[0] and dado2 == combinacion[1]:
            contador += 1

    probabilidad = contador / lanzamientos_totales
    return probabilidad

# Datos de ejemplo
n_lanzamientos = 100000
combinacion_interes = (6, 6)

# Calcular la probabilidad de obtener la combinación deseada
probabilidad_combinacion = calcular_probabilidad(n_lanzamientos, combinacion_interes)

# Mostrar el resultado
print(f"La probabilidad de obtener la combinación {combinacion_interes} es: {probabilidad_combinacion}")
