# Cree una función notaFinal, que calcule la nota final de un estudiante en función de dos parámetros:
# una nota para el examen y una cantidad de proyectos completados.
# Esta función debe tomar dos argumentos: examen - calificación del examen(de 0 a 100)
# proyectos - número de proyectos completados(de 0 en adelante)
# Esta función debería devolver un número(calificación final).
# Hay cuatro tipos de calificaciones finales:
#     100, si la calificación del examen es superior a 90 o si el número de proyectos terminados es superior a 10.
#     90, si la calificación del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
#     75, si la calificación del examen es superior a 50 y si el número de proyectos completados es mínimo 2.


examen = int(input('Ingresa la nota del examen: '))
proyectos = int(input('Ingresa cantidad de proyectos completados: '))

if examen > 90 or proyectos > 10:
    print('nota 100')
elif (examen > 75 and examen < 91) and proyectos >= 5:
    print('nota 90')
elif examen > 50 and proyectos >= 2:
    print('nota 75')
else:
    print('su calificacion esta por debajo del minimo')
