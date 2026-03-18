#peluqueria

horario = int(input("ingrese su horario de llegada (6-22): "))

if 6 <= horario <= 11:
    print("mañana")
elif 12 <= horario <= 17:
    print("tarde")
elif 18 <= horario <= 22:
    print("noche")
else:
    print("fuera de horario")