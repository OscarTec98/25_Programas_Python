#García Vázquez Oscar Daniel - 18212189
#Programa que hace uso de la libreria Math para operaciones basicas de estadistica

import math

# Función para calcular la media
def calcular_media(datos):
    suma = sum(datos)
    media = suma / len(datos)
    return media

# Función para calcular la mediana
def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    return mediana

# Función para calcular la desviación estándar
def calcular_desviacion_estandar(datos):
    media = calcular_media(datos)
    suma_cuadrados = sum((x - media) ** 2 for x in datos)
    desviacion_estandar = math.sqrt(suma_cuadrados / len(datos))
    return desviacion_estandar

# Solicitar al usuario que ingrese los valores
datos = input("Ingresa los datos separados por comas: ")

# Convertir los datos a numeros
numeros = [float(x) for x in datos.split(',')]

# Calcular la media, mediana y desviación estándar
media = calcular_media(datos)
mediana = calcular_mediana(datos)
desviacion_estandar = calcular_desviacion_estandar(datos)

# Mostrar los resultados
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)
