"""Crie um programa que permita a um professor registrar as notas de uma turma. 
O programa deve continuar solicitando notas até que o professor digite 'fim'. 
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.

"""
notas = []

print("Registro de notas da turma")
print("Digite as notas dos alunos (entre 0 e 10). Digite 'fim' para encerrar.\n")

while True:
    entrada = input("Digite a nota ou 'fim': ").lower()

    if entrada == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")


if notas:
    media = sum(notas) / len(notas)
    print(f"\n Média da turma: {media:.2f}")
else:
    print("\n Nenhuma nota válida foi registrada.")