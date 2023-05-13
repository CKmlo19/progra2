import os 
from pathlib import Path

mazo_global = open("/home/camilo/Downloads/Mazo.txt", encoding="utf-8")

def iniciar_juego():
    """Funcion que inicia el juego"""
    mazo = cargar_mazo(mazo_global)

def cargar_mazo(mazo_global):
    contenido_mazo = mazo_global.read()
    return contenido_mazo

def separar_mazo_matriz(contenido):
    '''Funcion que separar el mazo en contenido'''
