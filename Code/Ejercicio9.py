#García Vázquez Oscar Daniel - 18212189

#Programa que determina la categoria de edad en que se encuentra el usuario.
edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Eres menor de edad")
else:
    if edad < 65:
        print("Eres adulto")
    else:
        print("Eres adulto mayor")
