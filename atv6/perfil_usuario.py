"""Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
 O programa deve exibir o nome, email e país do usuário gerado."""
import urllib.request
import json

def gerar_usuario():
    url = "https://randomuser.me/api/"

    try:
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read().decode())

            usuario = dados['results'][0]
            nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']

            print("=== Perfil Gerado ===")
            print(f"Nome : {nome_completo}")
            print(f"E-mail: {email}")
            print(f"País : {pais}")

    except Exception as erro:
        print(f"Erro ao acessar a API: {erro}")

if __name__ == "__main__":
    gerar_usuario()
