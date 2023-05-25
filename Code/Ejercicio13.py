#García Vázquez Oscar Daniel - 18212189
# Programa que obtiene el factorial de n numero utilizando una función

#Funcion recursiva (se manda a llamar a si misma hasta que sea necesario)
def calcular_factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)

# Pedir al usuario que ingrese un número entero positivo
numero = int(input("Ingresa un número entero : "))

# Validar que el número sea positivo
if numero < 0:
    print("El número debe ser positivo.")
else:
    # Calcular el factorial del número ingresado
    factorial = calcular_factorial(numero)
    print("El factorial de {} es: {}".format(numero, factorial))

