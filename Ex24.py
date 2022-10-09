# 24º Exercício => Sistema de Análise de Casamentos:

# Apresentação do Sistema:
print("\nSistema de Análise de Casamentos:\n")

# Entrada de Valores:
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ")
estado_civil = input("Digite seu estado civil (S/C/V/D): ")

# Etapa de Decisão:
if (sexo == "F" and estado_civil == "C"):
    tempo_casada = input("Digite o tempo de casada: ")
    print(f"\n{nome} - {sexo} - {estado_civil} - {tempo_casada}\n")
else:
    print(f"\n{nome} - {sexo} - {estado_civil}\n")
