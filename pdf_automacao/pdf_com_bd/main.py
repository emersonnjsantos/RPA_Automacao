"""

from tabula.io import read_pdf

# Certifique-se de que o caminho do arquivo está correto
file_path = "seu_arquivo.pdf"

# Ajuste os parâmetros conforme necessário
df = read_pdf(file_path, pages='all', multiple_tables=True)

# Verifique se a lista não está vazia antes de acessar
if df:
    objTable = df[0]
    print(objTable)
else:
    print("Nenhuma tabela encontrada.")

    """


"""
from tabula import read_pdf
objTable = read_pdf("Stock Prices.pdf",pages="all") 
df = objTable[0]
df.to_excel("Stock Prices.xlsx",index=None)

"""


"""
 Alternativa 100% Python (sem Java): Usar pdfplumber
Se você quer algo mais simples, mais “Python puro” e sem Java, te recomendo essa abordagem:

pip install pdfplumber pandas openpyxl

E o código seria algo assim:

"""


"""
import pdfplumber
import pandas as pd

# Abrir o PDF e extrair o texto da primeira página
with pdfplumber.open("Stock Prices.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

# Separar as linhas do texto
lines = text.split('\n')

# Procurar a linha com os nomes dos meses
for i, line in enumerate(lines):
    if "Stocks" in line and "Jan" in line:
        header_line = line
        data_lines = lines[i+1:]  # as próximas linhas são os dados
        break

# Montar os cabeçalhos
columns = header_line.split()
# Corrigir se a palavra "Stocks" estiver separada
if columns[0].lower() != "stocks":
    columns = ["Stocks"] + columns

# Preparar os dados
data = []
for line in data_lines:
    parts = line.split()
    stock_name = parts[0]
    values = list(map(int, parts[1:]))
    row = [stock_name] + values
    data.append(row)

# Criar o DataFrame
df = pd.DataFrame(data, columns=columns)

# Exportar para Excel
df.to_excel("Stock Prices.xlsx", index=False)

print("✅ Excel gerado com sucesso!")

"""


"""
Aqui está o script completo que usa o seu código base com pdfplumber, e adiciona exportações para:

📄 Excel (.xlsx)

📊 CSV (.csv)

🧾 JSON (.json)

🗄️ Banco de dados SQLite (.db)

"""




import pdfplumber
import pandas as pd
import sqlite3

# Abrir o PDF e extrair o texto da primeira página
with pdfplumber.open("Stock Prices.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

# Separar as linhas do texto
lines = text.split('\n')

# Procurar a linha com os nomes dos meses
for i, line in enumerate(lines):
    if "Stocks" in line and "Jan" in line:
        header_line = line
        data_lines = lines[i+1:]  # as próximas linhas são os dados
        break

# Montar os cabeçalhos
columns = header_line.split()
# Corrigir se a palavra "Stocks" estiver separada
if columns[0].lower() != "stocks":
    columns = ["Stocks"] + columns

# Preparar os dados
data = []
for line in data_lines:
    parts = line.split()
    stock_name = parts[0]
    values = list(map(int, parts[1:]))
    row = [stock_name] + values
    data.append(row)

# Criar o DataFrame
df = pd.DataFrame(data, columns=columns)

# Exportar para Excel
df.to_excel("Stock Prices.xlsx", index=False)

# Exportar para CSV
df.to_csv("Stock Prices.csv", index=False)

# Exportar para JSON
df.to_json("Stock Prices.json", orient="records", indent=4)

# Exportar para banco de dados SQLite
conn = sqlite3.connect("Stock Prices.db")
df.to_sql("stock_prices", conn, if_exists="replace", index=False)
conn.close()

print("✅ Arquivos gerados com sucesso:")
print("   - Stock Prices.xlsx")
print("   - Stock Prices.csv")
print("   - Stock Prices.json")
print("   - Stock Prices.db (tabela: stock_prices)")
