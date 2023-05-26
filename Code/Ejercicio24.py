#García Vázquez Oscar Daniel - 18212189

#Algoritmo que implementa el MergeSort de una lista de valores predefinidos para demostrar la función

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente ordenar las mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combinar las mitades ordenadas
    merged = merge(left_half, right_half)

    return merged

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Combinar los elementos en orden ascendente
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Agregar los elementos restantes de la mitad izquierda
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Agregar los elementos restantes de la mitad derecha
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Ejemplo de uso
arr = [5, 2, 8, 3, 1, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)
