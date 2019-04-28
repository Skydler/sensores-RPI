#!/usr/bin/python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

"""
A0  --> pin 7
VCC --> pin 2
GND --> pin 6
D0  --> pin 15 (BCM22)
"""

class Sonido:
    
    def __init__(self, canal=22):
        self._canal = canal
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._canal, GPIO.IN)
        # Desactivo las warnings por tener más de un circuito en la GPIO
        GPIO.setwarnings(False)

    def agregar_evento(self,funcion):
        GPIO.add_event_detect(self._canal, GPIO.BOTH, callback=funcion, bouncetime=200)
        

if __name__ == "__main__":
    import time
    """ La funcion que vayamos a usar cuando detecte sonido necesita un parametro de cual es el pin al que esta conectado """
    def test(pin):
        print('Sonido detectado!')
    

    sonido = Sonido()
    sonido.agregar_evento(test)
    while True:
        time.sleep(0.0001)

    GPIO.cleanup()
