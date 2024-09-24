def contar_as(texto: str) -> int:
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
frase = input("Digite uma frase: ")
# Chama a função e imprime o resultado
quantidade_as = contar_as(frase)
print(f"A letra 'a' aparece {quantidade_as} vezes na frase.")
