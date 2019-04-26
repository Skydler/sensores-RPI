#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from matriz import Matriz
from sonido import Sonido
from temperatura import Temperatura

# Activamos los sensores que vamos a usar

matriz = Matriz()
sonido = Sonido()
temperatura = Temperatura()

def acciones():
    try:
        print ("Sonido Detectado!")
        temp_data = temperatura.datos_sensor()
        info = 'Temperatura = {0:0.1f}°C  Humedad = {1:0.1f}%'.format(temp_data['temperatura'], temp_data['humedad'])
        matriz.mostrar_mensaje(info, delay=0.01, font=2)
        matriz.dibujar_corazon()
    except:
        print("Algo salió mal O.o")
            
sonido.agregar_evento(acciones)


if __name__ == "__main__"
    while True:
        time.sleep(0.1)


""" 
	Matriz> vcc: 2
                gnd: 6
                din: 19
                cs: 24
                clk: 23
	Sonido> a0:7
                gnd: 9
                vc: 3
                d0: 15
	Temperatura> vcc: 1
                     sda: 11
                     clk: 14			
"""
