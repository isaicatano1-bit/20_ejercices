#cafeteria
jugo = 5000
te = 3500
cafe =4000

bebidas ={
    "jugo" : jugo,
    "te" : te,
    "cafe" : cafe
}

print("BIENVENIDO")
print("")
print(bebidas)
bebida = input("que bebida desea? ")
cantidad = int(input ("cuantas unidades desea? "))
total = bebidas[bebida] * cantidad
print (total)





