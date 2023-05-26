#García Vázquez Oscar Daniel - 18212189

#Implementacion del algoritmo RadixSort para un conjunto de datos predefinido

def radix_sort(arr):
    # Encuentra el número máximo en la lista
    max_num = max(arr)

    # Obtiene el número de dígitos del número máximo
    num_digits = len(str(abs(max_num)))

    # Realiza el sorting basado en cada dígito, de menos significativo a más significativo
    for digit in range(num_digits):
        # Crea las listas de contenedores para cada dígito
        buckets = [[] for _ in range(10)]

        # Distribuye los números en los contenedores según el dígito actual
        for num in arr:
            digit_value = (num // (10 ** digit)) % 10
            buckets[digit_value].append(num)

        # Reasigna los números a la lista original en el orden de los contenedores
        arr = [num for bucket in buckets for num in bucket]

    return arr

def main():
    nums = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_nums = radix_sort(nums)
    print("Lista original:", nums)
    print("Lista ordenada:", sorted_nums)

if __name__ == "__main__":
    main()
