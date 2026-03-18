asistencia = int(input("ingrese sus asistencias al mes: "))

if asistencia <5:
    print("asistencia baja")
elif asistencia <=8:
    print("asistencia media")
else:
    print("asistencia alta")