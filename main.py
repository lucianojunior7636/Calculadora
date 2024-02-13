import math

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    else:
        return x / y

def potenciacao(x, y):
    return x ** y

def radiciacao(x):
    return math.sqrt(x)

def porcentagem(x, percentual):
    return x * (percentual / 100)

def logaritmo(x, base):
    return math.log(x, base)

def fatorial(x):
    return math.factorial(x)

def valor_absoluto(x):
    return abs(x)

def seno(x):
    return math.sin(x)

def cosseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

def arredondamento(x):
    return round(x)

def media(lista):
    return sum(lista) / len(lista)

def desvio_padrao(lista):
    media_lista = media(lista)
    variancia = sum((x - media_lista) ** 2 for x in lista) / len(lista)
    return math.sqrt(variancia)

def conversao_unidades(valor, unidade_origem, unidade_destino):
    if unidade_origem == "Celsius" and unidade_destino == "Fahrenheit":
        return valor * 9/5 + 32
    elif unidade_origem == "Fahrenheit" and unidade_destino == "Celsius":
        return (valor - 32) * 5/9
    else:
        return "Conversão não suportada."

def juros_simples(capital, taxa, tempo):
    return capital * taxa * tempo

def juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo - capital

def raiz_cubica(x):
    return x ** (1/3)

def exponencial(x):
    return math.exp(x)

def modulo(x, y):
    return x % y

def media_ponderada(valores, pesos):
    soma_valores_pesos = sum(valores[i] * pesos[i] for i in range(len(valores)))
    soma_pesos = sum(pesos)
    return soma_valores_pesos / soma_pesos

def potencia_de_10(expoente):
    return 10 ** expoente

def inverso(x):
    return 1 / x

def numero_euler():
    return math.e

def logaritmo_natural(x):
    return math.log(x)

def combinacao(n, k):
    return math.comb(n, k)

def permutacao(n, k):
    return math.perm(n, k)

def conjugado_complexo(complexo):
    return complexo.conjugate()

def parte_imaginaria(complexo):
    return complexo.imag

def parte_real(complexo):
    return complexo.real

def cotangente(x):
    return 1 / math.tan(x)

def calcular(expressao):
    try:
        return eval(expressao)
    except Exception as e:
        return "Erro: " + str(e)

