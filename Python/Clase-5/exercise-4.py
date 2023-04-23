# Dado un mes como un número entero del 1 al 12,
# devuelva a qué trimestre del año pertenece como un número entero.
# Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre
# el mes 6 (junio),# forma parte del segundo trimestre
# y el mes 11 (noviembre), forma parte del cuarto trimestre.

mes = int(input('Ingresa el numero del mes: '))

if mes > 0 and mes < 13:
    if mes < 4:
        print('el mes: ', mes, ' pertenece al primer trimestre\n')

    if mes > 3 and mes < 7:
        print('el mes: ', mes, ' pertenece al segundo trimestre \n')

    if mes > 6 and mes < 10:
        print('el mes: ', mes, ' pertenece al tercer trimestre \n')

    if mes > 9:
        print('el mes: ', mes, ' pertenece alcuarto trimestre \n')

else:
    print(" El mes debe ser entre 1 y 12 \n")
