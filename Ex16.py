# 16º Exercício => Faça um sistema que confirma que três valores podem se tornar um triângulo retângulo.

# Entrada do Primeiro Valor:
print("\nSistema de Análise de Triângulos Retângulos:\n")

# Entrada de Valores:
a = float(input("Digite o valor da hipoternusa: "))
b = float(input("Digite o valor do primeiro cateto: "))
c = float(input("Digite o valor do segundo cateto: "))

# Etapa de Decisão:
if (a * a == b * b + c * c):
    print("\nOs valores inseridos podem formar um triângulo retângulo!\n")

else:
    print("\nOs valores inseridos não podem formar um triângulo retângulo!\n")