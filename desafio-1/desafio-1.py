def is_fibonacci(num):
    # Função para verificar se um número é quadrado perfeito
    def is_perfect_square(x):
        return int(x**0.5)**2 == x

    # Um número é Fibonacci se e somente se um dos dois valores abaixo for um quadrado perfeito:
    # 5*n*n + 4 ou 5*n*n - 4 (Teorema de Binet)
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

# Número a ser verificado
numero = int(input("Informe um número: "))

# Verifica se o número está na sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
