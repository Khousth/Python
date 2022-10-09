# 21º Exercício => Faça um sistema operacional de contas:

# Apresentação do Sistema:
print("\nSistema Operacional de Contas:\n")

# Entrada de Valores:
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

# Saída de Valores:
print("\nCalculadora\n")
print("1 - Multiplicação")
print("2 - Adição")
print("3 - Divisão")
print("4 - Subtração")
print("5 - Fim do processo\n")

# Etapa de Decisão:
resposta = int(input("Digite sua opção: "))

if resposta == 1:
    print(v1 * v2)
    print("\nFim do programa\n")
elif resposta == 2:
    print(v1 + v2)
    print("\nFim do programa\n")
elif resposta == 3:
    if v1 == 0  or v2 == 0:
        print("\nErro\n")
        print("\nFim do programa\n")
    else:
        print(v1 / v2)
        print("\nFim do programa\n")
elif resposta == 4:
    print(v1 - v2)
    print("\nFim do programa\n")
elif resposta == 5:
    print("\nFim do programa\n")
else:
    print("\nComando não encontrado.\n")