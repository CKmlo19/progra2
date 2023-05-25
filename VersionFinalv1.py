import sys
import random
sys.setrecursionlimit(10000000)

azul = "\033[94m"
rojo_negrita = "\033[1;91m"
azul_negrita = "\033[94;1m"
verde_negrita = "\033[92;1m"
morado_negrita = "\033[35;1m"
blanco_negrita =  "\033[97;1m"
cian_negrita = "\033[1;36m"
amarillo_negrita = "\033[1;33m"
azul_subrayado = "\033[94;4m"
verde_subrayado = "\033[4;92m"
amarillo_subrayado = "\033[33;4m"
rojo_subrayado = "\033[4;31m"
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
    print(r"""
    
                                ______ _                           _     _               _     _                        _ 
                                | ___ (_)                         (_)   | |             | |   (_)                      | |
                                | |_/ /_  ___ _ ____   _____ _ __  _  __| | ___     __ _| |    _ _   _  ___  __ _  ___ | |
                                | ___ | |/ _ | '_ \ \ / / _ | '_ \| |/ _` |/ _ \   / _` | |   | | | | |/ _ \/ _` |/ _ \| |
                                | |_/ | |  __| | | \ V |  __| | | | | (_| | (_) | | (_| | |   | | |_| |  __| (_| | (_) |_|
                                \____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|_|   | |\__,_|\___|\__, |\___/(_)
                                                                                            _/ |            __/ |        
                                                                                            |__/            |___/                                                         
    """)
    print(r"""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓  ▓▓▓▓ ▓▓▓▓  ▓▓▓   ▓▓   ▓▓▓   ▓▓▓   ▓▓▓   ▓▓   ▓▓▓   ▓▓▓  ▓▓▓  ▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓  ▓▓▓  ▓▓▓   ▓▓▓   ▓▓   ▓▓    ▓▓   ▓▓    ▓▓   ▓▓    ▓    ▓▓    ▓     ▓     ▓     ▓   ░▓    ▓▓    ▓▓   ▓▓    ▓    ▓▓   ▓▓▓   ▓▓   ▓▓▓  ▓▓▓▓  ▓▓▓  ▓▓▓▓  ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓
▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓░ ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ░   ▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓
▓▓▓▒▓▓▓▓▓▓▓░ ░▓▓▓  ▓▓▓░ ░▓▓▓   ▓▓     ░ ▓ ░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░  ░░ ▓▓▓▒▒░▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓  ▓▓▓▒▒▓ ▒▓▓▓▒▒ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓▓▓▓▓▓▓▓▓░░░▓▓   ▓▓▓   ░▓▓   ▓      ░░ ▓  ░▒▒ ▓▓▓▓▓ ▒▒▒▒▓▓▓▓░ ░ ░░░ ▓▓▒▒░▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒ ▓▓▓▓▓▒▓░    ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓░░░▓▓   ▓▓▓░    ▓   ▓    ▓▓░░░▓▓▓░▒▒▓▓▓▓▓▓▒▒▒▒▒ ▓▓▓░░░▓▓░░░▓▓░▒░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓░▓▓▓▓▓▓▓░░░▓▓   ▓▓▓░        ▓▓     ▓▓▓▓▓▓░▒▒▓▓▓▓▓▒▒▒▒▒▒░▓▓▓░░░ ░░░ ▓▓▒▒░▓▓▓▓▓▓▒▒▓ ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒░   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓▒▓▓▓▓▓▓▓░ ░▓▓  ░▓▓▓   ░     ▓▓▓▓   ░ ▓▓▓▓░▒▒▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓░░░ ░░▒▓▓▓▒▒░▓▓▓▓▓▓▒▒▓▒▒▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓   ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓▓▓▓▓▓▓▓▓░ ░▓▓   ▓▓▓   ▓░    ▓   ▓▓ ░░░▓▓▓░░▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓░░░▓▓░░ ▓▓▒▒░▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▓▓▓▓▓▓▓░ ░▓▓   ▓▓▓░  ▓▓    ▓    ▓▓░░░▓▓▓░░▒▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓░░░▓▓░░ ▓▓▒▒░▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓ ░ ▓▓▓▓▓▓▓░      ▓▓▓   ▓▓    ▓▓     ░░▓▓▓▓░░▒▓▓▓▒▒▒▒▒▒▒▒▒ ▓▓░ ░░░░░▓▓▓▒░▒▒▒▒▓▓▓▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓  ▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▒▒▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ▓▓ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░░ ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░▒▒▒ ▓▓▓▓▓▓▓▓▓░ ▓
▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░▒▓▓░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░  ▒▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
▓▓ ░ ▓▓▓▓▓▓░░░▓▓   ▓▓▓    ▓▓   ▓▓   ▓▓▓░░░░▒░░▓▓▓ ▒▒▒▒▒▒ ▓▓▒░░ ░░░░▓▓▓▒▒▒▓▓▓▒▒▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓ ▒▒   ▓▓▓▓▒▒ ▓▓▓▓▓▓  ▓ ▓▓▓  ▒▓▓▓▓ ▓▓░▓▓▓▓▓▓▓▒░ ░▒▒▒▒▒▓▓▓▓▓▓▓▓▓░ ▓
▓▓▓ ▓▓▓▓▓▓▓░ ░▓▓   ▓▓▓   ░▓▓   ▓▓   ▓▓ ░░ ▓ ░▒ ▓▓▒▒▒▓▓▒▒▒▓▓▒░░▓▓ ░░ ▓▓▒▒▒▒▓▓▒▒▓▓▒▒▓▓▓▓▒▒▒▓▓▓▓░▓░  ▓▓▓▓  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒░▒▒▒  ░▒       ░░░░░▒▒▒▒▒▒▓▒▓▓▓▓▓▓▓  ▓
▓▓▓▒▓▓▓▓▓▓▓░░░▓▓  ░▓▓▓     ▓   ▓▓   ▓▓░░░▓▓▓▒▒░▓▓▒▒ ▓▓▒▒▒▓▓▒░░▓▓▓░░ ▓▓▒▒▒▒▒▓▒▒▓▓ ▓▒▒▓▓▓▓▒▓▓▓▓ ░  ▓▓▓  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▓▓▓▓░░     ░░   ░   ░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓  ▓
▓▓ ░ ▓▓▓▓▓▓░░░▓▓  ░▓▓▓         ▓▓   ▓▓░░░▓▓▓▓▓▓▓▓▒▒ ▓▓▒▒▒▓▓░░ ░░░░░▓▓▓▒▒▒▒▒ ▒▒▓▓▓ ▒▒▓▒▓▓▓▓▓▓▓▓ ▒▓▓▓░ ▒▒▒▒▒▒▒  ▒▒▒░▒▒▒▒▓▓░░▒   ░          ░ ░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓▒▓▓▓▓▓▓▓░░░▓▓   ▓▓▓         ▓▓   ▓▓░░░▓▓▓▓▓▓▓▓▒▒ ▓▓▒▒▒▓▓░░░░░░░░▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒▒ ▓     ░▒▒▒▒▒▒▒▒▒▒            ░░   ▒▒▒▒▒ ▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓▓▓▓▓▓▓▓▓░ ░▓▓   ▓▓▓   ▓     ▓▓   ▓▓░░░▓▓▓▒▒░▓▓▒▒ ▓▓▒▒▒▓▓░░░▓▓ ░░ ▓▓▒▒▒▓▓▒▒▒▓▓░▒▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓ ░▒▒▒▒▒ ▓▓▓▓▓░   ▒▒▒▒▒▒▒▒▒     ░       ░   ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▓▓▓▓▓▓▓░ ░ ▓░ ░▓▓▓   ▓▓░   ▓▓   ▓▓ ░░░ ░▒▒ ▓▓▒▒▒▓ ▒▒▒▓▓░░░▓▓ ░░▓▓▓▒▒▒▓▓▒▒▒▓▓▓▒▒▒▓ ▓▒▒▓▓▓▓▓▓▓▓  ▒▒▒▒▒▓  ▓▓▓░  ▒▒▒░       ░            ░░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓░▓▓▓▓▓▓▓▓░    ░ ▓▓▓   ▓▓▓   ▓▓  ░▓▓▓ ▒▒░░▒ ▓▓▓▓▒▒▒▒▒▒▓▓▓▒░░▓▓ ░░ ▓▓▒▒▒▓▓▓▒▒▓▓▓ ▓▒▒▒▓░▓▓▓▓▓▓▓▓  ░▒▒▒▒▒    ▓   ░▒▒▒▒▒▒▒▒▓ ░░               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▒▒▒▒▒  ░▓▓░   ▒▒▒▒▒▒▒▒▒   ░░       ░░░ ▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░▒▒▒▒▒▒ ▓▓   ░ ▒▒▒▒▒▒▒▒    ░              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓     ▓       ▓▓░░░░░▒▓▓▓▓▓ ▒▒▒▒▒▒▓▓    ░▓▓▓▒░░▓▒ ░▓▓░░░░░ ▓▓▓▓▓▓▓▓▓▓▓▓    ▒▒▒▒▒▒▒▒▒▒▒▒░    ░░░▒░    ░              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓
▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓  ░▓▓▓▓▓      ▓   ▓     ░░ ▓ ░░ ▓▓▓▒▒░▓▓▓▓▓▓  ░   ▓ ░░░░ ░░▒ ░░ ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                ░░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ ░▓▓▓▓▓      ░       ▓▓░░  ░░░ ▓▓▓▓▒ ▓▒▒▒▓░   ░  ▓▒ ▓▒░▒▓░░▓░░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▒▒▒▒▒▒▒▒▒▒▒▒      ░░▒░   ░            ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░   ░▓░ ▓▓  ░▓   ▓    ░░░░░▒▓▓▓▓▓▓ ▒▒▒▒▒▓░  ▓▓░░ ░░▓▓▓▓▓▒░▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒    ░░   ░░░  ▓ ░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓  ░░░       ░░    ░░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓░ ▓▓▓░░▓▓▓ ░ ▓▓▓░░▓▓▓ ░▒▓▓ ░░ ▓▓░░░▓▓ ░░ ▓▓░░░▓▓░░░░▓ ░░░▓▓░░░░▓░░░░▓▓░░░░ ▓ ░░░ ▓░░░░▓ ░░░ ▓░░░ ▓▓░░░▓▓░░░ ▓▓░░░▓▓ ░░▓▓▓░░ ▓▓ ░░▓▓▓▒░▓▓▓▓░ ▓▓▓░░▓▓▓▓  ▓
▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓  ▓▓▓  ▓▓▓▓ ░ ▓▓▓ ░ ▓▓▓  ▓▓▓▓ ▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

""")
    ver_instrucciones = input("\nPresiona la tecla " + azul_negrita +  "1" + resetear + " para ver las instrucciones completas. \nPresiona " + azul_negrita + "cualquier otra tecla" + resetear + " para jugar: ")
    if ver_instrucciones == "1":
        print("Las instrucciones son estas: ")
        print("\nEste juego se ejecuta mediante lineas de comandos, ciertas acciones se ejecutaran mediante palabras claves que deben ser escritas exactamente: ")
        print("\n1. Cuando sea tu turno, digita " + morado_negrita + "mazo" + resetear + " para mostrar el mazo actual")
        print("2. Si quieres ver la mano y establo del rival, digita " + morado_negrita +  "rival" + resetear + " para ver su mano actual")
        print("3. Para seleccionar una carta digita el numero de la posicion de dicha carta en tu mano")
        print("4. Las cartas de unicornios al seleccionarse pasaran al establo")
        print("5. Las cartas de ventaja haran que se descarte una carta aleatoriamente de tu rival, puedes seleccionar si sera una carta de la mano o del establo")
        print("6. Las cartas de magia robaran una carta aleatoriamente, puedes seleccionar si sera del mazo restante o del establo de tu rival, la carta pasara a tu mano")
        print("7. Las cartas de desventaja solo saldran al comer una carta del mazo, su efecto aplicara automaticamente, se te descartara una carta de tu mano y se te acabara el turno")
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
    mazo_sin_desventajas = mazo[:74]
    mazo_solo_desventajas = mazo[74:]
    mano1 = random.sample(mazo_sin_desventajas, tamaño)
    nueva_lista = eliminar_elemento(mazo_sin_desventajas, mano1[0])
    nueva_lista = eliminar_elemento(nueva_lista, mano1[1])
    nueva_lista = eliminar_elemento(nueva_lista, mano1[2])
    mano2 = random.sample(nueva_lista, tamaño)
    nueva_lista = eliminar_elemento(nueva_lista, mano2[0])
    nueva_lista = eliminar_elemento(nueva_lista, mano2[1])
    nueva_lista = eliminar_elemento(nueva_lista, mano2[2])
    return [mano1, mano2, nueva_lista + mazo_solo_desventajas]


