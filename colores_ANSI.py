rojo_negrita = "\033[1;91m"
verde_subrayado = "\033[4;92m"
azul_fondo_blanco = "\033[44;97m"
rojo = "\033[91m"
verde = "\033[92m"
azul = "\033[94m"
resetear = "\033[0m"


# Nota: si no pones el resetar, todo lo que sigue se imprimira de dicho color
print(rojo_negrita + "Texto en rojo y negrita" + resetear)
print(verde_subrayado + "Texto en verde y subrayado" + resetear)
print(azul_fondo_blanco + "Texto con fondo azul y letras blancas" + resetear)
print(rojo + "Este es un texto en rojo" + resetear)
print("Hola")
input(verde_subrayado + "A ver si esto se imprime verde: " + resetear) # Si lo imprime 
