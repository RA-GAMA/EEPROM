# EEPROM
Módulo de micropython simplificado para uso de una memoria EEPROM por medio del protocolo I2C

================================= ESCRITURA ===========================================
El modelo de escritura seleccionado es el de escritura aleatoria, a través de la cual se peude escribir un solo valor o una cadena de valores consecutivos, tal como:
  "registro_n, registro_n+1, ..., registro_n+n"

Para poder escribir un valor en un registro determinado, se emplea la función "writeto" del protocolo I2C.
Se escriben 3 valores específicos en una cadena, tal como:
  ( 0x0 , _registro , _valor ), donde:
    => 0x0 es el valor por defecto del protocolo I2C que indica un proceso de escritura
    => "_registro" indica el número de registro donde se almacenará el valor dado, considera que cada registro es del tamaño de 1 byte.
    => "_valor" es el valor que se desea guardar en dicho registro.

Al hacer esto, la eeprom responderá con señales de reconocimiento (Acknowledge), indicando que ha recibido cada byte transferido.

Después se cuenta la cantidad de reconocimientos y se determinal si la información fue enviada exitosamente.

================================= LECTURA ==================================================
Hay varias consideracinoes que deben tenerse al momento de leer un valor de la eeprom:

  1) Comunicación:
     La eeprom necesita notificación del deseo de leer un valor almacenaado en un registro aleatorio, por ello se escribe una cadena, tal como:
     (_registro_1, _registro_1_2), donde:
       0x01 indica el valor por defecto del protocolo I2C para indicar la intención de lecura.
       _registro indica el número del registro que se desea "leer"

  Al realizar este proceso, la eeprom prepara un "indicador" en el registro dado.

  3) Número de registro:
     Las memorias EEPROM cuentan con una gran cantidad de registros, esta cantidad peude superar fácilmente el valor máximo de 1 byte, por lo que es necesario ajustar este valor a una cadena que pueda contener dicho valor, en este caso, se considera una capacidad de 64KB, por lo que un valor doble es capaz de contener dicho valor, este valor doble se debe enviar en el proceso de intención de lectura mencionado anteriormente.

  4) Lectura de valores:
     Se pueden leer 1 o más valores después de haber notificado a la EEPROM de manera directa con la función de readfrom, del protocolo I2C, solo se debe indicar la cantidad de bytes que se desea leer.

     Nota: se puede agregar funciones para ordenamiento de bits, tal como little o big endian.