def comprobar_tipo(lista, elemento):
    '''Funcion que comprueba el tipo de una carta'''
    if type(lista) != list:
        return "Error02"
    else:
        return comprobar_tipo_aux(lista, elemento, 0)
    
#Nota, de este archivo .txt, los unicornios van del 0 al 50, magia del 51 al 65, ventaja del 66 al 73, y desventaja del 74 al 81

def comprobar_tipo_aux(lista, elemento, indice):
    '''Funcion que comprueba el tipo de carta basado en sus indices en el mazo'''
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

def descartar_aux(mano_descartar, numero_aleatorio, indice, largo, mazo_descartado):
    '''Funcion auxiliar de descartar'''
    if mano_descartar == []:
        return []
    elif indice == largo:
        return mazo_descartado
    elif indice == numero_aleatorio:
        return descartar_aux(mano_descartar, numero_aleatorio, indice + 1, largo, mazo_descartado)
    else:
        return descartar_aux(mano_descartar, numero_aleatorio, indice + 1, largo, mazo_descartado + [mano_descartar[indice]])

def sacrificar(mano):
    '''Funcion que sacrifica una carta de tu propia mano'''
    numero_aleatorio = random.randint(0, len(mano)-1)
    return sacrificar_aux(mano, numero_aleatorio, 0, len(mano), [])

