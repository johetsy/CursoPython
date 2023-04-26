# Escriba una clase MobilePhone que represente un teléfono móvil

# Atributos:
#     .- manufacturer (cadena de texto)
#     .- screen_size (flotante)
#     .- num_cores (entero)
#     .- apps (lista de cadena de texto)
#     .- status (False: apagado, True:encendido)
# Métodos:
#     . __init__(self, manufacturer, screen_size, num_cores)
#     . power_on(self)
#     . power_off(self)
#     . install_app(self, app)
#     . uninstall_app(self, app)
# ////////////////////////////////


class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, app: str):
        self.apps.append(app)

    def uninstall_app(self, app: str):
        if app in self.apps:
            self.apps.remove(app)


cellphone = MobilePhone('Samsung', 6.4, 8)

cellphone.power_on()
print()
print('Hola, has encendido tu telefono', cellphone.manufacturer, ', Pantalla:',
      cellphone.screen_size, ', Cores:', cellphone.num_cores, '\n')

cellphone.install_app('Twitter')
cellphone.install_app('Facebook')
cellphone.install_app('Whatsapp')
print('Instalaste:', cellphone.apps, 'en tu telefono\n')

cellphone.uninstall_app('Twitter')
print('Eliminaste Twiter de tu telefono, solo quedan', cellphone.apps)


cellphone.power_off
print('\n Hasta pronto')
