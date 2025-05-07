# CalcCientifica

# RF

1. Rodar as operações em looping até que o usuário encerre o programa (Código -1)
2. Todas as funções terão no máximo 2 operandos
3. 8 Espaços de memória para armazenar resultados - Iniciados em 0 e nomeados em M (M1, M2, M3, ...)
4. O último resultado deve ser armazenado em uma variável
5. Respostas em :.8f

# Regras de Negócio

1. **Não é permitido a importação de bibliotecas**
2. Apenas operações de _+ - \* /_
3. Apenas as estruturas de:
   - Entrada / Saída
   - Operações aritmédicas
   - Estruturas condicionais
   - Estruturas de repetição
   - Vetores

# Códigos de cada operação

- Soma - Cod 1
- Sub - Cod 2
- Mult - Cod 3
- Div - Cod 4
- Power - Cod 5
- Root - Cod 6 - Método de Newton
- Fat - Cod 7
- Ln - Cod 8
  - Traz x para perto de 1 usando identidade: ln(x) = ln(a^b) = b \* ln(a)
  - Aqui usamos mudança de base: x = a^k => ln(x) = k \* ln(a)
  - Então aproximamos ln(x) pela identidade: ln(x) = 2 _ [ (x-1)/(x+1) + 1/3_((x-1)/(x+1))^3 + 1/5\*((x-1)/(x+1))^5 + ... ]
- Log - Cod 9
  - Série de Taylor
- Seno - Cod 10
- Cosseno - Cod 11
- Tan - Cod 12
- ArcSen - Cod 13
- Arccos - Cod 14
- Arctan - Cod 15
- **STORE - Cod 16**
- **Clear - Cod 17**

- Exit - Cod -1

# Casos de teste

1. Números positivos
2. Números negativos
3. Números decimais