def sacrificar_aux(mano, numero_aleatorio, indice, largo, mano_nueva):
    '''Funcion auxiliar de sacrificar'''
    if indice == largo:
        return mano_nueva
    elif indice == numero_aleatorio:
        return sacrificar_aux(mano, numero_aleatorio, indice + 1, largo, mano_nueva)
    else:
        return sacrificar_aux(mano, numero_aleatorio, indice + 1, largo, mano_nueva + [mano[indice]])

def robar(mano, mazo_gen):
    '''Funcion que roba una carta'''
    numero_aleatorio = random.randint(0, len(mazo_gen)-1)
    return robar_aux(mano, mazo_gen, numero_aleatorio, 0, len(mazo_gen), [])

def robar_aux(mano, mazo_gen, numero_aleatorio, indice, largo, mazo_nuevo):
    '''Funcion auxiliar de robar'''
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
        print(cian_negrita + "\nEste es el mazo del jugador1:" + resetear + " ", jugador1)
        print(amarillo_negrita+ "\nEste es el mazo del jugador2:" + resetear + " ", jugador2)
        return turnos_aux(jugador1, jugador2, mazo_general, 0, [], [])

def turnos_aux(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2):
    '''Funcion que controla los turnos con una bandera'''
    #Condiciones de parada
    if len(mazo_general) == 0:
        return "El mazo se ha quedado sin cartas! La partida queda en empate"
    elif len(establo1) == 5:
        return cian_negrita + r"""

        
 _____ _     _                       _              __    _                                         _       _ 
|  ___| |   (_)                     | |            /  |  | |                                       | |     | |
| |__ | |    _ _   _  __ _  __ _  __| | ___  _ __  `| |  | |__   __ _    __ _  __ _ _ __   __ _  __| | ___ | |
|  __|| |   | | | | |/ _` |/ _` |/ _` |/ _ \| '__|  | |  | '_ \ / _` |  / _` |/ _` | '_ \ / _` |/ _` |/ _ \| |
| |___| |   | | |_| | (_| | (_| | (_| | (_) | |    _| |_ | | | | (_| | | (_| | (_| | | | | (_| | (_| | (_) |_|
\____/|_|   | |\__,_|\__, |\__,_|\__,_|\___/|_|    \___/ |_| |_|\__,_|  \__, |\__,_|_| |_|\__,_|\__,_|\___/(_)
           _/ |       __/ |                                              __/ |                                
          |__/       |___/                                              |___/                                 

          
                                                              ▒▓▓▓▒ ░                          ▒░   ░ ░  ▒         ░░▒▒░      ▒  ▒ 
 ░░░░░░░░░░░░░           ░  ░   ░              ░░░░░░ ░░░░▒▓                         ░░    ▒░   ▒                 ░ ▒   
 ░░░░░░░░░░░░░       ░      ░    ░            ▒░░░░░░░   ░░░▒                          ▒     ░   ▒  ░ ▒            ░    
 ░░░░░░░░░░░░░       ░   ░  ░   ░            ▓  ░░░░░░░░░░░░░                           ▒░     ░   ▒▒   ░          ▒   ░
 ░░░░░░░░░░░░░       ░   ░  ░                ░  ░░░░░░░░░░░░░▓░                       ▒▓▓░▒         ▒░   ▒  ░     ▒   ░▒
 ░░░░░░░░░░░░░       ░      ░    ░      ▒░        ░░░░░░░░░▒▒▓ ▒  ░               ▒░▓  ░░▓▒▒░        ▒░   ▒▒░░░ ░▒   ░░▒
 ░░░░░░░░░░░░░       ░      ░   ░      ▒ ▓▒  ░      ░░░░░░ ░░░░ ░ ▓  ▓       ▒▓ ▓   ▓░░░░░▒  ▒░            ▒░░░▒ ░ ▒  ▒▒
 ░░░░░░░░░░░░░           ░  ░   ░   ░░ ▓▓▓▓▓    ░          ▒░░░  ▒ ░    ░░        ▒▒░░░░░░▒   ░▒░          ░▒░░░▒░▒  ▒▒▒
 ░░░░░░░░░░░░░       ░   ░  ░      ▒▒  ▓▓▓▓▒░    ▒▒    ░░ ▒ ▓▓░░  ░  ░░░         ░░░░░░░░▒▓      ▒░         ░░░░░░░░▒▒▒▒
 ░░░░░░░░░░░░░           ░  ░   ░     ▓▓▓▓▓▓ ░               ░▓▓  ░ ░░░░░      ░▒▓                ░░░       ░░░░░░░░▒▒▒▒
 ░░░░░░░░░░░░░   ░▒░ ░   ░  ░  ░░ ▓▒ ▓▓▓▓▓▓▓▓▒             ▒ ░▓░░░▒ ░░ ░░░░░  ░▒░░      ░▓        ▒░░▒░░     ░░░░░░░░▒░▒
 ░░░░░░░░░░░░░      ▒  ▓▒▓  ░▒▓▓▓▓░  ▓▓▓▓▓▓▓▓ ▒           ▒▒▓░  ▒  ░░▓   ░░  ░▒         ▒         ▒░░░▒ ▒░    ░░░░░░░▒░░
 ░░░░░░░░░░░░░    ░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ▓▓░▓▓▓▓▓▓▒▓▓▓ ▒     ▒ ▓▓▓▓▒░░▒ ▒  ░ ░░░░░▓ ▒       ░▒          ░▒▒▒░  ░▒░  ░░░░░░░░░
 ░░░░░░░░░░░░░    ░░▒▒ ▓▓▓▓▓▓▓▓▓▓▓▒ ▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▒▓▒ ▓▓▓▓▓     ▓▓▓▓▓  ░░░ ░▓       ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ░░░░░░░░░░░░░        ▒▒  ▓▓▓▓▓▓▓▓░ ▓▓▓▓▓▓▓▓▓░ ▓▓▓▓▓ ░▓▓▓▒▓▓      ▓▓▓▒▓▓▒░░░▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ░░░░░░░░░░░░░    ░░▒  ▓▓ ▓▓▓▓▓▓▓▒░▓▓▓▓▓▓▓▓▓▓░   ▓▓░▓▓▓▓▓▓▓░   ▒▓ ▓   ░▓▓░░▓       ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ░░░░░░░ ░░░░░░░▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▒▓▓▓▓▓▓▓▓▓ ░▒   ▓▓▓▓▓▓▓▓      ▒  ▒ ▓▒▓▓ ░       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ░░░░░░░░░░░  ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓   ░░░▒     ▓▒▓▓▓░▓    ░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ░░░░░░░░░░░░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓     ░   ░   ▓ ▓▓▓▒░  ▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓
 ░░░░░░░░░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░ ░░░░   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒▓▓▓▓▓▓▓▓▓▓▓
 ░░░░░░░░▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ ░   ▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓   ▓▓▓▓▓▓▓▓▓▓▓
░░░░░░░▒ ▓▓     ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓   ░▓▓▓▓▓▓▓▓▓▓▓
░░░░ ▓░▓  ░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓
▓▒░░ ░░░░░░░ ▓▓▓▓▓▓▓▓▓▓▓▓▓    ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒▓▓     ▒▓▓▓▓▓▓▓▓▓▓▓
▓ ░░░░░░░░░▒▓▓▓▓▓▓▓   ▓ ░░░ ▓▓▓▓▓▓▓▓▓▓▓▓▓▒   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░      ▓▓▓▓▓▓▓▓▓▓▓
▓▓▒░░░░░░  ▓▓▓▓▓▓    ▒▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▒ ░░░░░ ░▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░    ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓  ░░░░ ▒▓▓▓▓▓▓   ▒▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓
 ▓▓▓▓░░░░  ▓▓▓▓▓▓   ▒    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░ ▒▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓        ░▓▓▓▓▓ ▓░░▒▓▓▓▓
  ▓▓▓▒░░░  ▓▓▓▓▓▓   ▒    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓         ░▓▓ ▓       ▓▓▓▓
  ▓▓▓▒░░░░▒▓▓▓▓▓▓   ▒▒   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▒░░ ▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ░░░▒      ░▒░▓▓▓▓▓
   ▓▓▓  ░░▒▓▓▓▓▓▓   ▒▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒▒░▒▓▓▓▓▓▓▓▓▓▓▓░░░▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓          ▓▓         ▓▓▓▓▓▓▓▓
    ▓▓▓▒ ░▒▓▓▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓          ▒▒            ▓▓▓▓▓▓▓
     ▓▓▓  ░▓▓▓▓▓▓    ▒▒  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓░▓▓           ▒          ▒▓▓▓▓▓▓▓▓▓▓
      ▓▓▓ ▓▓▓▓▓▓▓   ░░▒   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ▓▓                      ▒▓▓▓▓▓▓▓▓▓▓▓▓
       ▓▓▓░▓▓▓▓▓ ░░ ░░    ▓▓▓▓▓▓▓▓▓▓▓▓ ▒▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓ ▓▓▓▓▓ ▓▓                     ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▓▓▓░▓▓▓▓░░▓░░░▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▓▓                    ▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▓▓▓▒▓▓▓░▓▓░░░░   ▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓░▓▓                 ░  ▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
          ▓▓▓░▓▓▓▓ ░░░░░░ ▓▓▓▓▓▓▓▓▓▓▓░░░░░▒▒▒▒▓▓▓▓▒▒▓▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓ ▓           ▓▓ ▓▓   ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
           ▓▓▓▒▓▓▓     ▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░▒▒▒▓▓▓▓ ▓ ▒░▒▒░▒▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒       ▒            ▓▒         ░▒▓▓▓▓▓▓▓▓▓▓▓▓
            ▓▓▓▓▓       ▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒   ░▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓                 ▓░▒             ▓▓▓▓▓▓▓▓▓▓▓▓▓
             ▓▓▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒░  ▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒ ▓▓▓▓░                ▓ ▓            ▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ▓             ▓▓▓▒▒      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░  ▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▓ ▓▓▓▓▒               ▓░▒           ▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                ▓▓▓▓▓   ▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓░▓              ▓░░▒▒▒▓   ▓  ▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                  ▓▓▓ ░▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▒▓                     ▓  ▓▓ ▓ ▒▓▓▒░░  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
   ▓▓▒            ░▓▓▓▓ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▓ ▒░░░░░░                  ▓▓▓░▓ ▓▒ ▓▓▓▓▓▓▓▓▓ ▓▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▒                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▒  ░   ░░              ▓▓░▓▒ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▒ ░▒▓▓▒▒░  ░▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓                    ░▓▓▒ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓               ░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ░                      ▓▓▓▓ ▓▓▓▓▓▓▓▓░░▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    ▓▓░ ▓▓ ▓▓▓▓▓▓▓▓▓▓▒  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▒                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓    ▓▓           ▓   ░▒▒▓▒▒░ ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░ ▓▒    ▓ ▒ ▓▒  ▓  ▓▓▓▓ ▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░▓▓▓▓▓▓▒  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▒▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ▒▓░ ░▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ▓▓▒▓▓▓▓▓░ ░▒░ ▒▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
         ▒▒ ▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               ▓▓░ ░░░░░░░░░  ░▒▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓         ░░▓▒▒▓▓▓▓▓ ▓░   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒ ▓▓       ░░░░░░░░░░░░░░░░░  ▓▒▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
   ▒          ░▓▒▓░▒▓▓  ▓   ▓▓▓▓▓▓▓▓▓ ▒          ▒░▓▒░   ░░░░░░░░░░░░░░░░░░░░  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ░▓      ░░░     ▓▒  ░    ▓▓▓▓▓▓▓▓              ▓░▓▓▓░░░░░░░░░░░░░░░░░░░░░░░ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
      ▒▓  ░▓ ░░        ▓ ▒   ▓▓▓▓▓▓▓                  ▓░░░░░░░░░░░░░░░░░░░░░░░░░ ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
   ░▓▓   ░   ░                ▓▓▓▓▓▓                  ░░░░░░░░░░░░░░░░░░░░░░░░░░  ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓  ░░░░░░░       ░   ▓▒   ▓▓▓▓▓▓▓  ▓▒▒             ░░░░░░░░░░▓▒   ▒▒░░░░░░░░░ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ░░ ░░░░░░░░░                 ▓▓▓▓▓▓▓     ▓▓          ▒░░░░░░░░▒      ▒░░░░░░░░░ ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ░░ ░░░░░░░░░░             ▒   ▓▓▓▓▓▓░      ▓▒         ░▒░░░░░░▒        ▒░░░░░░░░ ▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 ░░░░░░░░░░░░░          ░▓░░  ░░░░░  ░  ▓    ▓          ▓░░░░░▒    ░▒  ░▒░░░░░░░░ ░▓          ▓ ▓ ▓▓▓▓   ▓▓▓ ▓▓▓▓▓▓▓▓▓▓ 
 ░░░░░░░░░░░░░       ░  ▓░░░     ▓▓▓▓▓░      ░          ▓░░░░░         ░░░░░░░░░░ ░               ░    ░░░░░░           
 ░░░░░░░░░░░░░         ░ ░░▓    ▒▓▓▓▓▓▓ ░   ░▓         ░▒░░░░░        ▒░░░░░░░░░░▒▒             ░  ░           ░        
 ░░░░░░░░░░░░░       ░ ▒░░░░░    ▓      ░░░░▒          ▓░░░░░░░▒    ░ ░░░░░░░░░░ ░               ░               ░      
 ░░░░░░░░░░░░░         ░░░░░    ░░░░░░ ░░░░▓░░░        ▓░░░░░░░░░░░░░░░░░░░░░░░░▒                               ░       
 ░░░░░░░░░░░░░       ░  ░       ░░░   ░ ░░ ░░░░░░░░ ░ ░░░░░░░░░░░░░░░░░░░░░░░░░░             ░                    ░░    
 ░░░░░░░░░░░░░       ░░ ░░      ░░      ▒░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░               ░              ░░  ░░ ░    
 ░░░░░░░░░░░░░        ░▓░       ▒▒░░░▒▓  ░░░░░░░░░░░▓▒▒ ░  ░░░░░░░░░░░░░░ ░░▒▓               ░            ░             
 ░░░░░░░░░░░░░       ░                   ░ ░░░░░░░░                       ░░                 ░                          
 ░░░░░░░░░░░░░       ░  ▒▓               ░   ░░ ░░▒     ░ ░            ░ ▓                  ▒             ░             
 ░░░░░░░░░░░░░       ░   ▒▓                   ░ ░░         ░▓ ░▒░░▒░ ▓                      ▒                ░          
 ░░░░░░░░░░░░░       ░   ░░░░                ░ ░                                            ▒      


        """
    elif len(establo2) == 5:
        return verde_negrita + "El jugador 2 ha ganado, felicidades!" + resetear
   
    # Turno del primer jugador
    elif turno == 0: 
        sacar_carta = robar(mazo_jugador1, mazo_general)
        print(cian_negrita + "\n================> Es el turno del jugador 1 estas son tus cartas: " + resetear)
        print(blanco_negrita + f"{mazo_jugador1}" + resetear)
        input("\nDigite cualquier tecla para comer una carta del mazo: ")
        mazo_jugador1 = sacar_carta[0]
        mazo_general = sacar_carta[1]
        print("\nEsta es la carta que comiste: " + verde_negrita, mazo_jugador1[len(mazo_jugador1)-1] + resetear)
        # Si la carta que salio es de desventaja
        if comprobar_tipo(mazo, mazo_jugador1[len(mazo_jugador1)-1]) == "Desventaja":
            print(rojo_negrita + "\nHaz comido una carta de desventaja!" + resetear)
            print("Por lo que se te sacrificara una carta automaticamente de tu mano")
            eliminar_carta = eliminar_elemento(mazo_jugador1, mazo_jugador1[len(mazo_jugador1)-1]) # ya que la carta estaria de ulitmo siempre
            mazo_sacrificado = sacrificar(eliminar_carta)
            print(rojo_negrita + "\nTu mano se actualizo al siguiente: "  + blanco_negrita + f"{mazo_sacrificado}" + resetear)
            return turnos_aux(mazo_sacrificado, mazo_jugador2, mazo_general, turno + 1, establo1, establo2)
        elif len(mazo_jugador1) > 7:
            print(rojo_negrita + "\nTu mano supera las 7 cartas, por lo que se te descartara aleatoriamente una carta" + resetear)
            mano_descartar_carta_extra = descartar(mazo_jugador1)
            print(cian_negrita + "\nTu mano actual es el siguiente: " + resetear)
            print(blanco_negrita + f"\n{mano_descartar_carta_extra}" + resetear)
            print(cian_negrita + "\nEste es tu establo actual: " + resetear)
            print(blanco_negrita + f"\n{establo1}" + resetear)
            return verificar_carta_jugador1(mano_descartar_carta_extra, mazo_jugador2, mazo_general, turno, establo1, establo2)
        else:
            print(cian_negrita + "\nTu mano actual es el siguiente: " + resetear)
            print(blanco_negrita + f"\n{mazo_jugador1}" + resetear)
            print(cian_negrita + "\nEste es tu establo actual: " + resetear)
            print(blanco_negrita + f"\n{establo1}" + resetear)
            return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    
     # Turno del segundo jugador
    else:
        sacar_carta = robar(mazo_jugador2, mazo_general)
        print(amarillo_negrita + "\n================> Es el turno del jugador 2 estas son tus cartas: " + resetear)
        print(blanco_negrita + f"{mazo_jugador2}" + resetear)
        input("\nDigite cualquier tecla para comer una carta del mazo: ")
        mazo_jugador2 = sacar_carta[0]
        mazo_general = sacar_carta[1]
        print("\nEsta es la carta que comiste: " + verde_negrita, mazo_jugador2[len(mazo_jugador2)-1] + resetear)
        # Si la carta que salio es de desventaja
        if comprobar_tipo(mazo, mazo_jugador2[len(mazo_jugador2)-1]) == "Desventaja":
            print(rojo_negrita + "\nHaz comido una carta de desventaja!" + resetear)
            print("Por lo que se te sacrificara una carta automaticamente de tu mano")
            eliminar_carta = eliminar_elemento(mazo_jugador2, mazo_jugador2[len(mazo_jugador2)-1]) # ya que la carta estaria de ulitmo siempre
            mazo_sacrificado = sacrificar(eliminar_carta)
            print(rojo_negrita + "\nTu mano se actualizo al siguiente: " + blanco_negrita + f"{mazo_sacrificado}" + resetear)
            return turnos_aux(mazo_jugador1, mazo_sacrificado, mazo_general, turno - 1, establo1, establo2)
        elif len(mazo_jugador2) > 7:
            print(rojo_negrita + "\nTu mano supera las 7 cartas, por lo que se te descartara aleatoriamente una carta" + resetear)
            mano_descartar_carta_extra = descartar(mazo_jugador2)
            print(amarillo_negrita + "\nTu mano actual es el siguiente: " + resetear)
            print(blanco_negrita + f"\n{mano_descartar_carta_extra}" + resetear)
            print(amarillo_negrita + "\nEste es tu establo actual: " + resetear)
            print(blanco_negrita + f"\n{establo2}" + resetear)
            return verificar_carta_jugador2(mazo_jugador1, mano_descartar_carta_extra, mazo_general, turno, establo1, establo2)
        else:
            print(amarillo_negrita + "\nTu mano actual es el siguiente: " + resetear)
            print(blanco_negrita + f"\n{mazo_jugador2}" + resetear)
            print(amarillo_negrita + "\nEste es tu establo actual: " + resetear)
            print(blanco_negrita + f"\n{establo2}" + resetear)
            return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
        

def verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2):
    '''Funcion que tiene los comandos para ver la mano y establo del jugador 2 o el mazo completo y verifica que el input sea un numero'''
    carta = input("\nPresiona el numero de cual quieres utilizar (primera, segunda, tercera...): " )
    if carta == "mazo":
        print(blanco_negrita + "\nEste es el mazo: " + resetear)
        print(f"\n{mazo_general}")
        print(cian_negrita + "\nEstas son tus cartas: " + resetear)
        print(blanco_negrita + f"\n{mazo_jugador1}" + resetear)
        print(cian_negrita + "\nEste es tu establo actual: " + resetear)
        print(blanco_negrita + f"\n{establo1}" + resetear)
        return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif carta == "rival":
        print(blanco_negrita + "\nEsta es la mano y establo del rival: " + resetear)
        print(amarillo_negrita + "\nMazo del rival: " + resetear, mazo_jugador2)
        print(amarillo_negrita + "\nEstablo del rival: " + resetear, establo2)
        return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif len(carta) != 1:
        print(rojo_negrita + "Error, por favor selecciona solamente numeros [1,2,3,...]" + resetear)
        return verificar_carta_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif 49 <= ord(carta) <= 55:
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
    '''Funcion que aplica las acciones de las cartas al jugador 1 y pasa el turno'''
    print("Jugaste esta carta: " + verde_negrita + f"{mazo_jugador1[carta]}" + resetear)

    # Si la carta seleccionada es unicornio
    if comprobar_tipo(mazo, mazo_jugador1[carta]) == "Unicornio":
        print(blanco_negrita + "\nHaz pasado un unicornio al establo!" + resetear)
        print(verde_subrayado + "Tu establo se actualizo:" + resetear + " ", establo1 + [mazo_jugador1[carta]])
        return turnos_aux(eliminar_elemento(mazo_jugador1, mazo_jugador1[carta]), mazo_jugador2, mazo_general, turno + 1, establo1 + [mazo_jugador1[carta]], establo2)
    
     # Si la carta seleccionada es de ventaja
    elif comprobar_tipo(mazo, mazo_jugador1[carta]) == "Ventaja":
        print(blanco_negrita + "\nHaz hecho que el rival descarte un carta!" + resetear)
        descartar_input = input("Digite la palabra " + azul_negrita +  "mano" + resetear + " para hacer que el rival descarte una carta de su mano o " + azul_negrita + "establo"  + resetear + " para hacer que el rival descarte una carta de su establo: ")
        if descartar_input == "establo":
            if len(establo2) == 0:
                print(rojo_negrita + "\nEl establo rival esta vacio, por lo que se descartara una carta de la mano del rival!" + resetear)
                print(blanco_negrita + "El rival ha descartado una carta de su mano!" + resetear)
                mano_descartada = descartar(mazo_jugador2)
                print(verde_subrayado + "\nLa mano del rival se actualizo:" + resetear + " " +  f"{mano_descartada}")
                return turnos_aux(eliminar_elemento(mazo_jugador1, mazo_jugador1[carta]), mano_descartada, mazo_general, turno + 1, establo1, establo2)
            else:
                print(blanco_negrita + "\nEl rival ha descartado una carta de su establo!" + resetear)
                establo_descartado = descartar(establo2)
                print(verde_subrayado + "El establo rival se actualizo:" + resetear + " " + f"{establo_descartado}")
                return turnos_aux(eliminar_elemento(mazo_jugador1, mazo_jugador1[carta]), mazo_jugador2, mazo_general, turno + 1, establo1, establo_descartado)
        elif descartar_input == "mano":
            print(blanco_negrita + "\nEl rival ha descartado una carta de su mano!" + resetear)
            mano_descartada = descartar(mazo_jugador2)
            print(verde_subrayado + "La mano del rival se actualizo:" + resetear + " " + f"{mano_descartada}")
            return turnos_aux(eliminar_elemento(mazo_jugador1, mazo_jugador1[carta]), mano_descartada, mazo_general, turno + 1, establo1, establo2)
        else:
            print(rojo_negrita + "\nDigite exactamente si quieres descartar una carta de la mano o del establo del rival\n" + resetear)
            return acciones_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
    
     # Si la carta seleccionada es de magia
    elif comprobar_tipo(mazo, mazo_jugador1[carta]) == "Magia":
        print(blanco_negrita + "Haz elegido una carta de magia!, por lo que robas una carta aleatoria" + resetear)
        robar_input = input("\nDigite la palabra " + azul_negrita + "mazo" + resetear +  " si quieres robar una carta del mazo o " + azul_negrita + "establo" + resetear + " si quieres robar una carta del establo rival: ")
        if robar_input == "mazo":
            if mazo_general == []:
                print(rojo_negrita + "\nEl mazo se ha quedado sin cartas!" + resetear)
                return "\nLa partida queda en empate"
            else:
                print(blanco_negrita + "\nHaz robado una carta del mazo!" + resetear)
                roba = robar(mazo_jugador1, mazo_general)
                eliminar_carta = eliminar_elemento(roba[0], mazo_jugador1[carta])
                print(verde_subrayado + "Tu mano se actualizo al siguiente:" + resetear + " ", eliminar_carta)
                return turnos_aux(eliminar_carta, mazo_jugador2, roba[1], turno + 1, establo1, establo2)
        elif robar_input == "establo":
            if len(establo2) == 0:
                print(rojo_negrita + "\nEl establo esta vacio, por lo que se robara una carta del mazo" + resetear)
                print(blanco_negrita + "Se ha robado una carta del mazo!" + resetear)
                roba = robar(mazo_jugador1, mazo_general)
                eliminar_carta = eliminar_elemento(roba[0], mazo_jugador1[carta])
                print(verde_subrayado + "\nTu mano se actualizo al siguiente:" + resetear + " ", eliminar_carta)
                return turnos_aux(eliminar_carta, mazo_jugador2, roba[1], turno + 1, establo1, establo2)
            else:
                print(blanco_negrita + "\nHaz robado una carta del establo rival!" + resetear)
                roba = robar(mazo_jugador1, establo2)
                eliminar_carta = eliminar_elemento(roba[0], mazo_jugador1[carta])
                print(verde_subrayado + "Tu mano se actualizo:" + resetear + " ", eliminar_carta)
                return turnos_aux(eliminar_carta, mazo_jugador2, mazo_general, turno + 1, establo1, roba[1])
        else:
            print(rojo_negrita + "\nDigite exactamente si quieres robar una carta del establo rival o del mazo" + resetear)
            return acciones_jugador1(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
            
def verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2):
    '''Funcion que tiene los comandos para ver la mano y establo del jugador 1 o el mazo completo y verifica que el input sea un numero'''
    carta = input("\nPresiona el numero de cual quieres utilizar (primera, segunda, tercera...): " )
    if carta == "mazo":
        print(blanco_negrita + "\nEste es el mazo: " + resetear)
        print(f"\n{mazo_general}")
        print(amarillo_negrita + "\nEstas son tus cartas: " + resetear)
        print(blanco_negrita + f"\n{mazo_jugador2}" + resetear)
        print(amarillo_negrita + "\nEste es tu establo actual: " + resetear)
        print(blanco_negrita + f"\n{establo2}" + resetear)
        return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif carta == "rival":
        print(blanco_negrita + "\nEsta es la mano y establo del rival: " + resetear)
        print(cian_negrita + "\nMazo del rival: " + resetear, mazo_jugador1)
        print(cian_negrita+ "\nEstablo del rival: " + resetear, establo1)
        return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif len(carta) != 1:
        print(rojo_negrita + "Error, por favor selecciona solamente numeros [1,2,3,...]" + resetear)
        return verificar_carta_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2)
    elif 49 <= ord(carta) <= 55:
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
    '''Funcion que aplica las acciones de las cartas al jugador 2 y pasa el turno '''

    # Si la carta seleccionada es unicornio
    print("Jugaste esta carta: " + verde_negrita + f"{mazo_jugador2[carta]}" + resetear)
    if comprobar_tipo(mazo, mazo_jugador2[carta]) == "Unicornio":
        print(blanco_negrita + "\nHaz pasado un unicornio al establo!" + resetear)
        print(verde_subrayado + "Tu establo se actualizo:" + resetear + " ", establo2 + [mazo_jugador2[carta]])
        return turnos_aux(mazo_jugador1, eliminar_elemento(mazo_jugador2, mazo_jugador2[carta]), mazo_general, turno - 1, establo1, establo2 + [mazo_jugador2[carta]])
    
    # Si la carta seleccionada es de ventaja
    elif comprobar_tipo(mazo, mazo_jugador2[carta]) == "Ventaja":
        print(blanco_negrita + "\nHaz hecho que el rival descarte un carta!" + resetear)
        descartar_input = input("Digite la palabra " + azul_negrita +  "mano" + resetear + " para hacer que el rival descarte una carta de su mano o " + azul_negrita + "establo"  + resetear + " para hacer que el rival descarte una carta de su establo: ")
        if descartar_input == "establo":
            if len(establo1) == 0:
                print(rojo_negrita + "\nEl establo rival esta vacio, por lo que se descartara una carta de la mano del rival!" + resetear)
                print(blanco_negrita + "El rival ha descartado una carta de su mano!" + resetear)
                mano_descartada = descartar(mazo_jugador1)
                print(verde_subrayado +  "La mano del rival se actualizo:" + resetear + " " + f"{mano_descartada}")
                return turnos_aux(mano_descartada, eliminar_elemento(mazo_jugador2, mazo_jugador2[carta]), mazo_general, turno - 1, establo1, establo2)
            else:
                print(blanco_negrita + "\nEl rival ha descartado una carta de su establo!" + resetear)
                establo_descartado = descartar(establo1)
                print(verde_subrayado + "El establo rival se actualizo:" + resetear + " " + f"{establo_descartado}")
                return turnos_aux(mazo_jugador1, eliminar_elemento(mazo_jugador2, mazo_jugador2[carta]), mazo_general, turno - 1, establo_descartado, establo2)
        elif descartar_input == "mano":
            print(blanco_negrita + "\nEl rival ha descartado una carta de su mano!" + resetear)
            mano_descartada = descartar(mazo_jugador1)
            print(verde_subrayado + "La mano del rival se actualizo:" + resetear + " " + f"{mano_descartada}")
            return turnos_aux(mano_descartada, eliminar_elemento(mazo_jugador2, mazo_jugador2[carta]), mazo_general, turno - 1, establo1, establo2)
        else:
            print(rojo_negrita + "\nDigite exactamente si quieres descartar una carta de la mano o del establo del rival\n" + resetear)
            return acciones_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)
        
    # Si la carta seleccionada es de magia
    elif comprobar_tipo(mazo, mazo_jugador2[carta]) == "Magia":
        print(blanco_negrita + "Haz elegido una carta de magia!, por lo que robas una carta aleatoria" + resetear)
        robar_input = input("\nDigite la palabra " + azul_negrita + "mazo" + resetear +  " si quieres robar una carta del mazo o " + azul_negrita + "establo" + resetear +  " si quieres robar una carta del establo rival: ")
        if robar_input == "mazo":
            if mazo_general == []:
                print(rojo_negrita + "El mazo se ha quedado sin cartas!" + resetear)
                return "\nLa partida queda en empate"
            else:
                print(blanco_negrita + "\nHaz robado una carta del mazo!" + resetear)
                roba = robar(mazo_jugador2, mazo_general)
                eliminar_carta = eliminar_elemento(roba[0], mazo_jugador2[carta])
                print(verde_subrayado + "\nTu mano se actualizo al siguiente:" + resetear + " ", eliminar_carta)
                return turnos_aux(mazo_jugador1, eliminar_carta, roba[1], turno - 1, establo1, establo2)
        elif robar_input == "establo":
            if len(establo1) == 0:
                print(rojo_negrita + "\nEl establo esta vacio, por lo que se robara una carta del mazo" + resetear)
                print(blanco_negrita + "Se ha robado una carta del mazo!" + resetear)
                roba = robar(mazo_jugador2, mazo_general)
                eliminar_carta = eliminar_elemento(roba[0], mazo_jugador2[carta])
                print(verde_subrayado + "\nTu mano se actualizo al siguiente:" + resetear + " ", eliminar_carta)
                return turnos_aux(mazo_jugador1, eliminar_carta, roba[1], turno - 1, establo1, establo2)
            else:
                print(blanco_negrita + "\nHaz robado una carta del establo rival!" + resetear)
                roba = robar(mazo_jugador2, establo1)
                eliminar_carta = eliminar_elemento(roba[0], mazo_jugador2[carta])
                print(verde_subrayado + "Tu mano se actualizo:" + resetear + " ", eliminar_carta)
                return turnos_aux(mazo_jugador1, eliminar_carta, mazo_general, turno - 1, roba[1], establo2)
        else:
            print(rojo_negrita + "\nDigite exactamente si quieres robar una carta del establo rival o del mazo" + resetear)
            return acciones_jugador2(mazo_jugador1, mazo_jugador2, mazo_general, turno, establo1, establo2, carta)

                            
res = iniciar_juego()
print(res)