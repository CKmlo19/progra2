import os 
import sys
from pathlib import Path
sys.setrecursionlimit(10000000)

mazo_global = open("/home/camilo/Downloads/Mazo.txt", encoding="utf-8")

def iniciar_juego():
    """Funcion que inicia el juego"""
    mazo = cargar_mazo(mazo_global, '', [])

def cargar_mazo(mazo_global, texto_actual, texto_secciones):
    contenido_mazo_linea = mazo_global.readline()
    if contenido_mazo_linea != '':
        return separar_mazo_matriz(contenido_mazo_linea, 0, len(contenido_mazo_linea), texto_actual, texto_secciones)
    else:
        return texto_secciones
def separar_mazo_matriz(contenido, indice, largo, texto_actual, texto_secciones):
    '''Funcion que separar el mazo en contenido'''

    if indice == largo:
        return texto_secciones
    elif contenido[indice] == "/":
        return separar_mazo_matriz(contenido, indice + 1, largo, '', texto_secciones + [texto_actual])
    else:
        return separar_mazo_matriz(contenido, indice + 1, largo, texto_actual + contenido[indice], texto_secciones)
    
print(cargar_mazo(mazo_global, '', []))
