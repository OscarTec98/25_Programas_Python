#Garcia Vazquez Oscar Daniel - 18212189
#Programa que calcula la suma de los numeros primos menos al numero ingresado por el usuario

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

# Función para calcular la suma de los números primos menores que un número dado
def suma_numeros_primos(numero):
    suma = 0

    for i in range(2, numero):
        if es_primo(i):
            suma += i

    return suma

# Pedir número al usuario
numero = int(input("Ingresa un número: "))

# Calcular la suma de los números primos
suma = suma_numeros_primos(numero)

# Mostrar el resultado
print("La suma de los números primos menores que", numero, "es:", suma)
