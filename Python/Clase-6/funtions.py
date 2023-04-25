print('\n- def saludar------\n')


def saludar(name):
    print(f'Hola {name} !!!')


saludar('Rodrigo')
saludar('Richard')


print('\n---def saludar_dos-----\n')


def saludar_dos(first_name, last_name):
    print(f'Hola {first_name}, {last_name} !!!')


# se hace para asegurar la posicion de los valores
saludar_dos(last_name='Alvarez', first_name='Johetsy')


print('\n----def multiplicar texto-------\n')


def multiplicar_texto(texto, multiplier=2):
    print(texto * multiplier)


multiplicar_texto('V', 5)

multiplicar_texto('x')  # lo va a multiplicar de acuerdo al parámetro
# que se le haya puesto en este caso sería 2
# que está en la linea 17

print('\n------def varietal-----------\n')


def varietal(param1, param2, *others):
    print(param1)
    print(param2)
    print(others)


varietal('1A', '2B', 0, 'XX', [0, 1])


print('\n---def varietal2-----------\n')


def varietal2(param1, **others):
    print(param1)
    print(others)


varietal2('1A', id=0, name='Carlos')

print('\n-----------------\n')
