# Escriba un programa que calcule el máximo común
# divisor entre dos números enteros.
# usaré la función math de la libreria de python
# gcd =greatest commun divisor

import math

num_1 = int(input('Ingresa primer numero: '))
num_2 = int(input('Ingresa segundo numero: '))
a = math.gcd(num_1, num_2)
print('\n El máximo común divisor es: ', a)
print('\n')
