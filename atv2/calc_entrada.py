"""Calculadora de Soma com Entrada do Usuário

Leia 2 valores inteiros e armazene-os nas variáveis A e B. 

Efetue a soma de A e B, atribuindo o seu resultado à variável X. 

Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.

"""
print("Digite um número para somar:")
A = int(input())
print("Digite outro número para somar:")
B = int(input())
X = A + B
print(f"X = {X} \n****************************")
