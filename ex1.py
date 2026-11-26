################################################################
# Descrição: Apresentar as potências de base 3, com expoentes
# de 0 até 15, utilizando laço de repetição, sem utilizar o
# operador de exponenciação (**).
#
# Parâmetros de entrada: Nenhum.
#
# Valores de saída: Resultados das potências de 3, do expoente
# 0 até o expoente 15.
#
# Autor: Samuel Guimarães
################################################################

base = 3

for i in range(16): # i = expoente
    resultado = 1

    for j in range(i): # j controla quantas multiplicações serão realizadas
        resultado = resultado * base

    print(resultado)