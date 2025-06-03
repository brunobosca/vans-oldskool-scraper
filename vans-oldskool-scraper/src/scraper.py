import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def coletar_dados(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extração dos dados
    nome = soup.find('h1', {'class': 'ui-pdp-title'}).get_text(strip=True)
    preco = soup.find('span', {'class': 'andes-money-amount__fraction'}).get_text(strip=True)
    disponibilidade = 'Disponível' if soup.find('span', {'class': 'ui-pdp-buybox__quantity__available'}) else 'Indisponível'

    # Dados coletados
    dados = {
        'data_coleta': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'nome': nome,
        'preco': preco,
        'disponibilidade': disponibilidade
    }

    return dados

def salvar_dados(dados, caminho_arquivo='data/historico_precos.csv'):
    campo_nomes = ['data_coleta', 'nome', 'preco', 'disponibilidade']
    try:
        with open(caminho_arquivo, 'x', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=campo_nomes)
            writer.writeheader()
            writer.writerow(dados)
    except FileExistsError:
        with open(caminho_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=campo_nomes)
            writer.writerow(dados)
