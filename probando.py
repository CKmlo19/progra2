import sys
import random
sys.setrecursionlimit(10000000)

azul = "\033[94m"
rojo_negrita = "\033[1;91m"
azul_negrita = "\033[94;1m"
verde_negrita = "\033[92;1m"
morado_negrita = "\033[35;1m"
blanco_negrita =  "\033[97;1m"
azul_subrayado = "\033[94;4m"
verde_subrayado = "\033[4;92m"
amarillo_subrayado = "\033[33;4m"
resetear = "\033[0m"


# esto abre el archivo que esta en la misma carpeta
with open("Mazo_sin_lineas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().rstrip("\n")


def iniciar_juego():
    """Funcion que inicia el juego"""
    resultado_manos = manos(mazo)
    mano1 = resultado_manos[0]
    mano2 = resultado_manos[1]
    nuevo_mazo = resultado_manos[2]
    print('Bienvenido al juego de unicornios inestables!')
    ver_instrucciones = input("\nPresiona la tecla " + azul_negrita +  "1" + resetear + " para ver las instrucciones completas. \nPresiona " + azul_negrita + "cualquier otra tecla" + resetear + " para jugar: ")
    if ver_instrucciones == "1":
        print("Las instrucciones son estas: ")
        print("\nEste juego se ejecuta mediante lineas de comandos, las acciones se ejecutaran mediante palabras claves que deben ser escritas exactamente: ")
        print("\n1. Cuando sea tu turno, digita " + morado_negrita + "mazo" + resetear + " para mostrar el mazo actual")
        print("2. Si quieres ver la mano y establo del rival, digita " + morado_negrita +  "rival" + resetear + " para ver su mano actual")
        # print("3. Para ver tu establo, digita " + morado_negrita + "establo1" + resetear +  " para ver el establo de tu rival, digita" + morado_negrita + " establo2" + resetear)
        input("\nDigita cualquier tecla para continuar: ")
        return turnos(mano1, mano2, nuevo_mazo)
    else:
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
    '''Funcion que comprueba el tipo de carta'''
    if indice < 51:
        if lista[indice] == elemento:
            return "Unicornio"
    elif indice < 66:
        if lista[indice] == elemento:
            return "Magia"
    elif indice < 74:
        if lista[indice] == elemento:
            return "Ventaja"
    elif indice < 82:
        if lista[indice] == elemento:
            return "Desventaja"
    
    if indice < 81:
        return comprobar_tipo_aux(lista, elemento, indice + 1)

def descartar(mano_descartar):
    '''Funcion que descarta una carta del jugador de manera aleatoria'''
    if mano_descartar == []:
        return []
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
        print(azul_subrayado + "\nEste es el mazo del jugador1:" + resetear + " ", jugador1)
        print(amarillo_subrayado + "\nEste es el mazo del jugador2:" + resetear + " ", jugador2)
        return turnos_aux(jugador1, jugador2, mazo_general, 0, [], [])

def turnos_aux(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2):
    '''Funcion que controla los turnos con una bandera'''
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
        print("\n====> Es el turno del " + azul_subrayado + "jugador 1" + resetear + " estas son tus cartas:")
        print(f"\n{mazo_jugador1}")
        print("\nEste es tu establo actual: ")
        print(f"\n{establo1}")
        return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    else:
        sacar_carta = robar(mazo_jugador2, mazo_general)
        mazo_jugador2 = sacar_carta[0]
        mazo_general = sacar_carta[1]
        print("\n====> Es el turno del " + amarillo_subrayado + "jugador 2" + resetear + " estas son tus cartas:")
        print(f"\n{mazo_jugador2}")
        print("\nEste es tu establo actual: ")
        print(f"\n{establo2}")
        return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
        

def verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2):
    '''Funcion que sirve para rellamar en caso de que el jugador selecciona un indice invalido'''
    carta = input("\nPresiona el numero de cual quieres utilizar (primera, segunda, tercera...): " )
    if carta == "mazo":
        print("Este es el mazo: ")
        print(f"\n{mazo_general}")
        print("\nEstas son tus cartas: ")
        print(f"\n{mazo_jugador1}")
        print("\nEste es tu establo actual: ")
        print(f"\n{establo1}")
        return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif carta == "rival":
        print(blanco_negrita + "\nEsta es la mano y establo del rival: " + resetear)
        print(azul_negrita + "\nMazo del rival: " + resetear, mazo_jugador2)
        print(azul_negrita + "\nEstablo del rival: " + resetear, establo2)
        return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif len(carta) != 1:
        print(rojo_negrita + "Error, por favor selecciona solamente numeros [1,2,3,...]" + resetear)
        return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif 49 <= ord(carta) <= 54:
        carta = int(carta)
        carta -= 1
        if 0 <= carta <= len(mazo_jugador1) - 1:
            return acciones_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
        else:
            print("\nCarta invalida!")
            print(rojo_negrita + "Por favor selecciona selecciona un numero que esta entre las cartas" + resetear)
            return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    else:
        print(rojo_negrita + "Error, por favor selecciona solamente numeros [1,2,3,...]" + resetear)
        return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
        
