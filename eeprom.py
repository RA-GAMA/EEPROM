'''Módulo de control simple para EEPROM por protocolo I2C

Ra-GAMA - 2024.
'''

from machine import Pin, SoftI2C, I2C

class EEPROM:
    def __init__(self,_i2c:SoftI2C=None,_dir:int=0x50):
        '''crea un nuevo objeto de control para la memoria
            _i2c = Protocolo i2c
            _dir = Dirección de la memoria
        '''
        if _i2c==None:
            self.i2c = SoftI2C(sda=Pin(21),scl=Pin(22))
        else:
            if type(_i2c)==SoftI2C or type(_i2c)==I2C:
                self.i2c = _i2c
            else:
                raise RuntimeError('Error al generar el protocolo I2C')
        # Busca el dispositivo con la dirección dada
        encontrado = False
        for f in self.i2c.scan():
            if f==_dir: 
                self.direccion = _dir   # establece la dirección del dispositivo
                encontrado = True       # marca el cambio de estado
                break                   # termina el ciclo.
        if not encontrado:
            raise RuntimeError('No se pudo localiza el dispositivo con dirección {:02x}')
    
    def __setitem__(self,_dir:int,_valor:int):
        '''establece el valor dado en la dirección especificada
            _dir = Dirección de la memoria
            _valor = Valor a guardar (numérico)
        '''
        # guarda el número de bytes reconocidos, debe coincidir con la cantidad de bytes enviados (3)
        reconocimiento = self.i2c.writeto(self.direccion,bytes([0,_dir,_valor]))
        if reconocimiento !=3:  # error desconocido
            raise RuntimeError('Error al guardar los datos. Volver a interntar')
    
    def __getitem__(self,_dir:int):
        '''devuelve un valor almacenado en la eeprom, en la dirección establecida.
            _dir = Dirección de la memoria
        '''
        self.i2c.writeto(self.direccion,bytes([_dir>>8,_dir&0xff]))
        return self.i2c.readfrom(self.direccion,1)[0]
