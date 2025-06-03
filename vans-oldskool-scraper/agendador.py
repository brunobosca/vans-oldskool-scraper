import schedule
import time
from src.scraper import coletar_dados, salvar_dados

def tarefa_diaria():
    url = 'https://www.mercadolivre.com.br/tnis-vans-old-skool-color-pretobranco-adulto-40-br/p/MLB22456175'
    dados = coletar_dados(url)
    salvar_dados(dados)
    print("Coleta realizada com sucesso", dados)
    

# Agendar para executar diariamente às 09:00
schedule.every().day.at("14:23").do(tarefa_diaria)

while True:
    schedule.run_pending()
    time.sleep(60)

# Rodar manualmente para teste
# tarefa_diaria()
    



