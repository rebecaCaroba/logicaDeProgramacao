import math
num = int(input('Digite um número (math): '))

def CalcFatorialMath(num):
    fat = math.factorial(num)
    return fat

print(f"O {num}! = {CalcFatorialMath(num)}")
    
def CalcFatorial(n):
    if n == 0 or n == 1:
        return 1
    
    fatorial = 1
    for i in range(1, n+1): # in range(inicio, fim, passo) / padrao -> in range(0, fim, 1)
        fatorial *= i
    return fatorial

# res = CalcFatorial(n)
# print(f"O fatorial de {n} é {res}")
n = int(input('Digite um número: '))
print(f"O fatorial de {n} é {CalcFatorial(n)}")

