  # en caso de requerir objetos de control globales:
from machine import Pin, SoftI2C
  # importación del módulo
from eeprom import EEPROM

  # declaración del protocolo I2C
i2c = SoftI2C(sda=Pin(21),scl=Pin(22))
  # declaración de la memoria EEPROM
memo = EEPROM(i2c)

  # prepara un registro donde guardar o leer un valor
registro = 0 # {0,1,2, ... , 65535}
valor = 5    # {0,1,2, ... , 255}
  # Para guardar un valor en la memoria:
memo[registro] = valor
print('Se ha guardado el valor {} en el registro {} de la EEPROM'.format(valor,registro))

  # Para leer un valor de la memoria:
valor = memo[registro]
print('Se ha leído el valor {} del registro {} de la EEPROM'.format(valor,registro))
