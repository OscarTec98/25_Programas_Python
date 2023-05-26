#García Vázquez Oscar Daniel - 18212189

#Programa que muestra la suma y el producto de todos los numeros pares entre 15 y 20

numeros = [15,16,17,18,19,20]
suma = 0
producto = 0
for num in numeros:
    if num %2== 0:
        suma += num
        producto *= num
    
print("Suma: " +suma)
print("Multiplicacion: " + producto)
