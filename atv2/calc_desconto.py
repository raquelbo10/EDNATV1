"""Calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""
nome_prod = "camiseta"
preco_original = 50.00
desconto = 0.2
valor_desconto = preco_original*desconto 
preco_final = preco_original - valor_desconto
print(f"Produto: {nome_prod}\n Preço: {preco_original}\n Preço com desconto aplicado: {preco_final: .2f}\n Você economizou R${valor_desconto}!")