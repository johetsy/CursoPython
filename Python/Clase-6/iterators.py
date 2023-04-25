print('\n----print words-------------')

words = 'Esto es una cadena de texto '

word = ''
for letter in words:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = ''

print('\n--Imprime la primera palabra antes del espacio-----')

for letter in words:
    if letter != ' ':
        print(letter)
    else:
        break

print('\n-------lista---------')

animals_list = ['Gato', 'Perro', 'Pajaro', 'Ardilla']
for animal in animals_list:
    print(animal)

print('\n------lista rangos-------')

list1 = range(2, 3)  # [0,1,2,3]
print(list1)
for number in range(1, 10):
    print(number)

print('\n-------lista rango 2--------')

list1 = range(2, 3)  # [0,1,2,3]
print(list1)
for number_in in range(1, 10, 2):
    print(number_in)

print('\n-----Tablas de Multiplicar-----')

for num_tabla in range(1, 11):
    for num_mul in range(1, 10):
        result = num_tabla * num_mul
        print(f'{num_tabla} x {num_mul} = {result}')
    print('-----------------\n')

print('\n-----Arreglos Bidimensionales------')

double_list = [[1, 2, 3], [4, 6, 7]]

print(double_list[0])  # imprime la lista 1 [1, 2, 3]
print(double_list[1])  # imprime la lista 2 [4, 6, 7]

print(double_list[0][2])  # imprime la segunda posicion de la lista 1 [3]
print(double_list[1][1])  # imprime la primera posicion de la lista 2 [6]

# double_list[0].pop()  # imprime la lista 2
