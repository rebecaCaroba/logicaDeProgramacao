carta1 = int(input("Digite o valor da carta 1: "))
carta2 = int(input("Digite o valor da carta 2: "))

def maximizarValorDasCartas(carta1, carta2):
    if(carta1 == carta2):
        return carta1
    
    if(carta1 > carta2):
        return carta1
    else:
        return carta2
    

print(maximizarValorDasCartas(carta1, carta2))