#García Vázquez Oscar Daniel - 18212189
#Programa que realiza el promedio de una lista de datos ingresada por el usuario (separados por coma) 
#Los cuales son transformados a su valor float para realizar los calculos
#De la lista de valores se obtiene el valor maximo y minimo y se despliegan los resultados



# Solicitar al usuario que ingrese una lista de números separados por comas
numeros = input("Ingresa una lista de números separados por comas: ")

# Convertir la cadena de entrada en una lista de números
lista_numeros = [float(numero) for numero in numeros.split(",")]

# Calcular el promedio de los números
suma = 0
for numero in lista_numeros:
    suma += numero

promedio = suma / len(lista_numeros)

# Encontrar el número máximo y mínimo
maximo = max(lista_numeros)
minimo = min(lista_numeros)

# Imprimir los resultados
print("Lista de números:", lista_numeros)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
