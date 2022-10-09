# 10º Exercício => Faça um sistema que mostre qual variável é maior considerando semelhantes:

# Apresentação do Sistema:
print("\nSistema que mostra qual variavel é maior:\n")

# Entrada de valores:
a = int(input('Digite a primeira variável: '))
b = int(input('Digite a segunda variável: '))
 
# Etapa de Decisão
if (a > b):
    print("\nA primeira variável é maior!\n")

elif (a == b):
    print("\nAs variáveis são iguais!\n")

else:
    print("\nA segunda variável é menor!\n")