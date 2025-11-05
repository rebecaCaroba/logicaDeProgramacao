# Lê o tipo de chá real T
T = int(input("digite o tipo de chá"))

respostas = []
i = 0
acertos = 0

while (i < 5):
    deducao = int(input(f"Digite a dedução {i + 1}: "))
    respostas.append(deducao)

    if(respostas[i] == T):
        acertos += 1

    i += 1
     
print("Quantidade de acetos foi: ", acertos)