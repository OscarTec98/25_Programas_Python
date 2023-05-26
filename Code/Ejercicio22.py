#García Vázquez Oscar Daniel - 18212189
#Programa que implementa un sistema de gestion de inventarios
#Permite ver, agregar, eliminar productos guardados en una base de datos
#A su vez se pueden realizar modificaciones sin menú solo es la lógica
inventario = {}

def agregar_producto(codigo, nombre, precio, cantidad):
    if codigo in inventario:
        print("Producto ya existente.")
    else:
        inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        print("Producto agregado correctamente.")

def eliminar_producto(codigo):
    if codigo in inventario:
        del inventario[codigo]
        print("Producto eliminado correctamente.")
    else:
        print("Error: El producto no existe en el inventario.")

def actualizar_precio(codigo, nuevo_precio):
    if codigo in inventario:
        inventario[codigo]["precio"] = nuevo_precio
        print("Precio actualizado correctamente.")
    else:
        print("Error: El producto no existe en el inventario.")

def actualizar_cantidad(codigo, cantidad):
    if codigo in inventario:
        inventario[codigo]["cantidad"] += cantidad
        print("Cantidad actualizada correctamente.")
    else:
        print("Error: El producto no existe en el inventario.")

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for codigo, producto in inventario.items():
            print(f"Código: {codigo}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

# Agregar productos al inventario
agregar_producto("P001", "Camiseta", 20.99, 50)
agregar_producto("P002", "Pantalón", 39.99, 30)
agregar_producto("P003", "Zapatos", 59.99, 20)

# Actualizar precio de un producto
actualizar_precio("P001", 22.99)

# Actualizar cantidad de un producto
actualizar_cantidad("P002", 10)

# Mostrar inventario
mostrar_inventario()

# Eliminar un producto del inventario
eliminar_producto("P003")

# Mostrar inventario actualizado
mostrar_inventario()

