import pandas as pd
import rpa as r
from time import sleep

# Função para preencher o formulário
def fill_form(row):
    try:
        r.url('https://codenboxautomationlab.com/registration-form/')
        r.type('//*[@name="fname"]', str(row["First Name"]))
        r.type('//*[@name="lname"]', str(row["Last Name"]))
        r.type('//*[@name="email"]', str(row["Email"]))
        r.select('//*[@name="nf-field-22"]', str(row["Course"]))
        r.select('//*[@name="nf-field-24"]', str(row["Enroll Month"]))
        r.click('//*[@id="nf-field-23-6"]')
        r.click('//*[@id="nf-field-15"]')
        sleep(2)  # Aguarda o formulário ser enviado
        print(f"Formulário preenchido para {row['Email']}")
    except Exception as e:
        print(f"Erro ao preencher para {row['Email']}: {e}")

# Busca o arquivo Excel
try:
    input_df = pd.read_excel(r"C:\Users\emer7\OneDrive\Área de Trabalho\Training.xlsx")
except FileNotFoundError:
    print("Erro: Arquivo 'Training.xlsx' não encontrado.")
    exit()

# Inicializa o navegador
r.init()

# Loop para cada linha
for index, row in input_df.iterrows():
    fill_form(row)

# Fecha o navegador
r.close()