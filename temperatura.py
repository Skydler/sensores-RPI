# -*- coding: utf-8 -*-
import sys
import time
import Adafruit_DHT

"""
Conección One-Wire:
Resistencia 10K entre VCC y DATA
1er pin del sensor al VCC 3,3V
2do pin del sensor DATA al BCM 17( pin numero 11 de la raspberry)
4to pin del sensor al GND de la raspberry
"""

# Usamos el DHT11 que es compatible con el DHT12 
sensor = Adafruit_DHT.DHT11
pin = 17

def datos_sensor(sensor,pin):
  """ devuelve un diccionario con la temperatura y humedad"""
  humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
  return {'temperatura': temperatura, 'humedad': humedad}
 

if __name__ == "__main__":
    while True:
        datos = datosSensor(sensor,pin)
        # Imprime en la consola las variables temperatura y humedad con un decimal
        print('Temperatura = {0:0.1f}°C  Humedad = {1:0.1f}%'.format(datos['temperatura'], datos['humedad']))
        time.sleep(0.5)
