first_name = "Johetsy"
last_name = "Alvarez"
print(first_name + " " + last_name)
mensaje1 = "Hola " * 3
print(mensaje1)

mensaje2 = "Sebastian"
print(mensaje2)
mensaje2 += ","
print(mensaje2)
mensaje2 += " Alvarez"
print(mensaje2)

print(len(mensaje2))

cadena = "esto es una cadena de caracteres"
posicion = cadena.find("pelo")
print("camisa se encuentra en: ", posicion)
posicion = cadena.find("cadena")
print("cadena se encuentra en: ", posicion)

hola = "HOLA YO ESTOY EN MAYUSCULAS"
hola_lower = hola.lower()
print(hola_lower)

hola = hola.replace("MAYUSCULA", "minuscula")
print(hola)

print("===== LISTAS=====")

empty_list = []
print(empty_list)

full_list = [1, 3, 500, 1.4, [2, "a"], {"name": "Johetsy"}, (1, 3, 5)]
print(full_list)

# imprime la palabra letra por letra
print(list("concurso"))

# imprime una lista de uno en uno
range_one = range(10)
print(list(range_one))

# imprime una lista
numeros = [1, 4, 6]
print(numeros)

# agrega items a la lista ejemplo el 10 al final de la lista
numeros.append(10)
print(numeros)

# imprime la posicion 2
print(numeros[2])

# iterar lista
lista_iterada = [1, 2, 3, 4, 5, 6]
for y in lista_iterada:
    print(y)

# eliminar un valor de la lista en esete caso el numero 4
# elimina por posicion lista.pop(posicion)
numeros.remove(4)
print(numeros)

# modificar lista lista[posicion]=nuevo_valor
numeros[0] = 5
print(numeros)

# reverse() los cambia el orden de los elementos
lista_rev = ["cuaderno", "lapiz", "borra"]
lista_rev.reverse()
print(lista_rev)

# extend() une ambas listas
lista_ext1 = [1, 2, 3]
lista_ext2 = [4, 5, 6]
lista_ext1.extend(lista_ext2)
print(lista_ext1)

# append() agrega un elemento
lista_app = ["perro", "gato", "ratón"]
lista_app.append("animales")
print(lista_app)


print("=====TUPLAS=====")

empty_tuple = ()
fullfiled_tuple = (1, "johetsy", 500.87)

print(empty_tuple, fullfiled_tuple)

one_tuple = ("juan",)
print(type(one_tuple))

# se puede declarar una tupla si usar parentesis, funciona, pero esto es una mala pratica
hojas = "carta", "oficio"
print(type(hojas))
print(hojas)

empty_tuple_2 = tuple()
print(empty_tuple_2)

list_to_convert = [2, 6, 8, 9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)

# reverse(), append(), extend() remove() clear() sort()

# sort() ordena los elementos
numeros = [16, 4, 9, 3]
numeros.sort()
print(numeros)
