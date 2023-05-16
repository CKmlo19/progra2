import os 
import sys
import random
from pathlib import Path
sys.setrecursionlimit(10000000)

# esto abre el archivo que esta en la misma carpeta
with open("Mazo_no_lineas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

#Nota, de este archivo .txt, los unicornios van del 0 al 50, magia del 51 al 65, ventaja del 66 al 73, y desventaja del 74 al 81


def iniciar_juego():
    """Funcion que inicia el juego"""
    mazo = separar_mazo_lista(contenido, 0, len(contenido), '', [])
    mano = manos(mazo)
    mazo_nuevo = mano[2]
    mano1 = mano[0]
    mano2 = mano[1]
    return descartar(mano2)

def separar_mazo_lista(contenido, indice, largo, texto_actual, texto_secciones):
    '''Funcion que separar el mazo de acuerdo a un caracter separador previamente en el archivo'''
    if indice == largo:
        # return texto_secciones
        return remover_saltos_linea(texto_secciones, 0, len(texto_secciones), [])
    elif contenido[indice] == "/":
        return separar_mazo_lista(contenido, indice + 1, largo, '', texto_secciones + [texto_actual])
    else:
        return separar_mazo_lista(contenido, indice + 1, largo, texto_actual + contenido[indice], texto_secciones)
    
def remover_saltos_linea(lista_contenido, indice, largo, resultado):
    '''Funcion que trata de remover los \n que hay en la lista'''
    if indice == largo:
        return resultado
    elif lista_contenido[indice] == "\n":
        return remover_saltos_linea(lista_contenido, indice + 1, largo, resultado)
    elif lista_contenido[indice] == " \n":
        return remover_saltos_linea(lista_contenido, indice + 1, largo, resultado)
    elif lista_contenido[indice] == "  \n":
        return remover_saltos_linea(lista_contenido, indice + 1, largo, resultado)
    else:
        return remover_saltos_linea(lista_contenido, indice + 1, largo, resultado + [lista_contenido[indice]])

def eliminar_elemento(lista, elemento):
    ''' Elimina un elemento de una lista'''
    return eliminar_elemento_aux(lista, elemento, 0, len(lista), [])

def eliminar_elemento_aux(lista, elemento, indice, largo, resultado):
    ''' Funcion auxiliar 
    '''
    if largo <= indice:
        return resultado
    elif lista[indice] == elemento:
        return eliminar_elemento_aux(lista, elemento, indice + 1, largo, resultado)
    else:
        return eliminar_elemento_aux(lista, elemento, indice + 1, largo, resultado + [lista[indice]])

def manos(mazo):
    tamaño = 3
    mano1 = random.sample(mazo, tamaño)
    nueva_lista = eliminar_elemento(mazo, mano1[0])
    nueva_lista = eliminar_elemento(nueva_lista, mano1[1])
    nueva_lista = eliminar_elemento(nueva_lista, mano1[2])
    mano2 = random.sample(nueva_lista, tamaño)
    nueva_lista = eliminar_elemento(nueva_lista, mano2[0])
    nueva_lista = eliminar_elemento(nueva_lista, mano2[1])
    nueva_lista = eliminar_elemento(nueva_lista, mano2[2])
    return [mano1, mano2, nueva_lista]

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
    
print(iniciar_juego())
