"""Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de combustível 
 de um veículo. Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) e 
exibir todos os dados da viagem, incluindo o resultado final 
arredondado para duas casas decimais.

"""
distancia = 300
combustivel_gasto = 25
consumo_medio = distancia/combustivel_gasto

print(f" Distância percorrida: {distancia}km\n Combustível gasto: {combustivel_gasto}l\n Consumo médio: {consumo_medio: .2f}km/l")