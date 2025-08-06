"""Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual,
 máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""
import urllib.request
import json
from datetime import datetime

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read().decode())
            chave = f"{moeda}BRL"

            if chave not in dados:
                print("Moeda não encontrada.")
                return

            cotacao = dados[chave]

            valor_atual = cotacao['bid']
            valor_minimo = cotacao['low']
            valor_maximo = cotacao['high']
            timestamp = int(cotacao['timestamp'])
            data_hora = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

            print(f"\n=== Cotação {moeda} para BRL ===")
            print(f"Valor atual: R$ {valor_atual}")
            print(f"Valor mínimo: R$ {valor_minimo}")
            print(f"Valor máximo: R$ {valor_maximo}")
            print(f"Última atualização: {data_hora}")

    except Exception as erro:
        print(f"Erro ao consultar a cotação: {erro}")

def main():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip()
    if moeda:
        consultar_cotacao(moeda)
    else:
        print("Código da moeda não pode estar vazio.")

if __name__ == "__main__":
    main()
