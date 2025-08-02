"""Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”."""

import string

def palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


print(palindromo("Ana"))          
print(palindromo("python"))  
