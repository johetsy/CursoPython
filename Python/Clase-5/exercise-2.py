# utilizando dos while anidados, construya las tablas
# de mutiplicacion, ejemplo
# Ejemplo while anidados:
#     while codicion1
#     while codicion2
#     .....

table = 0
num = 0
while table <= 9:
    print('tabla del ', table)
    while num <= 9:
        print(table, 'x', num, '=', table*num)
        num += 1
    table += 1
    num -= 9
