producto = 0
for i in range(6):
    precio = int(input("ingrese el precio: "))

    if precio >= 100000:
        producto += 1

print("tienes",producto,"productos mayores a 100k")