# 18º Exercício => Faça um sistema que analisa a velocidade de um automóvel.

# Apresentação do Sistema:
print("\nSistema de Análise de Velocidade de veículos:\n")

# Entrada de Valores:
a = float(input("Digite o valor da aceleração em m/s²: "))
b = float(input("Digite a velocidade inicial em m/s: "))
c = float(input("Digite o tempo de percurso em segundos: "))

# Conta/processamento:
d = b + a * c

# Saída de Valores:
print(f"\nA velocidade do veícluo é de {d} m/s")

# Etapa de Decisão:
if (d <= 40):
    print("O Veículo está muito lento\n")

elif (40 < d <= 60):
    print("Está Velocidade é permitida\n")

elif (60 < d <= 80):
    print("O veículo está em Velocidade de cruzeiro\n")

elif (80 < d <= 120):
    print("O Veículo está andando rápido\n")

elif (d > 120):
    print("O Veículo está andando muito rápido\n")

else:
    print()