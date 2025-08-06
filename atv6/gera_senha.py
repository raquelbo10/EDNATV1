"""Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, 
possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória."""
import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres: letras, dígitos e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Informe a quantidade de caracteres da senha: "))
        if tamanho <= 0:
            print("Por favor, informe um número maior que zero.")
        else:
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")
    except ValueError:
        print("Digite um número inteiro válido.")

if __name__ == "__main__":
    main()
