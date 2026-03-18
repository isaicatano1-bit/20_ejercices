#gimnacio

edad = int(input("ingrese su edad: "))

if edad <13:
    print("no puedes ingresar")
elif edad <=17:
    print("clase juvenil")
elif edad <=59:
    print("clase general")
else:
    print("senior")