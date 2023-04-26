# Creando una clase se usa UpperCamelCase
class Transporte:
    pass


# Instaciar (llamar)la clases y crear un objeto
transporte1 = Transporte()
transporte2 = Transporte()


class BuzzeLigthYear:
    pass


bozz1 = BuzzeLigthYear()
bozz2 = BuzzeLigthYear()

print(type(transporte1))
print(type(bozz1))

# creamos una clase
# todos los atributos deben tener este self que
# significa que es parte de el mismo, encapsulamiento


class Droid:
    def __init__(self):  # método constructor de la clase
        self.power_on = False   # se coloca lo que queremos que esté por defecto
        # cuando se inicialice

    def switch_on(self):  # agregamos metodos
        print("Hola soy un droid, y estoy a tu orden")
        self.power_on = True  # para que se active cuando lo encienden

    def switch_off(self):
        print("Adios, enciendeme, cuando me necesites")
        self.power_on = False  # para que se desactive cuando lo apagan


k8_arthur = Droid()  # instaciamos la clase para producir droid y todo lo
k8_citripio = Droid()  # que la clase contiene pasa a ser parte de la variable
# k8 artur

k8_arthur.switch_on()  # entonces cuando se enciende imprime esto
print("power on Arthur: ", k8_arthur.power_on)
print("power on Citripio: ", k8_citripio.power_on)
k8_arthur.switch_off()  # cuanando se apaga imprime esto
print(k8_arthur.power_on)


class Vehicle:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model


sedan = Vehicle('Sedan', 'Aveo')
print(sedan.type_vehicle, sedan.model_vehicle)
pickup = Vehicle('Pickup', 'Ranger')
print(pickup.type_vehicle, pickup.model_vehicle)
