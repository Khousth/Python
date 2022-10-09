# 15º Exercício => Faça um sistema que confirma que três valores podem se tornar um triângulo e informe qual tipo seria.

# Entrada do Primeiro Valor:
print("\nSistema de Análise de Triângulos\n")

# Entrada dos Valorres:
a = int(input('Digite o primeiro lado: '))
b = int(input('Digite o segundo lado: '))
c = int(input('Digite o terceiro lado: '))
 
# Etapa de Confirmação:
if (a + b > c) and (b + c > a) and (a + c > b):
    print('\nEstes valores podem ser convertidos em um triânglo,')

# Etapa de Decisão:
    if (a == b == c):
     print('E neste caso seria um Triângulo Equilátero!\nOnde todos os lados são iguais.\n')

    elif (a == b or b == c or c == a):
      print('E neste caso seria um Trinângulo Isóceles!\nOnde apenas dois lados são iguais.\n')

    else:
     print('E neste caso seria um Triângulo Escaleno!\nOnde nem um dos lados são iguais.\n')

# Etapa de Confirmação:
else:
    print('\nEstes valores não podem ser convertidos em um triânglo, sinto muito!\n')
