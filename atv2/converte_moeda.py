"""- Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
tax_dolar = 5.60
tax_euro = 6.60
valor_real = 100.00

print(f"100 reais convertidos em dólar equivale a:{(valor_real/tax_dolar): .2f} dólares.")
print(f"100 reais convertidos em euro equivale a:{(valor_real/tax_euro): .2f} euros.")