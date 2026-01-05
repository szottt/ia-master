import requests
import sqlite3
from bs4 import BeautifulSoup

url = "https://www.idealsoftwares.com.br/indices/ipca_ibge.html"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

# Busca a primeira tabela da página
table = soup.find('table')
if not table:
    raise Exception("Tabela não encontrada na página.")

ipca_data = []
for row in table.find_all('tr')[1:]:  # pula o cabeçalho
    cols = [td.text.strip() for td in row.find_all('td')]
    if len(cols) >= 4:
        data, valor, ano, mes = cols[:4]
        try:
            valor_float = float(valor.replace(',', '.'))
            ano_int = int(ano)
            mes_int = int(mes)
            ipca_data.append((valor_float, mes_int, ano_int))
        except ValueError:
            continue  # pula linhas com dados inválidos

conn = sqlite3.connect('ipca.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS IPCA (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        VALUE REAL,
        MONTH INTEGER,
        YEAR INTEGER,
        UNIQUE(MONTH, YEAR)
    )
''')

for value, month, year in ipca_data:
    cursor.execute(
        'INSERT OR IGNORE INTO IPCA (VALUE, MONTH, YEAR) VALUES (?, ?, ?)',
        (value, month, year)
    )

conn.commit()
cursor.close()
conn.close()
print('Dados Históricos do IPCA salvos com sucesso!')