#Programa que comprueba si es posible realizar una división

# Se deben ingresar dos numeros
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Se realizan unos calculos basicos para manipular los datos ingresado
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Se muestran los resultado en pantalla
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)

# Se intenta hacer la división por 0
if numero2 != 0:
    division = numero1 / numero2
    print("División:", division)
else:
    print("No es posible dividir por cero.")
