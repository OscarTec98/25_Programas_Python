#García Vázquez Oscar Daniel - 18212189
#Juego de adivinar un numero del 1 al 100 utilizando random
#Se cuenta el numero de intentos y sale del bucle una vez se atine la respuesta

import random

# Función del juego
def jugar():
    num = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número del 1 al 100. ¡Adivina cuál es!")

    while True:
        intento = int(input("Ingresa tu número: "))
        intentos += 1

        if intento < num:
            print("Demasiado bajo. ¡Intenta nuevamente!")
        elif intento > num:
            print("Demasiado alto. ¡Intenta nuevamente!")
        else:
            print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
            break

# Jugar al juego de adivinanzas
jugar()
