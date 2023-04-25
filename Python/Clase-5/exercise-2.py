# utilizando dos while anidados, construya las tablas
# de mutiplicacion, ejemplo
# Ejemplo while anidados:
#     while codicion1
#     while codicion2
#     .....

table = 1
num = 0
while table <= 9:
    print()
    print('tabla del ', table)
    while num <= 9:
        print(table, 'x', num, '=', table*num)
        num += 1
    table += 1
    num -= 9


# -----------------utilizando for----------------
# print('\n-----Tablas de Multiplicar-----')

# for num_tabla in range(1, 11):
#     for num_mul in range(1, 10):
#         result = num_tabla * num_mul
#         print(f'{num_tabla} x {num_mul} = {result}')
#     print('-----------------\n')
