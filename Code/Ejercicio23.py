#García Vázquez Oscar Daniel - 18212189

#Sistema de gestion de una tienda de animales utilizando clases e instancias de objetos.
#Permite crear la tienda de mascotas y usar el objeto para realizar la gstión de las mascotas.

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class TiendaMascotas:
    def __init__(self):
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print("Mascota agregada correctamente.")

    def buscar_mascota(self, nombre):
        for mascota in self.mascotas:
            if mascota.nombre == nombre:
                return mascota
        return None

    def mostrar_mascotas(self):
        if len(self.mascotas) == 0:
            print("La tienda no tiene mascotas en este momento.")
        else:
            print("Mascotas en la tienda:")
            for mascota in self.mascotas:
                print(f"Nombre: {mascota.nombre}, Especie: {mascota.especie}, Edad: {mascota.edad}")

# Instancia de la clase tienda de mascotas
tienda = TiendaMascotas()

# Agregar mascotas a la tienda
mascota1 = Mascota("Max", "Perro", 2)
tienda.agregar_mascota(mascota1)

mascota2 = Mascota("Luna", "Gato", 1)
tienda.agregar_mascota(mascota2)

# Mostrar las mascotas en la tienda
tienda.mostrar_mascotas()

# Buscar una mascota por nombre
nombre_mascota = input("Ingresa el nombre de la mascota a buscar: ")
mascota_encontrada = tienda.buscar_mascota(nombre_mascota)
if mascota_encontrada:
    print(f"Se encontró a la mascota: Nombre: {mascota_encontrada.nombre}, Especie: {mascota_encontrada.especie}, Edad: {mascota_encontrada.edad}")
else:
    print("No se encontró ninguna mascota con ese nombre.")
