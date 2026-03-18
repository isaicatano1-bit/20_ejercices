#heladeria
cono = 3000
vaso = 4000
banana_split = 9000
its_ok = True
contador_cliente = 0
productos ={
    "cono" : cono,
    "vaso" : vaso,
    "banana split" : banana_split
}
contador_productos ={
    "cono" : 0,
    "vaso" : 0,
    "banana split" : 0
}
while its_ok:
    contador_cliente +=1
    print(productos)
    producto = input("que helado desea? ")
    cantidad = int(input("cuantos helados? "))       
    total = productos[producto] * cantidad
    print(total)
    contador_productos[producto] += cantidad
    mas_ventas = input("desea agregar otra venta? (si/no) ").lower()
    print("------------------------------------------")
    if mas_ventas == "no":
        its_ok = False

print("total de clientes atendidos: ",contador_cliente)
print("")
print("----------------------------------------------")
print("cantidad de veces que se vendio un producto: ")
for producto, cantidad in contador_productos.items():
    print(f"-{producto}: {cantidad}")
print("----------------------------------------------")