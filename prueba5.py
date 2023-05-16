import os 
import sys
import random
from pathlib import Path
sys.setrecursionlimit(10000000)

# esto abre el archivo que esta en la misma carpeta
with open("Mazo_no_lineas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().rstrip("\n")


def iniciar_juego():
    """Funcion que inicia el juego"""
    mano = manos(mazo)
    return mano

def separar_mazo_matriz_aux(texto):
    '''Funcion auxiliar'''
    if type(texto) != str:
        return "Error02"
    else:
        return separar_mazo_matriz(contenido, 0, len(contenido), '', [])

def separar_mazo_matriz(contenido, indice, largo, texto_actual, texto_secciones):
    '''Funcion que separar el mazo de acuerdo a un caracter separador previamente en el archivo'''
    if indice == largo:
        # return texto_secciones
        return remover_saltos_linea(texto_secciones, 0, len(texto_secciones), [])
    elif contenido[indice] == "/":
        return separar_mazo_matriz(contenido, indice + 1, largo, '', texto_secciones + [texto_actual])
    else:
        return separar_mazo_matriz(contenido, indice + 1, largo, texto_actual + contenido[indice], texto_secciones)
    
def remover_saltos_linea(lista_contenido, indice, largo, resultado):
    '''Funcion que trata de remover los \n que hay en la lista'''
    if indice == largo:
        return resultado
    elif lista_contenido[indice] == "\n":
        return remover_saltos_linea(lista_contenido, indice + 1, largo, resultado)
    elif lista_contenido[indice] == " \n":
        return remover_saltos_linea(lista_contenido, indice + 1, largo, resultado)
    else:
        return remover_saltos_linea(lista_contenido, indice + 1, largo, resultado + [lista_contenido[indice]])

mazo = separar_mazo_matriz_aux(contenido)

def eliminar_elemento(lista, elemento):
    ''' Elimina un elemento de una lista
    '''
    if type(lista) != list:
        return 'Error01'
    else:
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
    '''Funcion que define las cartas de comienzo de cada jugador'''
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


def comprobar_tipo(lista, elemento):
    '''Funcion que comprueba el tipo de una carta'''
    if type(lista) != list:
        return "Error01"
    else:
        return comprobar_tipo_aux(lista, elemento, 0)
    

#Nota, de este archivo .txt, los unicornios van del 0 al 50, magia del 51 al 65, ventaja del 66 al 73, y desventaja del 74 al 81


def comprobar_tipo_aux(lista, elemento, indice):
    if indice < 50:
        if lista[indice] == elemento:
            return "Unicornio"
    elif indice < 65:
        if lista[indice] == elemento:
            return "Magia"
    elif indice < 73:
        if lista[indice] == elemento:
            return "Ventaja"
    elif indice < 82:
        if lista[indice] == elemento:
            return "Desventaja"
    
    if indice < 81:
        return comprobar_tipo_aux(lista, elemento, indice + 1)
    

    
    
res = comprobar_tipo(mazo, mazo[81])
print(res)
