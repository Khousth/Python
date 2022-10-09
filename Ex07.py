# 7º Exercício => Faça um sistema que some cinco produtos, subitrai o valor do pagamento e identifica o troco:

# Apresentação do Sistema:
print("\nSimulador de caixa com 5 produtos:\n")

# Entrada de valores:
a = int(input('Digite o valor do primeiro produto: '))
b = int(input('Digite o valor do segundo produto: '))
c = int(input('Digite o valor do terceiro produto: '))
d = int(input('Digite o valor do quarto produto: '))
e = int(input('Digite o valor do quinto produto: '))

# Entrada de valores:
f = int(input('\nDigite o valor do pagamento: '))

# Processamento/Conta:
v = f - (a + b + c + d + e)

# Saída de valores:
print(f"\nSeu troco é de {v} reias!\n")