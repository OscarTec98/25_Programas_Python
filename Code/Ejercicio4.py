#García Vázquez Oscar Daniel - 18212189

#Programa que muestra en pantalla las tablas desde 1 hasta 12

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = 1

while y <= 12:
    for num in x:
        res = num * y
        print(f"{y} * {num} = {res}" )
    y += 1
