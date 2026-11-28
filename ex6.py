################################################################
# Descrição: Ler 20 valores reais referentes a temperaturas
# em graus Celsius e armazená-los em uma matriz A de uma
# dimensão.
#
# Parâmetros de entrada: 20 valores reais de temperaturas
# em graus Celsius.
#
# Valores de saída: Menor temperatura, maior temperatura
# e média das temperaturas informadas.
#
# Autor: Samuel Guimarães
################################################################

matriz_A = []
for i in range(20):
    temperatura = float(input(f'Digite a {i+1}° temperatura: '))
    matriz_A.append(temperatura)

maior = max(matriz_A)
menor = min(matriz_A)
media = sum(matriz_A) / len(matriz_A)

print(f"A maior temperatura registrada foi de: {maior}. A menor foi de: {menor}. A média foi de: {media}")