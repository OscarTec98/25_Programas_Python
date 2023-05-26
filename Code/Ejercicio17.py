#García Vázquez Oscar Daniel - 18212189
#Programa que realiza operaciones basicas con  matrices
#Suma, resta y multiplicación utilizando numpy

import numpy as np

# Suma de dos matrices
def sumar_matrices(matriz1, matriz2):
    resultado = np.add(matriz1, matriz2)
    return resultado

# Resta de dos matrices
def restar_matrices(matriz1, matriz2):
    resultado = np.subtract(matriz1, matriz2)
    return resultado

# Multiplicar dos matrices
def multiplicar_matrices(matriz1, matriz2):
    resultado = np.dot(matriz1, matriz2)
    return resultado

# Matrices de ejemplo para la practica
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Sumar las matrices
resultado_suma = sumar_matrices(matriz1, matriz2)

# Restar las matrices
resultado_resta = restar_matrices(matriz1, matriz2)

# Multiplicar las matrices
resultado_multiplicacion = multiplicar_matrices(matriz1, matriz2)

# Mostrar los resultados
print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)
print("\nResultado de la suma:")
print(resultado_suma)
print("\nResultado de la resta:")
print(resultado_resta)
print("\nResultado de la multiplicación:")
print(resultado_multiplicacion)

