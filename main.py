#Funções auxiliares
def exp(x, termos=20):
    res = 1
    termo = 1
    for i in range(1, termos):
        termo *= x / i
        res += termo
    return res


# Operações

def soma(a, b):
    res = a + b

    return res

def sub(a, b):
    res = a - b
    
    return res

def mult(a, b):
    res = a * b

    return res

def div(a, b):
    if (b == 0):
        return "Resultado indeterminado"
    
    if (a == 0 and b == 0):
        return "Resultado indeterminado"
    
    res = a / b

    return res

def power(a, b):
    if b == 0:
        return 1
    elif int(b) == b and b > 0:  # Expoente inteiro positivo
        res = 1
        for _ in range(int(b)):
            res *= a
        return res
    elif int(b) == b and b < 0:  # Expoente inteiro negativo
        res = 1
        for _ in range(-int(b)):
            res *= a
        return 1 / res
    elif a > 0:  # Expoente real (ex: 2^0.5)
        return exp(b * ln(a))
    else:
        raise ValueError("Base negativa com expoente fracionário não suportada")

def root(a, b):
    if int(a) != a or a == 0:
        raise ValueError("Índice da raiz deve ser um inteiro diferente de zero")

    negativo = False
    if a < 0:
        negativo = True
        a = -a  # equivalente a abs(a), mas sem usar a função

    a = int(a)

    if b < 0 and a % 2 == 0:
        raise ValueError("Não existe raiz real de número negativo com índice par")

    if b == 0:
        return 0

    # Aproximação via Newton-Raphson
    iteracoes = 100
    x = b / a  # chute inicial

    for _ in range(iteracoes):
        x_pot = 1
        for _ in range(a - 1):
            x_pot *= x

        res = ((a - 1) * x + b / x_pot) / a
        x = res

    return 1 / res if negativo else res

def fat(a):
    if a == 0:
        return 1
    
    if a < 0:
        raise ValueError("Não existe fatorial de número negativo")

    if isinstance(a, float) and not a.is_integer():
        raise ValueError("Fatorial só é definido para inteiros não negativos")

    if a > 170:
        raise OverflowError("Número muito grande para calcular o fatorial com precisão")

    a = int(a)
    res = 1
    for i in range(1, a + 1):
        res *= i
    
    return res


def ln(a):
    i = 50
    if a <= 0:
        raise ValueError("x deve ser maior que 0")
    
    y = (a - 1) / (a + 1)
    res = 0

    for n in range(i):
        exp = 2 * n + 1
        b = (1 / exp) * power(y, exp)
        res += b

    res *= 2

    return res
 

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("a deve ser > 0 e b deve ser > 0 e diferente de 1")
    ln_a = ln(a)
    ln_b = ln(b)
    res = ln_a / ln_b

    return res

def seno(x):
    # Converter graus para radianos
    pi = 3.14159265359
    x = (x * pi) / 180

    # Normalizar o valor de x entre -2π e 2π para melhor precisão
    while x > 2 * pi:
        x -= 2 * pi
    while x < -2 * pi:
        x += 2 * pi

    termos = 10  # Quantidade de termos da série de Taylor
    resultado = 0

    for n in range(termos):
        sinal = -1 if n % 2 else 1
        numerador = power(x, 2 * n + 1)
        denominador = fat(2 * n + 1)
        resultado += sinal * numerador / denominador

    return resultado

def cosseno(x):

    x = (x * 3.14159265359) / 180

    # Normaliza o valor de x entre -2π e 2π
    while x > 6.28318530718:  # 2 * pi
        x -= 6.28318530718
    while x < -6.28318530718:
        x += 6.28318530718

    termos = 10  # Quantidade de termos da série de Taylor
    res = 0

    for n in range(termos):
        sinal = -1 if n % 2 else 1
        numerador = x ** (2 * n)
        denominador = fat(2 * n)
        res += sinal * numerador / denominador

    return res

def tan(x):
    cos = cosseno(x)
    if cosseno == 0:
        raise ValueError("Tangente indefinida (cosseno igual a zero)")
    
    sen = seno(x)
    res = sen / cos

    return res

def arcSen(x):

    if x < -1 or x > 1:
        raise ValueError("O domínio de arcsen é entre -1 e 1.")

    termos = 100
    res = 0
    for n in range(termos):
        # Cálculo do numerador: fatorial(2n)
        num = fat(2 * n)

        # Cálculo do denominador: (4^n) * (n!)^2 * (2n + 1)
        pot_4 = 1
        for _ in range(n):
            pot_4 *= 4
        
        fat_n = fat(n)
        den = pot_4 * fat_n * fat_n * (2 * n + 1)

        # x^(2n + 1)
        pot_x = 1
        for _ in range(2 * n + 1):
            pot_x *= x

        res += (num * pot_x) / den

    res = (res * 180) / 3.14159265359

    return res

