# 1. Cree un programa que encuentre el promedio de los tres
# puntajes dados y devuelva el valor de la letra asociada
# con esa calificación. con al siguiente tabla
# 0   - 2     D
# 2.1 - 5     C
# 5.1 - 6     B
# 6.1 - 7     A

nota_1 = float(input('Ingresa la nota 1: '))
nota_2 = float(input('Ingresa la nota 2: '))
nota_3 = float(input('Ingresa la nota 3: '))

promedio = (nota_1 + nota_2 + nota_3)/3

if promedio >= 0 and promedio < 8:
    if promedio <= 2:
        print('NOTA = D')

    if promedio > 2 and promedio <= 5:
        print('NOTA = C')

    if promedio > 5 and promedio <= 6:
        print('NOTA = B')

    if promedio > 6 and promedio <= 7:
        print('NOTA = A')
    print('El promedio de las 3 notas es:', round(promedio, 2))
else:
    print('Las notas no estan dentro del rango')
