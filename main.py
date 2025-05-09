#Funções auxiliares
def exp(x):
    j=20
    res = 1
    termo = 1
    for i in range(1, termos):
        termo *= x / i
        res += j
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
        return "Indeterminado - divisor igual a 0"
    
    if (a == 0 and b == 0):
        return "Indeterminado - divisor e dividendo igual a 0"
    
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
        return "Indeterminado - Base negativa com expoente fracionário não suportada"

def root(a, b):
    if int(a) != a or a == 0:
        return "indeterminado - Índice da raiz deve ser um inteiro diferente de zero"

    negativo = False
    if a < 0:
        negativo = True
        a = -a

    a = int(a)

    if b < 0 and a % 2 == 0:
        return "indeterminado - Não existe raiz real de número negativo com índice par"

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
        return "Indeterminado - Fatorial só é definido para inteiros não negativos"

    if isinstance(a, float) and not a.is_integer():
        return "Indeterminado - Fatorial só é definido para inteiros não negativos"

    if a > 170:
        return "Número muito grande para calcular o fatorial com precisão"

    a = int(a)
    res = 1
    for i in range(1, a + 1):
        res *= i
    
    return res


def ln(a):
    i = 50
    if a <= 0:
        return "x deve ser maior que 0"
    
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
        return "Indetermiando - a deve ser > 0 e b deve ser > 0 e diferente de 1"
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
        return "Indetermiando - Tangente indefinida (cosseno igual a zero)"
    
    sen = seno(x)
    res = sen / cos

    return res

def arcSen(x):

    if x < -1 or x > 1:
        return "Indetermiando - O domínio de arcsen é entre -1 e 1."

    termos = 100
    res = 0
    for n in range(termos):
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
        return "Indetermiando - O domínio de arccos é entre -1 e 1."
    
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
    "║ 18     │ Visualizar             │                         ║\n"   "╠═══════════════════════════════════════════════════════════╣\n"
    "║ Código -1: Sair                                           ║\n"
    "╚═══════════════════════════════════════════════════════════╝\n"
)

# Variáveis
cod = ""
operacoesComUmOperante = ['7', '8', '10', '11', '12', '13', '14', '15']
operacoesEspeciais = ['16', '17', '18']

armazenamento = [0, 0, 0, 0, 0, 0, 0, 0]
ans = 0

while(cod != '-1'):
    cod = input('\nDigite o código da operação que deseja realizar: ')
    
    if(cod != '-1'):
        if (int(cod) in range(1, 19)):
            if (cod not in operacoesEspeciais):
                a = input("Digite o valor do operante A: ")
                if (a[0] == "M"):
                    a = armazenamento[int(a[1]) - 1]
                else:
                    a = float(a)

                if(cod not in operacoesComUmOperante):
                    b = input("Digite o valor do operante B: ")
                    if (b[0] == "M"):
                        b = armazenamento[int(b[1]) - 1]
                    else:
                        b = float(b)
        
            if cod == "1":
                ans = soma(a, b)

            elif cod == "2":
                ans = sub(a, b)

            elif cod == "3":
                ans = mult(a, b)

            elif cod == "4":
                ans = div(a, b)

            elif cod == "5":
                ans = power(a, b)

            elif cod == "6":
                ans = root(a, b)

            elif cod == "7":
                ans = fat(a)

            elif cod == "8":
                ans = ln(a)

            elif cod == "9":
                ans = log(a, b)

            elif cod == "10":
                ans = seno(a)
            
            elif cod == "11":
                ans = cosseno(a)

            elif cod == "12":
                ans = tan(a)

            elif cod == "13":
                ans = arcSen(a)
                
            elif cod == "14":
                ans = arcCos(a)

            elif cod == "15":
                ans = arcTan(a)

            elif cod == "16":
                posicao = int(input(f"Qual posição deseja armazenar a última resposta ({ans:.8f}): "))

                if (posicao < 1 or posicao > 8):
                    print(f"A posição {posicao} é inválida, escolha um espaço de 1 à 8")
                else:
                    posicao -= 1
                    armazenamento[posicao] = ans
                    print(f"A resposta {ans:.8f} foi armazenada na posição M{posicao + 1}")

            elif cod == "17":
                posicao = int(input(f"Qual posição deseja limpar do armazenamento:"))
                posicao -= 1
                armazenamento[posicao] = 0

            elif cod == "18":
                print(f"Armazenamento: {armazenamento}")

            if(cod not in operacoesEspeciais):
                if isinstance(ans, str):
                        print(ans)
                else:
                    print(f'O resultado é {ans:.8f}')
        else:
            print("Digite um código válido.")
            

        

print("Até a próxima 🤓☝️")
