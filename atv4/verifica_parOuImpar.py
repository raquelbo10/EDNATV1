"""Crie um programa que solicite ao usuário que insira números inteiros. 
O programa deve continuar solicitando números até que o usuário digite 'fim'.
 Para cada número inserido, o programa deve informar se é par ou ímpar.
 Se o usuário inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos."""

pares = 0
impares = 0

print("Verificador de Par ou Ímpar")
print("Digite números inteiros. Digite 'fim' para encerrar.\n")

while True:
    entrada = input("Digite um número inteiro ou 'fim': ").strip().lower()

    if entrada == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("\n Resultado final:")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")