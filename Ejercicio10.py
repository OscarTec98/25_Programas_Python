#Programa que se detiene una vez que el usuario ingrese el numero 0
numero = 0

while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        print("Ha ingresado el número 0. Saliendo del programa...")
        break
    elif numero < 0:
        print("El número es negativo. Vuelva a ingresar un número positivo.")
        continue
    else:
        print(f"El número ingresado es: {numero}")