def arcCos(x):      
    if x < -1 or x > 1:
        raise ValueError("O domínio de arccos é entre -1 e 1.")
    
    res = 90 - arcSen(x)

    return res

def arcTan(x):
    termos = 20  # mais termos para melhor precisão

    if x > 1:
        return 90 - arcTan(1 / x)
    elif x < -1:
        return -90 - arcTan(1 / x)

    res = 0
    for n in range(termos):
        sinal = -1 if n % 2 else 1
        pot_x = 1
        for _ in range(2 * n + 1):
            pot_x *= x

        res += sinal * pot_x / (2 * n + 1)

    # Converter radianos para graus
    res = (res * 180) / 3.14159265359
    return res

print(
    "╔═══════════════════════════════════════════════════════════╗\n"
    "║           CALCULADORA CIENTÍFICA - UFABC - PI 💋 <3       ║\n"
    "║                     CÓDIGOS DAS OPERAÇÕES                 ║\n"
    "╠═══════════════════════════════════════════════════════════╣\n"
    "║ Código | Operação               │ Código | Operação       ║\n"
    "╠════════╪════════════════════════╪════════╪════════════════╣\n"
    "║ 1      │ Soma                   │ 2      │ Subtração      ║\n"
    "║ 3      │ Multiplicação          │ 4      │ Divisão        ║\n"
    "║ 5      │ Potência               │ 6      │ Raiz           ║\n"
    "║ 7      │ Fatorial               │ 8      │ Log. Natural   ║\n"
    "║ 9      │ Logaritmo              │ 10     │ Seno           ║\n"
    "║ 11     │ Cosseno                │ 12     │ Tangente       ║\n"
    "║ 13     │ Arcoseno               │ 14     │ Arcocosseno    ║\n"
    "║ 15     │ Arcotangente           │        │                ║\n"
    "╠═══════════════════════════════════════════════════════════╣\n"
    "║ 16     │ Armazenar              │ 17     │ Limpar         ║\n"
    "╠═══════════════════════════════════════════════════════════╣\n"
    "║ Código -1: Sair                                           ║\n"
    "╚═══════════════════════════════════════════════════════════╝\n"
)


# Variáveis
cod = ""
operacoesComUmOperante = ['7', '8', '10', '11', '12', '13', '14', '15']

while(cod != '-1'):
    cod = input('Digite o código da operação que deseja realizar: ')
    
    if(cod != '-1'):
        a = float(input("Digite o valor do operante A: "))
        if(cod not in operacoesComUmOperante):
            b = float(input("Digite o valor do operante B: "))
        
        if cod == "1":
            print("Soma")
            ans = soma(a, b)
            print(f'O resultado é {ans:.8f}')

        elif cod == "2":
            print("Subtração")
            ans = sub(a, b)
            print(f'O resultado é {ans:.8f}')

        elif cod == "3":
            print("Multiplicação")
            ans = mult(a, b)
            print(f'O resultado é {ans:.8f}')

        elif cod == "4":
            print("Divisão")
            ans = div(a, b)
            print(f'O resultado é {ans:.8f}')

        elif cod == "5":
            print("Potência")
            ans = power(a, b)
            print(f'O resultado é {ans:.8f}')

        elif cod == "6":
            print("Raiz")
            ans = root(a, b)
            print(f'O resultado é {ans:.8f}')

        elif cod == "7":
            print("Fatorial")
            ans = fat(a)
            print(f'O resultado é {ans:.8f}')

        elif cod == "8":
            print("Logaritmo Natural")
            ans = ln(a)
            print(f'O resultado é {ans:.8f}')

        elif cod == "9":
            print("Logaritmo")
            ans = log(a, b)
            print(f'O resultado é {ans:.8f}')

        elif cod == "10":
            print("Seno")
            ans = seno(a)
            print(f'O resultado é {ans:.8f}')
        
        elif cod == "11":
            print("Cosseno")
            ans = cosseno(a)
            print(f'O resultado é {ans:.8f}')

        elif cod == "12":
            print("Tangente")
            ans = tan(a)
            print(f'O resultado é {ans:.8f}')

        elif cod == "13":
            print("Arcoseno")
            ans = arcSen(a)
            print(f'O resultado é {ans:.8f}')
            
        elif cod == "14":
            print("Arccoseno")
            ans = arcCos(a)
            print(f'O resultado é {ans:.8f}')

        elif cod == "15":
            print("Arctangente")
            ans = arcTan(a)
            print(f'O resultado é {ans:.8f}')
            
        # elif cod == "16":
        # elif cod == "17":

print("Até a próxima 🤓☝️")