def acciones_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta):
    '''Funcion que crea el juego del jugador1'''
    print("Jugaste esta carta: " + verde_negrita + mazo_jugador1[carta] + resetear)
    if comprobar_tipo(mazo, mazo_jugador1[carta]) == "Unicornio":
        print("\nHaz pasado un unicornio al establo!")
        print(verde_subrayado + "Tu establo se actualizo:" + resetear + " ", establo1 + [mazo_jugador1[carta]])
        return turnos_aux(eliminar_elemento(mazo_jugador1, mazo_jugador1[carta]), mazo_jugador2, mazo_general, turno + 1, establo1 + [mazo_jugador1[carta]], establo2)
    elif comprobar_tipo(mazo, mazo_jugador1[carta]) == "Ventaja":
        print("\nHaz hecho que el rival descarte un carta!")
        descartar_input = input("Digite mano para hacer que el rival descarte una carta de su mano o establo para hacer que el rival descarte una carta de su establo: ")
        if descartar_input == "establo":
            print("El rival ha descartado una carta de su establo!: ")
            print("El establo rival se actualizo: ")
            print(descartar(establo2))
            return turnos_aux(mazo_jugador1, mazo_jugador2, mazo_general, turno + 1, establo1, descartar(establo2))
        elif descartar_input == "mano":
            print("El rival ha descartado una carta de su mano!")
            print("La mano del rival se actualizo: ")
            print(descartar(mazo_jugador2))
            return turnos_aux(mazo_jugador1, descartar(mazo_jugador2), mazo_general, turno + 1, establo1, establo2)
        else:
            print("Digite exactamente si quieres descartar la mano o el mazo del rival")
            return acciones_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
    elif comprobar_tipo(mazo, mazo_jugador1[carta]) == "Desventaja":
        print("Haz elegido una desventaja, por lo que haz sacrificado una carta!")
        return turnos_aux(sacrificar(mazo_jugador1), mazo_jugador2, mazo_general, turno + 1, establo1, establo2)
    elif comprobar_tipo(mazo, mazo_jugador1[carta]) == "Magia":
        print("Haz elegido una carta de magia, por lo que robas una carta adicional del mazo")
        roba = robar(mazo_jugador1, mazo_general)
        return turnos_aux(eliminar_elemento(roba[0], mazo_jugador1[carta]), mazo_jugador2, roba[1], turno + 1, establo1, establo2)
    
def verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2):
    '''Funcion que sirve para rellamar en caso de que el jugador selecciona un indice invalido'''
    carta = input("\nPresiona el numero de cual quieres utilizar (primera, segunda, tercera...): " )
    if carta == "mazo":
        print("Este es el mazo: ")
        print(f"\n{mazo_general}")
        print("\nEstas son tus cartas: ")
        print(f"\n{mazo_jugador2}")
        print("\nEste es tu establo actual: ")
        print(f"\n{establo2}")
        return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif carta == "rival":
        print(blanco_negrita + "\nEsta es la mano y establo del rival: " + resetear)
        print(azul_negrita + "\nMazo del rival: " + resetear, mazo_jugador1)
        print(azul_negrita + "\nEstablo del rival: " + resetear, establo1)
        return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif len(carta) != 1:
        print(rojo_negrita + "Error, por favor selecciona solamente numeros [1,2,3,...]" + resetear)
        return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif 49 <= ord(carta) <= 54:
        carta = int(carta)
        carta -= 1
        if 0 <= carta <= len(mazo_jugador2) - 1:
            return acciones_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
        else:
            print("\nCarta invalida!")
            print(rojo_negrita + "Por favor selecciona selecciona un numero que esta entre las cartas" + resetear)
            return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    else:
        print(rojo_negrita + "Error, por favor selecciona solamente numeros [1,2,3,...]" + resetear)
        return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)


def acciones_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta):
    '''Funcion que crea el juego del jugador2'''
    print("Jugaste esta carta: " + verde_negrita + mazo_jugador2[carta] + resetear)
    if comprobar_tipo(mazo, mazo_jugador2[carta]) == "Unicornio":
        print("Haz pasado un unicornio al establo")
        print(verde_subrayado + "Tu establo se actualizo:" + resetear + " ", establo2 + [mazo_jugador2[carta]])
        return turnos_aux(mazo_jugador1, eliminar_elemento(mazo_jugador2, mazo_jugador2[carta]), mazo_general, turno - 1, establo1, establo2 + [mazo_jugador2[carta]])
    elif comprobar_tipo(mazo, mazo_jugador2[carta]) == "Ventaja":
        print("\nHaz hecho que el rival descarte un carta!")
        print("Por lo que el mazo del rival seria el siguiente: \n")
        print(descartar(mazo_jugador1))
        return turnos_aux(descartar(mazo_jugador1), mazo_jugador2, mazo_general, turno - 1, establo1, establo2)
    elif comprobar_tipo(mazo, mazo_jugador2[carta]) == "Desventaja":
        print("Haz sacrificado una carta!")
        return turnos_aux(mazo_jugador1, sacrificar(mazo_jugador2), mazo_general, turno - 1, establo1, establo2)
    elif comprobar_tipo(mazo, mazo_jugador2[carta]) == "Magia":
        print("Por lo que robas una carta adicional del mazo")
        roba = robar(mazo_jugador2, mazo_general)
        return turnos_aux(mazo_jugador1, eliminar_elemento(roba[0], mazo_jugador2[carta]), roba[1], turno - 1, establo1, establo2)

                              
        
res = iniciar_juego()
print(res)
