# 13º Exercício => Faça um sistema que mostre qual das três variáveis é maior:

# Apresentação do Sistema:
print("\nSistema que mostra o maior valor entre três variáveis:\n")

# Entrada de valores:
a = int(input('Digite a primeira variável: '))
b = int(input('Digite a segunda variável: '))
c = int(input('Digite a terceira variável: '))
 
# Etapa de Decisão:
if (a > b > c) or (a > c > b):
    print("\nA primeira variável é a maior!\n")

elif (b > a > c) or (b > c > a):
    print("\nA segunda variável é a maior!\n")

elif (c > a > b)  or (c > b > a):
    print("\nA terceira variável é a maior!\n")

else:
    print()