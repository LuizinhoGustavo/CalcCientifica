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
    res = a / b

    return res

def power(a, b):
    if (b == 0):
        return 1
    i = 1
    res = a
    while i < b:
        print(res)
        res *= a
        i += 1

    return res

def root(a, b):
    i = 100
    if b == 0:
        return 0
    if b < 0 and a % 2 == 0:
        raise ValueError("Não é possível calcular raiz par de número negativo.")

    x = b / a 
    for _ in range(i):
        x_pot = 1
        for _ in range(int(a) - 1):
            x_pot *= x

        res = ((a - 1) * x + b / x_pot) / a
        x = res 

    return res

def fat(a):
    if a == 0:
        return 1
    res = 1
    i = 1
    while i <= a:
        res *= i
        i += 1
    
    return res

def ln(a):
    i = 50
    if a <= 0:
        raise ValueError("x deve ser maior que 0")
    
    y = (a - 1) / (a + 1)
    y2 = y * y
    res = 0

    for n in range(i):
        b = (1 / (2 * n + 1)) * (y ** (2 * n + 1))
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

print(  
      "-------------------------------------------------------------\n"
      "|  CALCULADORA MUITO FODA DO PROFESSOR MATEUS COELHO 💋 <3  |\n"
      "|                    Códigos da operações                   |\n"
      "-------------------------------------------------------------\n\n"
      "Cod 1 - Soma     | Cod 2 - Sub\n"
      "Cod 3 - Mult     | Cod 4 - Div\n"
      "Cod 5 - Power    | Cod 6 - Root\n"
      "Cod 7 - Fat      | Cod 8 - Ln\n"
      "Cod 9 - Log      | Cod 10 - Seno\n"
      "Cod 11 - Cosseno | Cod 12 - Tan\n"
      "Cod 13 - ArcSen  | Cod 14 - Arccos\n"
      "Cod 15 - Arctan  |\n"
      "\n"
      "Cod 16 - STORE   | Cod 17 - Clear\n"
      "Cod -1 - Exit \n")

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
            res = soma(a, b)
            print(f'O resultado é {res:.8f}')

        elif cod == "2":
            res = sub(a, b)
            print(f'O resultado é {res:.8f}')

        elif cod == "3":
            res = mult(a, b)
            print(f'O resultado é {res:.8f}')

        elif cod == "4":
            res = div(a, b)
            print(f'O resultado é {res:.8f}')

        elif cod == "5":
            res = power(a, b)
            print(f'O resultado é {res:.8f}')

        elif cod == "6":
            res = root(a, b)
            print(f'O resultado é {res:.8f}')

        elif cod == "7":
            res = fat(a)
            print(f'O resultado é {res:.8f}')

        elif cod == "8":
            res = ln(a)
            print(f'O resultado é {res:.8f}')

        elif cod == "9":
            res = log(a, b)
            print(f'O resultado é {res:.8f}')

        # elif cod == "10":
        # elif cod == "11":
        # elif cod == "12":
        # elif cod == "13":
        # elif cod == "14":
        # elif cod == "15":
        # elif cod == "16":
        # elif cod == "17":