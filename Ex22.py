# 22º Exercício => Faça um sistema operacional de contas para áreas:

# Apresentação do Sistema:
print("\nSistema Operacional de Contas para Áreas:\n")

# Entrada de Valores:
print("Calculadora de área")
print("1 - Triângulo")
print("2 - Quadrado")
print("3 - Retângulo")
print("4 - Círculo")
print("5 - Fim do processo")
resposta = int(input("\nDigite sua opção: "))

# Etapa de Decisão:
if resposta == 1:
    baset = float(input("Digite a base: "))
    alturat = float(input("Digite a altura: "))
    areat = (baset * alturat) / 2

    print(f"A área do triângulo é {areat}")
    print("\nFim do processo")

elif resposta == 2:
    baseq = float(input("Digite a base: "))
    areaq = baseq ** 2

    print(f"A área do quadrado é {areaq}")
    print("\nFim do processo")

elif resposta == 3:
    baser = float(input("Digite a base: "))
    alturar = float(input("Digite a altura: "))
    arear = baser * alturar

    print(f"A área do retângulo é {arear}")
    print("\nFim do processo")

elif resposta == 4:
    raioc = float(input("Digite o raio: "))
    pi = 3.14
    areac = pi * (raioc ** 2)

    print(f"A área do círculo é {areac}")
    print("\nFim do processo")

elif resposta == 5:
    print("\nFim do processo")