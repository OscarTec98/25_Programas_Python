#Garcia Vazquez Oscar Daniel - 18212189

#Programa que permite al usuario crear un usuario, mostrar a todos los usuarios registrados en una lista
#Buscar usuario por nombre y por ultimo al salir del programa ya que se encuentra en un bucle while

# Lista de empleados
empleados = []

# Función para agregar un empleado
def agregar_empleado():
    nombre = input("Ingresa el nombre del empleado: ")
    edad = int(input("Ingresa la edad del empleado: "))
    salario = float(input("Ingresa el salario del empleado: "))

    empleado = {"nombre": nombre, "edad": edad, "salario": salario}
    empleados.append(empleado)

# Función para mostrar la información de los empleados
def mostrar_empleados():
    if len(empleados) == 0:
        print("No hay empleados registrados.")
    else:
        print("Lista de empleados:")
        for empleado in empleados:
            print("Nombre:", empleado["nombre"])
            print("Edad:", empleado["edad"])
            print("Salario:", empleado["salario"])
            print("-----------------------")

# Función para buscar un empleado por nombre
def buscar_empleado():
    nombre_buscar = input("Ingresa el nombre del empleado a buscar: ")

    for empleado in empleados:
        if empleado["nombre"] == nombre_buscar:
            print("Empleado encontrado:")
            print("Nombre:", empleado["nombre"])
            print("Edad:", empleado["edad"])
            print("Salario:", empleado["salario"])
            return

    print("No se encontró ningún empleado con ese nombre.")

# Menú principal
while True:
    print("----- Menú Principal -----")
    print("1. Agregar empleado")
    print("2. Mostrar empleados")
    print("3. Buscar empleado")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_empleado()
    elif opcion == "2":
        mostrar_empleados()
    elif opcion == "3":
        buscar_empleado()
    elif opcion == "4":
        break
    else:
        print("Inténtalo nuevamente.")

print("ADIOS.")
