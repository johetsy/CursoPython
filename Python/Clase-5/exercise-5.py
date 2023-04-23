# Escriba un programa que elimine un signo de exclamación
# del final de una cadena. puede suponer que los datos de
# entrada son siempre una cadena, no es necesario verificarlos.

string = '*-esto es una cadena de caracteres!'
delete = '!'
print(string)
print('*-debo eliminar el ! ')

for x in range(len(delete)):
    string = string.replace(delete[x], "")

print(string)
print('\n')
