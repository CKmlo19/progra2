import random

mazo = [7,8,9,10]
mano1 = [1,2,3]
mano2 = [4,5,6, 7]

def sacrificar(mano1):
    '''Funcion que descarta una carta de tu mazo'''
    numero_aleatorio = random.randint(0, len(mano1)-1)
    return sacrificar_aux(mano1, numero_aleatorio, 0, len(mano1), [])

def sacrificar_aux(mano1, numero_aleatorio, indice, largo, mano_nueva):
    '''Auxiliar'''
    if indice == largo:
        return mano_nueva
    elif indice == numero_aleatorio:
        return sacrificar_aux(mano1, numero_aleatorio, indice + 1, largo, mano_nueva)
    else:
        return sacrificar_aux(mano1, numero_aleatorio, indice + 1, largo, mano_nueva + [mano1[indice]])
    
print(sacrificar(mano1))
