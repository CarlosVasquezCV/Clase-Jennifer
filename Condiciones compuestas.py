leche=input("¿Trajo la leche? \n Digite s o n \n ")
pan=input("Trajo el pan? \n Digite s o n \n")
huevos=input("Trajo los huevos? \n digite s o n \n ")

#Mamá estricta
if leche=="s" and pan=="s" and huevos=="s":
    print("Era lo minimo, venga y desayuna")

else:
    print("Chanclazo")

#Mamá comprensiva
if leche=="s" or pan=="s" or huevos=="s":
    print("Bueno mi amor")

else:
    print("Ayyy me va tocar ir a mi")