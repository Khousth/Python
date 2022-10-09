# 19º Exercício => Faça um sistema que diz a média do aluno e se foi aprovado ou não:

# Apresentação do Sistema:
print("\nSistema de Análise de Média Escolar:\n")

# Entrada de Valores:
p1 = float(input("Digite a nota da p1: "))
p2 = float(input("Digite a nota da p2: "))

# Conta/processamento:
m = (p1 + (2 * p2)) / 3

# Etapa de Decisão:
if m >= 5:
    print(f"Sua média foi {m:.2f} e você foi Aprovado!")
else:
    print(f"Sua média foi {m:.2f} e você foi Reprovado.")