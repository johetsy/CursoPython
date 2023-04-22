# ====dictionary=========

empty_dict = {}
print("esto es una lista vacia...")
print(empty_dict)

# es la forma mas opmima de crear el diccionario

fullfield_dict = {
    "id": 1234561,
    "name": "Pablo"
}
print("forma optima de crear una lista")
print(fullfield_dict)

# ---------------------------
lista1 = ['a1', 'b2'],
dict_converted = dict(lista1)
print(lista1, dict_converted)

tupla_1 = ('a1', 'b2'),
print(tupla_1, dict(tupla_1))

list_dimensional = [['a', 1], ['b', 3]]
print(list_dimensional, dict(list_dimensional))

# obtener un elemento
print(fullfield_dict.get('name'))

# añadir un elemento
fullfield_dict['phone'] = '9121212122'
print(fullfield_dict)

# modificar un elemento
fullfield_dict['name'] = 'Juan'
print(fullfield_dict)

empty_dict_2 = dict()
print(empty_dict_2)

full_dict = dict(
    genero="F",
    nacionaidad="E"
)
print(full_dict)

# Hacer un diccionario, imprimirlo y luego recorrerlo uno a uno
empleado = {
    "name": "valeria",
    "apellido": "Castellano",
    "edad": 23,
    "Rut": "25.252.252-2"
}
print(empleado)

for variablex in empleado.values():
    print(variablex)
# -------------------------------------
print("========Trabajando con condicionales========")

edad = 60
if edad > 50:
    print("eres mayor de 50")

print("acá sali del if")

temperatura = 40
if temperatura >= 37:
    print("temperatura alta")
else:
    print("temperatura normal")

# -----------if doble----------
temp = 5
pais = "Chile"

if temp < 10:
    if pais == "chile":
        print("cccc")
    else:
        print("oooo")
else:
    if pais == "chile":
        print("1111")
    else:
        print("2222")

# -------------------

if temp < 10:
    print("probablemente caiga nieve")
elif temp >= 10 and temp <= 20:
    print("no es tan probable que neve")
else:
    print("No nevará")

print("========Trabajando con ciclos========")
# ---------While1----------

want_exit = "n"
while want_exit == "n":
    print("Hola, como estas?")
    want_exit = input("Quieres salir S/N?")

print("Fuera del while")

print("========Trabajando con ciclos========")
# ---------While2----------
#  break nos permite romper un ciclo
want_exit = "n"
num_questions = 0
while want_exit == "n":
    print("Hola, como estas?")
    want_exit = input("Quieres salir S/N?")
    num_questions += 1
    if num_questions == 4:
        print("Alcanzaste el maximo permitido")
        break
print("se acabó el while")
