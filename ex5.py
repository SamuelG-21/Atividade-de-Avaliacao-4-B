################################################################
# Descrição: Apresentar o resultado inteiro da divisão de
# dois números quaisquer, utilizando laço de repetição,
# sem utilizar o operador de divisão com quociente inteiro.
#
# Parâmetros de entrada: Dois números, representando
# o dividendo e o divisor.
#
# Valores de saída: Quociente inteiro da divisão,
# representando quantas vezes o divisor cabe no dividendo.
#
# Autor: Samuel Guimarães
################################################################

n1 = int(input('Digite o dividendo: '))
n2 = int(input('Digite o divisor: '))
quociente = 0

while n1 > n2:
    n1 = n2 - n1
    quociente += 1

print(f"O quociente inteiro da divisão é: {quociente}")