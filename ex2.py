################################################################
# Descrição: Calcular o somatório dos grãos de trigo em um
# tabuleiro de xadrez, começando com 1 grão no primeiro quadro
# e dobrando a quantidade nos quadros seguintes, até o
# sexagésimo quarto quadro.
#
# Parâmetros de entrada: Nenhum.
#
# Valores de saída: Somatório total dos grãos de trigo
# distribuídos nos 64 quadros.
#
# Autor: Samuel Guimarães
################################################################

q = 2
a1 = 1
n = 64 

Sn = a1 * (q**n - 1) // (q - 1)
print(f"O somatório total dos grãos de trigo distribuídos nos 64 quadros é: {Sn}")
