"""Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

temp = float(input("Digite a temperatura que deseja converter: "))
origem = int(input("Qual a unidade de origem?\n 1-Celsius\n 2-Kelvin\n 3-Farenheit\n"))
destino = int(input("Para qual a unidade deseja converter?\n 1-Celsius\n 2-Kelvin\n 3-Farenheit\n"))

if origem == 1 :
    if destino == 2:
        celsius_kelvin = temp + 273.15
        print(f"{temp} em Kelvin corresponde a: {celsius_kelvin: .2f}")
    elif  destino == 3:
        celsius_fahrenheit = (temp * 9/5) + 32
        print(f"{temp} em Fahrenheit corresponde a: {celsius_fahrenheit: .2f} ")
elif origem == 2 :
    if destino == 2:
        kelvin_celsius = temp - 273.15
        print(f"{temp} em Celsius corresponde a: {kelvin_celsius: .1f}")
    elif  destino == 3:
        kelvin_fahrenheit = (temp - 273.15) * 9/5 + 32
        print(f"{temp} em Fahrenheit corresponde a: {kelvin_fahrenheit: .2f} ")
elif origem == 3 :
    if destino == 1:
        fahrenheit_celsius = (temp - 32) * 5/9
        print(f"{temp} em Celsius corresponde a: {fahrenheit_celsius: .2f}")
    elif  destino == 3:
        fahrenheit_kelvin = (temp - 32) * 5/9 + 273.15
        print(f"{temp} em Kelvin corresponde a: {fahrenheit_kelvin: .2f}")
