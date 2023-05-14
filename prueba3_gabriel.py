import sys
sys.setrecursionlimit(10000000)

with open("Mazo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

def funcion_separar(texto, separador):
    if type(texto) != str:
        return "Error01"
    else:
        return funcion_separar_aux(texto, separador, 0, len(texto), [], "")
    
def funcion_separar_aux(texto, separador, indice, largo, resultado, carta):
    if indice == largo:
        return resultado
    elif texto[indice] == separador:
        return funcion_separar_aux(texto, separador, indice + 1, largo, resultado + [carta], "")
    else:
        return funcion_separar_aux(texto, separador, indice + 1, largo, resultado, carta + texto[indice])

res = funcion_separar(contenido, "/")
print(res)

