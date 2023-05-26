#García Vázquez Oscar Daniel - 18212189
#Programa que simula un sistema de compras con un conjunto de productos establecido con sus valores
#Permite agregar productos al carrito
#Ver todos los productos y los productos en el carrito
#finalizar la compra y salir del programa


#Objetos del tipo clave-valor
productos = [
    {"nombre": "Camisa", "precio": 25.99},
    {"nombre": "Pantalón", "precio": 39.99},
    {"nombre": "Zapatos", "precio": 59.99},
    {"nombre": "Bolso", "precio": 19.99},
    {"nombre": "Gorra", "precio": 9.99}
]
#Lista de productos del cliente
carrito = []


def mostrar_productos():
    print("Productos disponibles:")
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto['nombre']} - ${producto['precio']:.2f}")

        #Agrega un producto al carrito del cliente
def agregar_producto():
    mostrar_productos()
    opcion = int(input("Selecciona el número del producto que deseas agregar al carrito: "))

    if opcion < 1 or opcion > len(productos):
        print("Opción inválida. Intenta nuevamente.")
        return

    producto_seleccionado = productos[opcion-1]
    carrito.append(producto_seleccionado)
    print(f"¡Se agregó {producto_seleccionado['nombre']} al carrito!")

    
def mostrar_carrito():
    total = 0
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        print("Carrito:")
        for producto in carrito:
            print(f"{producto['nombre']} - ${producto['precio']:.2f}")
            total += producto['precio']
        print(f"Total a pagar: ${total:.2f}")

        #Finaliza la simulacion de la compra y limpia el carrito
def finalizar_compra():
    mostrar_carrito()
    confirmacion = input("¿Deseas confirmar la compra? (S/N): ")

    if confirmacion.lower() == "s":
      
        print("¡Compra realizada exitosamente!")
        carrito.clear()
    else:
        print("La compra ha sido cancelada.")

# Menú principal
while True:
    print("\n------ TIENDA ONLINE ------")
    print("1. Mostrar productos")
    print("2. Agregar producto al carrito")
    print("3. Mostrar carrito")
    print("4. Finalizar compra")
    print("5. Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        mostrar_productos()
    elif opcion == 2:
        agregar_producto()
    elif opcion == 3:
        mostrar_carrito()
    elif opcion == 4:
        finalizar_compra()
    elif opcion == 5:
        print("¡Gracias por visitar nuestra tienda! ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")
