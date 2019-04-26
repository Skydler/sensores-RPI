#!/usr/bin/python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

"""
A0  --> pin 7
VCC --> pin 2
GND --> pin 6
D0  --> pin 11 (BCM17)
"""

class Sonido:
    
    def __init_(self, canal=17)
        self._canal = canal
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._canal, GPIO.IN)
        # Desactivo las warnings por tener más de un circuito en la GPIO
        GPIO.setwarnings(False)

    def agregar_evento(self, funcion):
        GPIO.add_event_detect(canal, GPIO.BOTH, callback=funcion, bouncetime=300) 

if __name__ == "__main__":

    def test():
        print('Sonido detectado!')
    

    sonido = Sonido()
    sonido.agregar_evento(test)
    while True:
        time.sleep(0.5)

    GPIO.cleanup()
