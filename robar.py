# Funcion que roba una carta del mazo
import random


mazo = [7,8,9,10]
mano1 = [1,2,3]
mano2 = [4,5,6, 7]

def robar(mano1, mazo):
    '''Funcion que roba una carta del mazo'''
    numero_aleatorio = random.randint(0, len(mazo)-1)
    return robar_aux(mano1, mazo, numero_aleatorio, 0, len(mazo), [])

def robar_aux(mano1, mazo, numero_aleatorio, indice, largo, mazo_nuevo):
    '''Funcion auxiliar'''
    if indice == largo:
        return mano1, mazo_nuevo
    elif indice == numero_aleatorio:
        return robar_aux(mano1 + [mazo[numero_aleatorio]], mazo, numero_aleatorio, indice + 1, largo, mazo_nuevo)
    else:
        return robar_aux(mano1, mazo, numero_aleatorio, indice + 1, largo, mazo_nuevo + [mazo[indice]])
    
print(robar(mano1, mazo))