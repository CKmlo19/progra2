import random

mazo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def otra_prueba(mazo):
    '''Funcion que descarta una carta de tu mazo'''
    mano = random.sample(mazo[:9], 3)
    numero_aleatorio = random.randint(0, len(mazo))
    return mano_prueba(mano, mazo, numero_aleatorio, 0, 0, len(mano), len(mazo[:9]), [])

def mano_prueba(mano, mazo, numero_aleatorio, ind_mano, ind_mazo, largo_mano, largo_mazo, mazo_nuevo):
    '''Auxiliar'''
    if ind_mano == largo_mano:
        return [mano, mazo_nuevo + mazo[ind_mano:]]
    elif ind_mazo == largo_mazo:
        return mano_prueba(mano, mazo, numero_aleatorio, ind_mano, 0, largo_mano, largo_mazo, mazo_nuevo)
    elif mano[ind_mano] == mazo[ind_mazo]:
        return mano_prueba(mano, mazo, numero_aleatorio, ind_mano + 1, ind_mazo + 1, largo_mano, largo_mazo, mazo_nuevo)
    else:
        return mano_prueba(mano, mazo, numero_aleatorio, ind_mano, ind_mazo + 1, largo_mano, largo_mazo, mazo_nuevo + [mazo[ind_mazo]])
    
res = otra_prueba(mazo)
print(res)