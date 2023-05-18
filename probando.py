import os 
import sys
import random
sys.setrecursionlimit(10000000)

azul = "\033[94m"
rojo_negrita = "\033[1;91m"
resetear = "\033[0m"


# esto abre el archivo que esta en la misma carpeta
with open("Mazo_sin_lineas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().rstrip("\n")


def iniciar_juego():
    """Funcion que inicia el juego"""
    mano1 = manos(mazo)[0]
    mano2 = manos(mazo)[1]
    nuevo_mazo = manos(mazo)[2]
    input('''Bienvenido al juego de unicornios inestables!
             Presiona una tecla para empezar: ''')
    return turnos(mano1, mano2, nuevo_mazo)

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
    elif lista_contenido[indice] == "  \n":
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
        return "Error02"
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

def sacrificar(mano):
    '''Funcion que descarta una carta de tu mazo'''
    numero_aleatorio = random.randint(0, len(mano)-1)
    return sacrificar_aux(mano, numero_aleatorio, 0, len(mano), [])

def sacrificar_aux(mano, numero_aleatorio, indice, largo, mano_nueva):
    '''Auxiliar'''
    if indice == largo:
        return mano_nueva
    elif indice == numero_aleatorio:
        return sacrificar_aux(mano, numero_aleatorio, indice + 1, largo, mano_nueva)
    else:
        return sacrificar_aux(mano, numero_aleatorio, indice + 1, largo, mano_nueva + [mano[indice]])

def robar(mano, mazo_gen):
    '''Funcion que roba una carta del mazo'''
    numero_aleatorio = random.randint(0, len(mazo_gen)-1)
    return robar_aux(mano, mazo_gen, numero_aleatorio, 0, len(mazo_gen), [])

def robar_aux(mano, mazo_gen, numero_aleatorio, indice, largo, mazo_nuevo):
    '''Funcion auxiliar'''
    if indice == largo:
        return [mano, mazo_nuevo]
    elif indice == numero_aleatorio:
        return robar_aux(mano + [mazo_gen[numero_aleatorio]], mazo_gen, numero_aleatorio, indice + 1, largo, mazo_nuevo)
    else:
        return robar_aux(mano, mazo_gen, numero_aleatorio, indice + 1, largo, mazo_nuevo + [mazo_gen[indice]])

def turnos(jugador1, jugador2, mazo_general):
    '''Funcion para determinar los turnos de cada jugador '''
    if type(jugador1) != list or type(jugador2) != list or type(mazo_general) != list:
        return "Error03"
    else:
        return turnos_aux(jugador1, jugador2, mazo_general, 0, [], [])

def turnos_aux(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2):
    print(establo1, establo2)
    if len(mazo_general) == 0:
        return "El mazo se ha quedado sin cartas! La partida queda en empate"
    elif len(establo1) == 5:
        return "El jugador 1 ha ganado, felicidades!"
    elif len(establo2) == 5:
        return "El jugador 2 ha ganado, felicidades!"
    elif turno == 0:
        sacar_carta = robar(mazo_jugador1, mazo_general)
        mazo_jugador1 = sacar_carta[0]
        mazo_general = sacar_carta[1]
        carta = input(f"Es el turno del jugador 1, estas son tus cartas: \n{mazo_jugador1}, presiona el numero de cual quieres utilizar (primera, segunda, tercera...): " ) #ligero salto de linea para que se vean mejor las cartas
        carta = int(carta)
        carta -= 1
        print(carta)
        return jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
    else:
        sacar_carta = robar(mazo_jugador2, mazo_general)
        mazo_jugador2 = sacar_carta[0]
        mazo_general = sacar_carta[1]
        carta = input(f"Es el turno del jugador 2, estas son tus cartas: \n{mazo_jugador2}, presiona el numero de cual quieres utilizar (primera, segunda, tercera...): " ) #ligero salto de linea para que se vean mejor las cartas
        carta = int(carta)
        carta -= 1
        print(carta)
        return jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
    
def jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta):
    '''Funcion que sirve para rellamar en caso de que el jugador selecciona un indice invalido'''
    if 0 <= carta <= len(mazo_jugador1) - 1:
            return jugador1_aux(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
    else:
        print("Carta invalida!")
        carta = input(rojo_negrita + "Por favor selecciona un numero valido: " + resetear)
        carta = int(carta)
        carta -= 1
        return jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
        
def jugador1_aux(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta):
    '''Funcion que crea el juego del jugador1'''
    if comprobar_tipo(mazo, mazo_jugador1[carta]) == "Unicornio":
        print("Haz pasado un unicornio al establo")
        return turnos_aux(eliminar_elemento(mazo_jugador1, mazo_jugador1[carta]), mazo_jugador2, mazo_general, turno + 1, establo1 + [mazo_jugador1[carta]], establo2)
    elif comprobar_tipo(mazo, mazo_jugador1[carta]) == "Ventaja":
        print("Haz hecho que el rival descarte un carta!")
        return turnos_aux(mazo_jugador1, descartar(mazo_jugador2), mazo_general, turno + 1, establo1, establo2)
    elif comprobar_tipo(mazo, mazo_jugador1[carta]) == "Desventaja":
        print("Haz elegido una desventaja, por lo que haz sacrificado una carta!")
        return turnos_aux(sacrificar(mazo_jugador1), mazo_jugador2, mazo_general, turno + 1, establo1, establo2)
    elif comprobar_tipo(mazo, mazo_jugador1[carta]) == "Magia":
        print("Haz elegido una carta de magia, por lo que robas una carta adicional del mazo")
        roba = robar(mazo_jugador1, mazo_general)
        return turnos_aux(eliminar_elemento(roba[0], mazo_jugador1[carta]), mazo_jugador2, roba[1], turno + 1, establo1, establo2)
    
def jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta):
    '''Funcion que sirve para rellamar en caso de que el jugador selecciona un indice invalido'''
    if 0 <= carta <= len(mazo_jugador2) - 1:
            return jugador2_aux(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
    else:
        print("Carta invalida!")
        carta = input(rojo_negrita + "Por favor selecciona un numero valido: " + resetear)
        carta = int(carta)
        carta -= 1
        return jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)


def jugador2_aux(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta):
    '''Funcion que crea el juego del jugador2'''
    if comprobar_tipo(mazo, mazo_jugador2[carta]) == "Unicornio":
        print("Haz pasado un unicornio al establo")
        return turnos_aux(mazo_jugador1, eliminar_elemento(mazo_jugador2, mazo_jugador2[carta]), mazo_general, turno - 1, establo1, establo2 + [mazo_jugador2[carta]])
    elif comprobar_tipo(mazo, mazo_jugador2[carta]) == "Ventaja":
        print("Haz hecho que el rival descarte un carta!")
        return turnos_aux(descartar(mazo_jugador1), mazo_jugador2, mazo_general, turno - 1, establo1, establo2)
    elif comprobar_tipo(mazo, mazo_jugador2[carta]) == "Desventaja":
        print("Haz elegido una desventaja, por lo que haz sacrificado una carta!")
        return turnos_aux(mazo_jugador1, sacrificar(mazo_jugador2), mazo_general, turno - 1, establo1, establo2)
    elif comprobar_tipo(mazo, mazo_jugador2[carta]) == "Magia":
        print("Haz elegido una carta de magia, por lo que robas una carta adicional del mazo")
        roba = robar(mazo_jugador2, mazo_general)
        return turnos_aux(mazo_jugador1, eliminar_elemento(roba[0], mazo_jugador2[carta]), roba[1], turno - 1, establo1, establo2)

                              
        
res = iniciar_juego()
print(res)
