import os 
import sys
from pathlib import Path
sys.setrecursionlimit(10000000)

# esto abre el archivo que esta en la misma carpeta
with open("Mazo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().rstrip("\n")

# mazo_global = open("/home/camilo/Downloads/Mazo.txt", encoding="utf-8")

def iniciar_juego():
    """Funcion que inicia el juego"""
    mazo = separar_mazo_matriz(contenido, 0, len(contenido), '', [])
    return mazo

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
    else:
        return remover_saltos_linea(lista_contenido, indice + 1, largo, resultado + [[lista_contenido[indice]]])
    
# def separar_lista_columnas(contenido, indice, largo, resultado):
#     '''Funcion que separar los elementos de la lista en elementos en si'''
#     if indice == largo:
#         return resultado
#     elif co

print(iniciar_juego())
