################################################################
# Descrição: Calcular a área total de uma residência,
# solicitando o nome, a largura e o comprimento de cada cômodo.
# O programa deve permitir o cadastro de vários cômodos,
# solicitando confirmação para continuar os cálculos.
#
# Parâmetros de entrada: Nome, largura e comprimento dos
# cômodos, além da confirmação para continuar.
#
# Valores de saída: Área individual de cada cômodo e
# área total da residência em metros quadrados.
#
# Autor: Samuel Guimarães
################################################################

area_total = 0

nome = input("Digite o nome do cômodo: ")
largura = float(input("Digite a largura do cômodo: "))
comprimento = float(input("Digite o comprimento do cômodo: "))

area = largura * comprimento
area_total += area

print(f"A área do cômodo {nome} é: {area} m²")

pergunta = input("Deseja cadastrar outro cômodo? (S/N): ")

while pergunta.upper() == "S":

    nome = input("Digite o nome do cômodo: ")
    largura = float(input("Digite a largura do cômodo: "))
    comprimento = float(input("Digite o comprimento do cômodo: "))

    area = largura * comprimento
    area_total += area

    print(f"A área do cômodo {nome} é: {area} m²")

    pergunta = input("Deseja cadastrar outro cômodo? (S/N): ")

print(f"\nA área total da residência é: {area_total} m²")