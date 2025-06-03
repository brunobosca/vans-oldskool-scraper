# 🛍️ Monitoramento de Preços - Tênis Vans Old Skool no Mercado Livre

Projeto de **web scraping** em Python que coleta diariamente o preço e disponibilidade do **Tênis Vans Old Skool** em uma página específica do [Mercado Livre](https://www.mercadolivre.com.br/tnis-vans-old-skool-color-pretobranco-adulto-40-br/p/MLB22456175). Os dados são armazenados em CSV e podem ser usados para análise da evolução de preços ao longo do tempo.

---

## 🎯 Objetivo

Demonstrar como utilizar Python, requests e BeautifulSoup para:

- Extrair informações de uma página web real.
- Armazenar os dados de forma organizada.
- Automatizar a coleta diária.
- Analisar variações de preço com gráficos.

---

## 📦 Tecnologias Utilizadas

- Python 3.x
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Schedule](https://pypi.org/project/schedule/)
- Pandas & Matplotlib (opcional para análise)

---

## 📁 Estrutura do Projeto

```bash
vans-oldskool-scraper/
├── data/
│   └── historico_precos.csv        # Onde os dados coletados são salvos
├── src/
│   └── scraper.py                  # Contém funções de coleta e salvamento
├── agendador.py                    # Script para rodar a coleta (manual ou agendada)
├── requirements.txt                # Bibliotecas necessárias
├── README.md                       # Este arquivo
