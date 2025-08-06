"""Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado."""
import urllib.request
import json

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read().decode())

            if "erro" in dados:
                print("CEP não encontrado.")
                return

            logradouro = dados.get("logradouro", "N/A")
            bairro = dados.get("bairro", "N/A")
            cidade = dados.get("localidade", "N/A")
            estado = dados.get("uf", "N/A")

            print("=== Endereço Encontrado ===")
            print(f"Logradouro: {logradouro}")
            print(f"Bairro    : {bairro}")
            print(f"Cidade    : {cidade}")
            print(f"Estado    : {estado}")

    except Exception as erro:
        print(f"Erro ao consultar o CEP: {erro}")

def main():
    cep = input("Digite o CEP (apenas números): ").strip()
    if len(cep) == 8 and cep.isdigit():
        consultar_cep(cep)
    else:
        print("CEP inválido. Deve conter 8 dígitos numéricos.")

if __name__ == "__main__":
    main()
