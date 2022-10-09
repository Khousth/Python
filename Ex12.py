# 12º Exercício => Faça um sistema que calcule a área de um retângulo e que avisa caso a área seja maior que cem ou não.

# Apresentação do Sistema:
print("\nCalculadora de Área para Retângulos que diz se o terreno é grande ou pequeno:\n")

# Entrada de valores:
a = int(input('Digite a base do retângulo: '))
b = int(input('Digite a altura do retângulo: '))

# Processamento/conta:
c = a * b

# Saída de valores:
print("\nA área do retângulo é de:", c)

# Etapa de Decisão
if (c > 100):
    print("Se trata de um Terreno Grande!\n")

else:
    print("Se trata de um Terreno Pequeno!\n")