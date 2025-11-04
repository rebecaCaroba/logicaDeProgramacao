# Elabore um algoritmo que leia dois números reais: a base e o 
# expoente, e calcule o resultado da exponenciação (base^expoente).
# O programa deve:
# Utilizar função para realizar o cálculo.
# Tratar possíveis erros de entrada (ex: valor inválido).
# Mostrar o resultado formatado com duas casas decimais.


# Declaração de variaveis
base = int(input("Digite a base"))
expoente = int(input("Digite expoente"))


# Declarar função
def calcularExponenciacao(base, expoente): # 125
    try:
        if base == 0:
            return 1
    
        return base ** expoente # 5 ** 3 = 5*5*5= 125
    
    # Tratamento de erros
    except Exception as erro:
        return 'Erro: {erro}'
    except ZeroDivisionError:
        return 'Erro, divisão por zero.'
    except ValueError:
        return 'Erro, numeros invalidos'
    else:
        print('Outro...')
    finally:
        return 'execução finalizada'

print(f" O resultado é {calcularExponenciacao(base, expoente)} ")

