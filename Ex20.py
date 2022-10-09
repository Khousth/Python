# 20º Exercício => Faça um sistema que diz a média do aluno e quanto o aluno precisa para passar de ano.

# Apresentação do Sistema:
print("\nSistema de Análise de Média Escolar:\n")

# Entrada de Valores:
p1 = float(input("Digite a nota da P1: "))

# Conta/processamento:
media = 5
p2 = ((3 * media) - p1) / 2

# Saída de Valores:
print(f"Para passar de ano você precisa tirar {p2:.2}.")
