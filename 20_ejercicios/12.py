"""2. Gimnasio: promedio de rendimiento semanal
Registrar 5 personas en un gimnasio.
 Por cada una pedir:
    • nombre
    • días asistidos en la semana
    • minutos promedio entrenados por día
Clasificar:
    • menos de 3 días → bajo compromiso
    • 3 a 4 días → compromiso medio
    • 5 o más → compromiso alto
Al final mostrar cuántas personas quedaron en cada categoría.
Practica: ciclos, contadores, condicionales."""
lista_personas=[]
for i in range (5):
    nombre =input("digite su nombre: ")
    dias = int(input("cantidad de dias asistidos por semana? "))
    minutos= int(input("cantidad de minutos por dia: "))
    if dias < 3:
     print("bajo compromiso")
    elif 3> dias < 4:
     print("compromiso medio")
    else:
     print("compromiso alto")
    print("-------------------------------------------")

personas ={
    "nombre" : nombre,
    "dias" : dias,
    "minutos" : minutos
}
lista_personas.append(personas)

if dias < 3:
    print("bajo compromiso")
elif 3> dias < 4:
    print("compromiso medio")
else:
    print("compromiso alto")

print(lista_personas)
