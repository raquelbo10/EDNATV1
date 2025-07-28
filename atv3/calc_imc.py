"""Calculadora de IMC


Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"""

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/altura**2
if  imc < 18.5 :
    print("Você está abaixo do peso ideal!") 
elif imc >= 18.5  and imc < 25 :
    print("Você está com o peso normal!")
elif imc >= 25 and imc < 30 :
    print("Você está com sobrepeso!")
else:
    print("Você está obeso!")