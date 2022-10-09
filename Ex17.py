# 17º Exercício => Faça um sistema para calcular se a pessoa está no peso ideal ou não dependendo do sexo:

# Apresentação do Sistema:
print("\nSistema que calcula o IMC basedo no sexo da pessoa:\n")

# Entrada de Valores:
a = float(input("Digite o seu peso: "))
b = float(input("Digite da sua altura: "))
c = input("Digite o seu sexo usando M ou F: ")

# Processamento/conta:
R = a / (b * b)

# Etapa de Decisão:
if (c == ("m") or ("M")):
    if (R < 20):
        print("\nAbaixo do peso, fique atento!\n")
    elif (20 <= R < 25):
        print("\nPeso ideal, continue assim!\n")
    elif (R >= 25):
        print("\nAcima do peso, fique atento!\n")

elif (c == ("f" or "F")):
    if (R < 19):
        print("\nAbaixo do peso, fique atento!\n")
    elif (19 <= R < 24):
        print("\nPeso ideal, continue assim!\n")
    elif (R >= 24):
        print("\nAcima do peso, fique atento!\n")
else:
    print()