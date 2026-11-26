################################################################
# Descrição: Ler sucessivamente valores numéricos positivos
# e apresentar o somatório, a média e o total de valores lidos.
# O programa deve encerrar quando receber um valor negativo.
#
# Parâmetros de entrada: Valores numéricos fornecidos pelo
# usuário, até que seja informado um valor negativo.
#
# Valores de saída: Somatório, média e quantidade total
# de valores positivos informados.
#
# Autor: Samuel Guimarães
################################################################

total = []

num = int(input('Digite um número: '))

while num >= 0:
    if num > 0:
        total.append(num)

    num = int(input('Digite um número: '))

somatorio = sum(total)

if len(total) > 0:
    media = somatorio / len(total)
else:
    media = 0

print(f"\nA quantidade de números positivos digitados é: {len(total)}")
print(f"\nA somatória de todos os números é: {somatorio}")
print(f"\nA média geral é: {media}")