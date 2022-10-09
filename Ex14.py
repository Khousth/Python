# 14º Exercício => Faça um sistema para calcular se a pessoa está no peso ideal ou não:

# Apresentação do Sistema:
print("\nSistema que calcula o seu IMC:\n")

# Entrada de valores:
a = float(input("Digite o seu peso: "))
b = float(input("Digite a sua altura: "))

# Processamento/conta:
c = a / (b * b)

# Saída de valores:
print(f"\nO seu Índice de Massa Corporal é: {c:.2f}")

# Etapa de decisão:
if (c > 24.9):
    print("Fique atento, vocês está a cima do peso!\n")

elif (c < 18.5):
    print("Fique atento, vocês está a baixo do peso!\n")

else:
    print("Você está no peso ideal! Parabéns, continue assim!\n")