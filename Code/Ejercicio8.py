#García Vázquez Oscar Daniel - 18212189

#Programa que imprime el numero de segundos segun los DIAS, HORAS, MINUTOS Y SEGUNDOS dados por el USUARIO
SEC_DIA = 24*60*60
SEC_HORA = 60 * 60
SEC_MIN = 60

D = int(input("INGRESA LOS DIAS"))
H = int(input("INGRESA LAS HORAS"))
M = int(input("INGRESA LOS MINUTOS"))
S = int(input("INGRESA LOS SEGUNDOS"))

TotalS = S + M * SEC_MIN + H * SEC_HORA + D * SEC_DIA

print(f"Hay {TotalS} SEGUNDOS en: {D} Dias,{H} Horas,{M} Minutos con {S} Segundos")
