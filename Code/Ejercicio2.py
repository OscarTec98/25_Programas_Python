#García Vázquez Oscar Daniel - 18212189

#Programa que muestra la tabla de potencias del 2 que NO exceda del 1000
x = 0
y = 0
while True:

    x = 2**y
    if x >= 1000:
        break
    print(x)
    y+=1
    
        
    
