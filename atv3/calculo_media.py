"""Calculadora da Média


Faça um programa que leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 

Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

 No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). 

Para estes dois casos
(aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media
final: " seguido da média final para esse aluno.


Entrada: A entrada contém quatro números de ponto flutuante correspondentes às notas dos alunos.

"""
num1 = float(input(" Digite a seguir as 4 notas para verificação\n Nota 1: "))
num2 = float(input(" \n Nota 2: "))
num3 = float(input(" \n Nota 3: "))
num4 = float(input(" \n Nota 4: "))
media = (num1 + num2 + num3 + num4)/4
if media >= 7.0:
    print(f"Aluno Aprovado!\n Média final: {media: .1f}")
elif media < 5.0:
    print(f"Aluno Reprovado!\n Média final: {media: .1f}")
else:
    print("Aluno em exame\n ")
    nota_exame = float(input("Digite a nota do exame:  "))
    media_final = (media + nota_exame)/2
    print(f"Nota do exame: {nota_exame} ")
    if media_final >= 7.0:
        print(f"Aluno Aprovado!\n Média final: {media_final: .1f}")
    elif media_final < 5.0:
        print(f"Aluno Reprovado!\n Média final: {media_final: .1f}")