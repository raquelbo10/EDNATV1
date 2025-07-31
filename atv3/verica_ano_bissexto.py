"""Verificador de Ano Bissexto


Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

"""

ano = int(input("Forneça um ano para saber se ele é Bissexto: "))
if ano%4 == 0 and ano%100 != 0:
    print(f"O ano {ano} é Bissexto!")
else:
     print(f"O ano {ano} NÃO é Bissexto!")