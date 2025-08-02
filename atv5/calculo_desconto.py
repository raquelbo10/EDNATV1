"""Crie um programa que receba o preço original de um produto e um percentual de desconto, 
realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. 
Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10)."""

def calcula_preco_final():
    try:
        
        preco_original = float(input("Informe o preço original do produto: R$ "))
        percentual_desconto = float(input("Informe o percentual de desconto (%): "))

        
        valor_desconto = preco_original * (percentual_desconto / 100)

        preco_final = preco_original - valor_desconto

        print(f"\n Valor do desconto: R$ {valor_desconto:.2f}")
        print(f" Preço final com desconto: R$ {preco_final:.2f}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")

calcula_preco_final()