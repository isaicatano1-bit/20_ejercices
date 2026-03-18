hora = 5000
horas = int(input("cuantas horas estuvo su carro en el parqueadero? "))
if horas == 1:
    print("total a pagar $5000")
elif horas == 2:
    print("total a pagar $8000")
else:
    print("total a pagar",5000 + (3000 * (horas-1)))
