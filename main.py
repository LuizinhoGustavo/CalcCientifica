# Operações

def soma(a, b):
    res = a + b
    print(f'O resultado é {res:.8f}')
    return res

def sub(a, b):
    res = a - b
    print(f'O resultado é {res:.8f}')
    return res

def mult(a, b):
    res = a * b
    print(f'O resultado é {res:.8f}')
    return res

def div(a, b):
    res = a / b
    print(f'O resultado é {res:.8f}')
    return res

def power(a, b):
    i = 1
    res = a
    while i < b:
        print(res)
        res *= a
        i += 1
    print(f'O resultado é {res:.8f}')
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

cod = ""

while(cod != '-1'):
    cod = input('Digite o código da operação que deseja realizar: ')
    
    if(cod != '-1'):
        a = float(input("Digite o valor do operante A: "))
        b = float(input("Digite o valor do operante B: "))
        
        if cod == "1":
            soma(a, b)
        elif cod == "2":
            sub(a, b)
        elif cod == "3":
            mult(a, b)
        elif cod == "4":
            div(a, b)
        elif cod == "5":
            power(a, b)