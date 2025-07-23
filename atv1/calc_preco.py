"""Calculadora de Preço Total
Desenvolva um programa que calcule o preço total de uma compra. 
Use as seguintes informações:
Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""
nome_prod = "Cadeira infantil"
preco = 12.40
qtde = 3
total = qtde*preco

print(f"# Compra realizada # \n Produto: {nome_prod} \n Preço unitário: R${preco} \n Quantidade: {qtde} \n Valor total: R${total}")