from clase16.computadora import Computadora
from clase16.monitor import Monitor
from clase16.orden import Orden
from clase16.raton import Raton
from clase16.teclado import Teclado


monitor1 = Monitor('ThinkVision', 'HDMI')
monitor2 = Monitor('Philips', 'VGA')
teclado1 = Teclado('HP', 'USB')
teclado2 = Teclado('Logitec', 'USB')
raton1 = Raton('HP', 'USB')
raton2 = Raton('Genius', 'Bluetooth')
computadora1 = Computadora('Gamer', monitor1, teclado2, raton1)
computadora2 = Computadora('Acer', monitor2, teclado1, raton2)

orden1 = Orden()
orden1.agregar_computadora(computadora1)
orden1.agregar_computadora(computadora2)
orden1.agregar_computadora(computadora1)
print(orden1)
