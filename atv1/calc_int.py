""" Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. A seguir, 
calcule e mostre a diferença do produto de A e B pelo produto de C e D 
segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas."""

print("Vamos começar! Vou te pedir para digitar 4 números inteiros!")
A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))
D = int(input("Digite o quarto número: "))

diferenca = (A*B - C*D)
print( f"DIFERENÇA = {diferenca}")