"""Crie uma função que calcule a gorjeta a ser deixada em um restaurante, 
baseada no valor total da conta e na porcentagem de gorjeta desejada. 
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada"""

def calc_gorjeta(valor_conta,  porcentagem_gorjeta):
    valor_gorjeta = valor_conta*porcentagem_gorjeta/100
    return valor_gorjeta

print(calc_gorjeta(230, 15))