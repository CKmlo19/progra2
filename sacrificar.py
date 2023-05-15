import os 
import sys
import random
from pathlib import Path
sys.setrecursionlimit(10000000)

# esto abre el archivo que esta en la misma carpeta
with open("Mazo_no_lineas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

#Nota, de este archivo .txt, los unicornios van del 0 al 50, magia del 51 al 65, ventaja del 66 al 73, y desventaja del 74 al 81

mazo = [7,8,9,10]
mano1 = [1,2,3]
mano2 = [4,5,6, 7]

def descartar(mano_descartar):
    '''Funcion que descarta una carta del jugador de manera aleatoria'''
    numero_aleatorio = random.randint(0, len(mano_descartar) - 1)
    return descartar_aux(mano_descartar, numero_aleatorio, 0, len(mano_descartar), [])

def descartar_aux(mazo_descartar, numero_aleatorio, indice, largo, mazo_descartado):
    '''Funcion que trata de descartar aleatoriamente una carta del mazo del jugador rival'''
    if indice == largo:
        return mazo_descartado
    elif indice == numero_aleatorio:
        return descartar_aux(mazo_descartar, numero_aleatorio, indice + 1, largo, mazo_descartado)
    else:
        return descartar_aux(mazo_descartar, numero_aleatorio, indice + 1, largo, mazo_descartado + [mazo_descartar[indice]])

print(descartar(mano2))