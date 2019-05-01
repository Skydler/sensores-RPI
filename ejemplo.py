#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import time
from matriz import Matriz
from sonido import Sonido
from temperatura import Temperatura

# Matriz --> vcc: 2, gnd: 6, din: 19, cs: 24, clk: 23
# Sonido --> a0: 7, gnd: 9, vc: 3, d0: 15
# Temperatura --> vcc: 1, sda: 11, clk: 14

# Activamos los sensores que vamos a usar

matriz = Matriz()
sonido = Sonido()
temperatura = Temperatura()

def guardar_ultima_temperatura():
    try:
        with open(os.path.join("archivos_texto", "ultimo_log_temperatura.json"), "w") as log_file:
            info_temperatura = temperatura.datos_sensor()
            json.dump(info_temperatura, log_file, indent=4)
    except:
        print("No se pudo guardar el ultimo_log :C")

def obtener_ultima_temperatura():
    try:
        with open(os.path.join("archivos_texto", "ultimo_log_temperatura.json"), "r") as log_file:
           info_temperatura = json.load(log_file) 
        return info_temperatura
    except:
        print("No se pudo obtener el ultimo_log :C")

def acciones(pin):
    print ("Sonido Detectado!")
    guardar_ultima_temperatura()
    temp_data = obtener_ultima_temperatura()
    temp_formateada = 'Temperatura = {0:0.1f}°C  Humedad = {1:0.1f}%'.format(temp_data['temperatura'], temp_data['humedad'])
        matriz.mostrar_mensaje(temp_formateada, delay=0.08, font=2)
    matriz.dibujar_corazon()
            
sonido.agregar_evento(acciones)


if __name__ == "__main__":
    while True:
        time.sleep(0.1)
