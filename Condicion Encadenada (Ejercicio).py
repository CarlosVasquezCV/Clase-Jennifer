print("...........BIENVENIDOS A PLAYLAND..............")
print()
print()

nombre=input("¿Cuál es tu nombre? ")
edad=int(input("¿Cuál es tu edad? "))


if edad < 4:
    print(nombre, "puedes entrar gratis!")
elif 5<=edad<17:
    print(nombre, "Debes pagar 20.000")
elif 18<=edad<=60:
    print(nombre, "debes pagar 15.000")
else:
    print(nombre, "debes pagar 3.000")

