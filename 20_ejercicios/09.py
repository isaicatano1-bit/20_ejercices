servicios = {"facial","masaje","manicure"}
print(servicios)
recepcion = input("que servicio desea hacerse? ")

if recepcion in servicios:
    print("servicio existente")
else:
    print("servicio no existente")