import random
mazo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
mazo_sin_desventajas = mazo[:11]


def manos(mazo):
    '''Funcion que define las cartas de comienzo de cada jugador'''
    tamaño = 3
    mano1 = random.sample(mazo_sin_desventajas, tamaño)
    nueva_lista = eliminar_elemento(mazo_sin_desventajas, mano1[0])
    nueva_lista = eliminar_elemento(nueva_lista, mano1[1])
    nueva_lista = eliminar_elemento(nueva_lista, mano1[2])
    mano2 = random.sample(nueva_lista, tamaño)
    nueva_lista = eliminar_elemento(nueva_lista, mano2[0])
    nueva_lista = eliminar_elemento(nueva_lista, mano2[1])
    nueva_lista = eliminar_elemento(nueva_lista, mano2[2])
    return [mano1, mano2, nueva_lista]

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
    
res = manos(mazo_sin_desventajas)
print(res)