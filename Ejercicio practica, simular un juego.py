from random import randint

print("---------JuegosDivertidos.com-----------")
print()
print()
print()
#-----------------------------------------------------
a=randint(0,1)

print("Juguemos a un juego!")
caraSello=int(input(" ¿Cara o sello?\n 1.Cara\n 2.Sello"))
a=randint(1,2)

if a==caraSello:
    print("Resultado: Ganaste!")
else:
    print("Resultado: Perdiste!")



print(a)