# Desafio 1

def pertence_fibonacci(num):
    """Verifica se um número pertence à sequência de Fibonacci.

    Args:
      num: O número a ser verificado.

    Returns:
      True se o número pertence à sequência, False caso contrário.
    """

    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num


# Solicita o número ao usuário
numero = int(input("Digite um número: "))

# Verifica se o número pertence à sequência e imprime o resultado
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


# Desafio 2

def contar_as(texto):
    """Conta o número de ocorrências da letra 'a' (maiúscula ou minúscula) em uma string.

    Args:
      texto: A string a ser analisada.

    Returns:
      O número de ocorrências da letra 'a'.
    """

    # Converte toda a string para minúsculas para facilitar a contagem
    texto_minusculo = texto.lower()

    # Conta o número de ocorrências da letra 'a'
    contagem = texto_minusculo.count('a')

    return contagem


# Solicita a entrada do usuário
# texto = input("Digite uma frase: ")
#
# # Chama a função e imprime o resultado
# quantidade_as = contar_as(texto)
# print(f"A letra 'a' aparece {quantidade_as} vezes na frase.")

# Desafio 3


def main():
    indice = 12
    soma = 0
    k = 1
    while k < indice:
        k += 1
        soma += k
    print(f"SOMA = {soma}")


main()
# soma = 77

# Desafio 4

""""
    
    a) P(A) 
       r = 3 - 1 = 2
       resposta:
        1, 3, 5, 7, 9
    
    b) P(G) 
       q = 4 / 2 = 2
       resposta:
        2, 4, 8, 16, 32, 64 
        
    c) Cada número da sequência é o quadrado da sua posição. 
    
    Ex:
    
      Lista:   [0, 1, 4, 9, 16, 25, 36, 49]
      Indice:   0² 1² 2² 3² 4²  5²  6², 7²
            
    
    d)
       o quadrado de cada valor par:
        lista = [4, 16, 36, 64, 100]
        par =    2² 4²  6²  8²  10²
    
    e)
        Sequência fibonacci
            [1, 1, 2, 3, 5, 8, 13]
            
    f)
        Todos eles começam com a letra D
        Dois, Dez, Doze, ....
        Portanto 200 será o próximo número
        
        2, 10, 12, 16, 17, 18, 19, 200 
        
        
5) 
    Acende um interruptor e mantenha-o assim por alguns minutos. Desligue-o e acenda outro. Na sala das lâmpadas, a lâmpada acesa é controlada pelo último interruptor ligado, a morna pelo primeiro e a fria pelo terceiro.
"""