def calculadora():
    while True:
        print("Selecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Radiciação")
        print("7. Porcentagem")
        print("8. Logaritmo")
        print("9. Fatorial")
        print("10. Valor Absoluto")
        print("11. Seno")
        print("12. Cosseno")
        print("13. Tangente")
        print("14. Arredondamento")
        print("15. Média")
        print("16. Desvio Padrão")
        print("17. Conversão de Unidades")
        print("18. Juros Simples")
        print("19. Juros Compostos")
        print("20. Raiz Cúbica")
        print("21. Exponencial")
        print("22. Módulo")
        print("23. Média Ponderada")
        print("24. Potência de 10")
        print("25. Inverso")
        print("26. Número de Euler")
        print("27. Logaritmo Natural")
        print("28. Combinação")
        print("29. Permutação")
        print("30. Conjugado Complexo")
        print("31. Parte Imaginária")
        print("32. Parte Real")
        print("33. Cotangente")
        print("34. Calcular Expressão Numérica")
        print("35. Sair")
        
        escolha = input("Digite sua escolha (1/2/3/4/5/6/7/8/9/10/.../35): ")

        if escolha == '35':
            print("Saindo da calculadora.")
            break

        if escolha == '34':
            expressao = input("Digite a expressão numérica: ")
            print("Resultado:", calcular(expressao))
        elif escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print("Resultado:", adicao(num1, num2))
            elif escolha == '2':
                print("Resultado:", subtracao(num1, num2))
            elif escolha == '3':
                print("Resultado:", multiplicacao(num1, num2))
            elif escolha == '4':
                print("Resultado:", divisao(num1, num2))
            elif escolha == '5':
                print("Resultado:", potenciacao(num1, num2))
        elif escolha in ['6', '20']:
            num = float(input("Digite o número: "))
            print("Resultado:", radiciacao(num))
        elif escolha == '7':
            num = float(input("Digite o número: "))
            percentual = float(input("Digite o percentual: "))
            print("Resultado:", porcentagem(num, percentual))
        elif escolha == '8':
            num = float(input("Digite o número: "))
            base = float(input("Digite a base: "))
            print("Resultado:", logaritmo(num, base))
        elif escolha == '9':
            num = int(input("Digite o número: "))
            print("Resultado:", fatorial(num))
        elif escolha == '10':
            num = float(input("Digite o número: "))
            print("Resultado:", valor_absoluto(num))
        elif escolha in ['11', '12', '13']:
            num = float(input("Digite o ângulo em graus: "))
            if escolha == '11':
                print("Resultado:", seno(math.radians(num)))
            elif escolha == '12':
                print("Resultado:", cosseno(math.radians(num)))
            elif escolha == '13':
                print("Resultado:", tangente(math.radians(num)))
        elif escolha == '14':
            num = float(input("Digite o número: "))
            print("Resultado:", arredondamento(num))
        elif escolha == '15':
            quantidade = int(input("Quantidade de números: "))
            lista = [float(input(f"Digite o {i+1}º número: ")) for i in range(quantidade)]
            print("Resultado:", media(lista))
        elif escolha == '16':
            quantidade = int(input("Quantidade de números: "))
            lista = [float(input(f"Digite o {i+1}º número: ")) for i in range(quantidade)]
            print("Resultado:", desvio_padrao(lista))
        elif escolha == '17':
            valor = float(input("Digite o valor: "))
            unidade_origem = input("Digite a unidade de origem: ")
            unidade_destino = input("Digite a unidade de destino: ")
            print("Resultado:", conversao_unidades(valor, unidade_origem, unidade_destino))
        elif escolha in ['18', '19']:
            capital = float(input("Digite o capital inicial: "))
            taxa = float(input("Digite a taxa de juros (em decimal): "))
            tempo = float(input("Digite o tempo (em anos): "))
            if escolha == '18':
                print("Resultado:", juros_simples(capital, taxa, tempo))
            elif escolha == '19':
                print("Resultado:", juros_compostos(capital, taxa, tempo))
        elif escolha == '21':
            num = float(input("Digite o número: "))
            print("Resultado:", exponencial(num))
        elif escolha == '22':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado:", modulo(num1, num2))
        elif escolha == '23':
            quantidade = int(input("Quantidade de valores: "))
            valores = [float(input(f"Digite o {i+1}º valor: ")) for i in range(quantidade)]
            pesos = [float(input(f"Digite o peso do {i+1}º valor: ")) for i in range(quantidade)]
            print("Resultado:", media_ponderada(valores, pesos))
        elif escolha == '24':
            expoente = float(input("Digite o expoente: "))
            print("Resultado:", potencia_de_10(expoente))
        elif escolha == '25':
            num = float(input("Digite o número: "))
            print("Resultado:", inverso(num))
        elif escolha == '26':
            print("Resultado:", numero_euler())
        elif escolha == '27':
            num = float(input("Digite o número: "))
            print("Resultado:", logaritmo_natural(num))
        elif escolha == '28':
            n = int(input("Digite o valor de n: "))
            k = int(input("Digite o valor de k: "))
            print("Resultado:", combinacao(n, k))
        elif escolha == '29':
            n = int(input("Digite o valor de n: "))
            k = int(input("Digite o valor de k: "))
            print("Resultado:", permutacao(n, k))
        elif escolha == '30':
            parte_real = float(input("Digite a parte real: "))
            parte_imaginaria = float(input("Digite a parte imaginária: "))
            complexo = complex(parte_real, parte_imaginaria)
            print("Resultado:", conjugado_complexo(complexo))
        elif escolha == '31':
            parte_real = float(input("Digite a parte real: "))
            parte_imaginaria = float(input("Digite a parte imaginária: "))
            complexo = complex(parte_real, parte_imaginaria)
            print("Resultado:", parte_imaginaria(complexo))
        elif escolha == '32':
            parte_real = float(input("Digite a parte real: "))
            parte_imaginaria = float(input("Digite a parte imaginária: "))
            complexo = complex(parte_real, parte_imaginaria)
            print("Resultado:", parte_real(complexo))
        elif escolha == '33':
            num = float(input("Digite o ângulo em graus: "))
            print("Resultado:", cotangente(math.radians(num)))
        else:
            print("Opção inválida")

calculadora()
